import xml.etree.ElementTree as ET
data= '''<person>
        <name>prince</name>
        <name>Ghoghari</name>
        <phone type="intl">9687333010</phone>
        <email hide="yes"/>
    </person>'''
tree=ET.fromstring(data)
print('NAME:',tree.find('name').text)
print('ATTR:',tree.find('email').get('hide'))
