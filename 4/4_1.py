import requests
res = requests.get('https://cowboy-spike-spiegel.github.io/')
print(res.status_code)
print(res.url)
print(res.headers)