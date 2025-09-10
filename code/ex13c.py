# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')

print("Retrieving:", url)
i=1
while i <= int(count):
    i = i + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    
    # Retrieve all of the anchor tags
    tags = soup('a')
    pages = list()
    for tag in tags:
        pages.append(tag.get('href', None))
        
    url = pages[int(position)-1]
    print("Retrieving:", url)