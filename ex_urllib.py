import urllib.request

url = "http://k-son.se"
with urllib.request.urlopen(url) as response:
    html = response.read().decode("utf-8")
print(html)
