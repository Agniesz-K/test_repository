from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
count = 0
total = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    total = total + int(tag.contents[0])
    count = count +1
    
print("Count", count)
print("Sum", total)
   