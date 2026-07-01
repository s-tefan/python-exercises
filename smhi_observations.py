"""
SMHI Weather Observations
Fetch weather observations from SMHI's open data API.
https://opendata-download-metobs.smhi.se

Usage:
    python smhi_observations.py

Requirements:
    pip install requests
"""

import csv
import io
import requests
from datetime import datetime, timezone

BASE_URL = "https://opendata-download-metobs.smhi.se/api/version/latest"

PARAMETERS = [
    {"key": 1,  "label": "Air temperature",        "unit": "°C",  "group": "Temperature"},
    {"key": 19, "label": "Min temperature (day)",   "unit": "°C",  "group": "Temperature"},
    {"key": 20, "label": "Max temperature (day)",   "unit": "°C",  "group": "Temperature"},
    {"key": 39, "label": "Min temperature (night)", "unit": "°C",  "group": "Temperature"},
    {"key": 4,  "label": "Wind speed",              "unit": "m/s", "group": "Wind"},
    {"key": 25, "label": "Wind direction",          "unit": "°",   "group": "Wind"},
    {"key": 26, "label": "Gust speed",              "unit": "m/s", "group": "Wind"},
    {"key": 6,  "label": "Relative humidity",       "unit": "%",   "group": "Other"},
    {"key": 7,  "label": "Precipitation",           "unit": "mm",  "group": "Other"},
    {"key": 9,  "label": "Air pressure",            "unit": "hPa", "group": "Other"},
]

PERIODS = [
    {"key": "latest-hour",        "label": "Latest hour"},
    {"key": "latest-day",         "label": "Latest day"},
    {"key": "latest-months",      "label": "Last 4 months"},
    {"key": "corrected-archive",  "label": "Full archive"},
]


# ── Formatting helpers ────────────────────────────────────────────────────────

def fmt_ts(unix_ms: int, period: str) -> str:
    """Convert a UNIX timestamp (ms) to a readable local string."""
    dt = datetime.fromtimestamp(unix_ms / 1000, tz=timezone.utc).astimezone()
    if period in ("latest-hour", "latest-day"):
        return dt.strftime("%d %b %H:%M")
    elif period == "latest-months":
        return dt.strftime("%d %b")
    else:
        return dt.strftime("%Y-%m-%d")


def fmt_value(raw: str, unit: str) -> str:
    try:
        v = float(raw)
        return f"{v:.1f} {unit}"
    except ValueError:
        return f"{raw} {unit}"


def separator(char: str = "─", width: int = 52) -> None:
    print(char * width)


# ── API calls ─────────────────────────────────────────────────────────────────

def fetch_stations(param_key: int) -> list[dict]:
    url = f"{BASE_URL}/parameter/{param_key}/station.json"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json().get("station", [])


def fetch_data(param_key: int, station_key: int, period: str) -> list[dict]:
    """
    Fetch observations. corrected-archive is CSV-only; all other periods are JSON.
    Returns a unified list of {"date": unix_ms, "value": str} dicts.
    """
    if period == "corrected-archive":
        url = f"{BASE_URL}/parameter/{param_key}/station/{station_key}/period/{period}/data.csv"
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        return _parse_archive_csv(resp.text)
    else:
        url = f"{BASE_URL}/parameter/{param_key}/station/{station_key}/period/{period}/data.json"
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        return resp.json().get("value", [])


def _parse_archive_csv(text: str) -> list[dict]:
    """
    Parse SMHI corrected-archive CSV into unified list of {"date": unix_ms, "value": str}.

    Two layouts exist depending on parameter:
      Layout A (e.g. air temperature):
        col 0: YYYY-MM-DD  col 1: HH:MM:SS  col 2: value  col 3: quality
      Layout B (e.g. daily min/max):
        col 0: from_datetime  col 1: to_datetime  col 2: YYYY-MM-DD  col 3: value  col 4: quality
    """
    results = []
    lines = text.splitlines()

    # Find the first data header line
    data_start = None
    for i, line in enumerate(lines):
        if line.startswith("Datum") or line.startswith("Från Datum"):
            data_start = i
            break
    if data_start is None:
        return results

    rows = list(csv.reader(lines[data_start + 1:], delimiter=";"))  # skip header
    if not rows:
        return results

    # Detect layout from first non-empty row
    sample = next((r for r in rows if len(r) >= 3), None)
    if sample is None:
        return results

    # Layout B: col[2] is a plain date YYYY-MM-DD (exactly 10 chars, no spaces)
    if len(sample) >= 4 and len(sample[2].strip()) == 10 and " " not in sample[2].strip():
        date_i, val_i, fixed_time = 2, 3, "12:00:00"
    else:
        date_i, val_i, fixed_time = 0, 2, None

    for row in rows:
        if len(row) <= val_i:
            continue
        date_str = row[date_i].strip()
        time_str = fixed_time if fixed_time else row[1].strip()
        raw_val  = row[val_i].strip()
        if not date_str or not raw_val:
            continue
        try:
            dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M:%S")
            unix_ms = int(dt.replace(tzinfo=timezone.utc).timestamp() * 1000)
            results.append({"date": unix_ms, "value": raw_val})
        except ValueError:
            continue

    return results


