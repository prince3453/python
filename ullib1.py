import urllib,urllib.request
from bs4 import BeautifulSoup

url = 'http://python-data.dr-chuck.net/known_by_Damian.html'
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
