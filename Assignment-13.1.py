import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
connection = urllib.request.urlopen(url)
data = connection.read().decode()
print('Retrieving', url)
print('Retrieving', len(data), 'characters')

info = json.loads(data)
count = 0
sum = 0
for item in info['comments']:
    sum = sum + int(item['count'])
    count = count + 1
print('Count: ', count)
print('Sum: ', sum)