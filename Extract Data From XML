import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    url = input('Enter location - ')
    if len(url) < 1 : break

    lst = list()
    ul = url + urllib.parse.urlencode(lst)
    print('Retrieving:', ul)

    xml = urllib.request.urlopen(ul, context=ctx)
    ht = xml.read().decode()
    print('retrieved', len(ht), 'characters')

    tree = ET.fromstring(ht)
    counts = tree.findall('comments/comment')
    print('comment count', len(counts))
    count = 0
    for i in counts :
        com = i.find('count').text
        fl = int(com)
        count = count + fl
    print('sum:', count)
