import urllib.request
import re
req = urllib.request.Request('https://pin.it/DfR37ocVv', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
urls = re.findall(r'"contentUrl":"([^"]+)"', html)
print(urls)
