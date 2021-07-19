import urllib.request, json

# test with temperetures from Skövde
url_str = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/83230/period/latest-day/data.json"
# url_str = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/26/station/83230/period/latest-months/data.json"

with urllib.request.urlopen(url_str) as url:
    data = json.loads(url.read().decode())
    '''
    for v in data:
        print(v)
        if type(data[v]) == type([]):
            for d in data[v]:
                print(d)
        else:
            print(data[v])
            '''
    station = data["station"]
    position = data["position"][0]
    print(f'{station["name"]}, ' + 
        f'lat {position["latitude"]}, ' + 
        f'lon {position["longitude"]}, ' +
        f'höjd {position["height"]}')
    par = data["parameter"]
    print(f'{par["name"]}, {par["summary"]}')
    for v in data["value"]:
        print(f'{v["date"]} \t{v["value"]}')