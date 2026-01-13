from urllib.request import urlopen

url = "https://www.dalailalkhayrat.com/"

page = urlopen(url)

print(page.read().decode("utf-8"))