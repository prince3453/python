import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=' http://py4e-data.dr-chuck.net/comments_555529.xml'
ur=urllib.request.urlopen(url)
data=ur.read()
stuff=ET.fromstring(data)
lst=stuff.findall('.//count')
print('Users count :',len(lst))
total=0
for item in lst:
    total=total+int(item.text)
print(total)
