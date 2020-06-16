import xml.etree.ElementTree as ET

data = '''
<users>
 <user>
  <name>omar</name>
  <phone type="intl" >
   +2027687644
  </phone>
  <email hide="yes" />
 </user>
 <user>
  <name>anna</name>
  <phone type="intl" >
   +2029876533
  </phone>
  <email hide="yes" />
 </user>
</users>'''

tree = ET.fromstring(data)
s = len(tree)
x = int(s)
print(x)

for i in tree:
    print('Name:', i.find('name').text)
    print('attri:', i.find('email').get('hide'))
