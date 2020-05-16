import xml.etree.ElementTree as ET
data= '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>prince</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>Rid</name>
        </user>
        <user x='10'>
            <id>028</id>
            <name>aRchi</name>
        </user>
    </users>
    </stuff>'''
stuff=ET.fromstring(data)
lst=stuff.findall('users/user')
print('Users count :',len(lst))
for item in lst:
    print('Name :',item.find('name').text)
    print('ID :',item.find('id').text)
    print('ATTR :',item.get("x"))