# ── UI helpers ────────────────────────────────────────────────────────────────

def choose(prompt: str, options: list, display_fn=None) -> int:
    """
    Print a numbered list of options and return the chosen index (0-based).
    display_fn(item) -> str   — optional, defaults to str(item)
    """
    print()
    for i, item in enumerate(options, 1):
        label = display_fn(item) if display_fn else str(item)
        print(f"  {i:>2}. {label}")
    print()
    while True:
        raw = input(f"{prompt} [1-{len(options)}]: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return int(raw) - 1
        print(f"      Please enter a number between 1 and {len(options)}.")


def search_stations(stations: list[dict], query: str) -> list[dict]:
    q = query.lower()
    return [s for s in stations if q in s.get("name", "").lower()]


# ── Display ───────────────────────────────────────────────────────────────────

def display_single(name: str, param: dict, values: list[dict], period: str) -> None:
    latest = values[-1]
    separator()
    print(f"  Station : {name}")
    print(f"  Parameter: {param['label']}")
    print(f"  Value   : {fmt_value(str(latest['value']), param['unit'])}")
    print(f"  Time    : {fmt_ts(latest['date'], period)}")
    separator()


def display_table(name: str, param: dict, values: list[dict], period: str,
                  max_rows: int = 50) -> None:
    rows = values[-max_rows:][::-1]   # most recent first, capped
    separator()
    print(f"  {name}  —  {param['label']} ({PERIODS[[p['key'] for p in PERIODS].index(period)]['label']})")
    separator()
    col_w = 14
    print(f"  {'Date':<{col_w}}  Value")
    separator("·")
    for r in rows:
        date_str = fmt_ts(r["date"], period)
        val_str  = fmt_value(str(r["value"]), param["unit"])
        print(f"  {date_str:<{col_w}}  {val_str}")
    separator()
    if len(values) > max_rows:
        print(f"  Showing {max_rows} of {len(values)} observations.")
        separator()


# ── Main flow ─────────────────────────────────────────────────────────────────

def main() -> None:
    print()
    print("  SMHI Weather Observations")
    print("  Data: opendata-download-metobs.smhi.se")
    separator("═")

    # 1. Choose parameter
    groups = {}
    for p in PARAMETERS:
        groups.setdefault(p["group"], []).append(p)

    flat_params: list[dict] = []
    print("\n  Parameters:")
    separator("·")
    for group, items in groups.items():
        print(f"  {group}")
        for item in items:
            flat_params.append(item)
            print(f"    {len(flat_params):>2}. {item['label']} ({item['unit']})")

    print()
    while True:
        raw = input(f"  Choose parameter [1-{len(flat_params)}]: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(flat_params):
            param = flat_params[int(raw) - 1]
            break
        print(f"     Enter a number between 1 and {len(flat_params)}.")

    # 2. Choose period
    period_idx = choose(
        "  Choose time period",
        PERIODS,
        display_fn=lambda p: p["label"],
    )
    period = PERIODS[period_idx]

    # 3. Search station
    print()
    print(f"  Fetching stations for '{param['label']}'…")
    try:
        stations = fetch_stations(param["key"])
    except requests.RequestException as e:
        print(f"\n  Error fetching stations: {e}")
        return

    while True:
        query = input("  Search station name: ").strip()
        if not query:
            continue
        matches = search_stations(stations, query)
        if not matches:
            print(f"  No stations found for '{query}'. Try again.")
            continue

        station_idx = choose(
            "  Choose station",
            matches[:10],
            display_fn=lambda s: (
                f"{s['name']}"
                + (f"  ({s['latitude']:.2f}°N, {s['longitude']:.2f}°E)" if s.get("latitude") else "")
                + ("  [inactive]" if not s.get("active") else "")
            ),
        )
        station = matches[:10][station_idx]
        break

    # 4. Fetch and display observations
    print(f"\n  Fetching {period['label'].lower()} data for {station['name']}…")
    try:
        values = fetch_data(param["key"], station["key"], period["key"])
    except requests.RequestException as e:
        print(f"\n  Error fetching data: {e}")
        return

    if not values:
        print("\n  No data available for this station / period combination.")
        return

    print()
    if period["key"] in ("latest-hour", "latest-day"):
        display_single(station["name"], param, values, period["key"])
    else:
        display_table(station["name"], param, values, period["key"])

    # 5. Loop — fetch another?
    print()
    again = input("  Fetch another observation? [y/N]: ").strip().lower()
    if again == "y":
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Goodbye!")
