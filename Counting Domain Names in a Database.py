import sqlite3

conn = sqlite3.connect('org.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('''CREATE TABLE counts
            (org TEXT, count INTEGER)''')

file = input('Enter the file:')
if len(file) < 1: file = 'mbox.txt'
fl = open(file)
for i in fl:
    if not i.startswith('From:') : continue
    div = i.split()[1]
    dom = div.split('@')[1]
    cur.execute('SELECT * FROM counts WHERE org = ?',(dom,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO counts (org, count)
                    VALUES (?, 1)''', (dom,))
    else:
        cur.execute('''UPDATE counts SET count = count + 1
                    WHERE org = ?''', (dom,))
conn.commit()
