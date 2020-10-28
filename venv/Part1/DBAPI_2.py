# PyMySQL 사용 절차

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='COYG1995!!', db='kleague', charset='utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM player"
cursor.execute(sql)

players = cursor.fetchall() # List of Dictionary
print(len(players))
print(players)
print()

print(players[0])
print()

# Print Values
columnNames = list(players[0].keys())
print(columnNames)
print()

for player in players:
    for columnName in columnNames:
        print(player[columnName], end=' ')
    print()
print()

# Print Key and Value
for player in players:
    kvlist = list(player.items())
    for (k,v) in kvlist:
        print(k, v, end=' ')
    print()
print()

conn.close()