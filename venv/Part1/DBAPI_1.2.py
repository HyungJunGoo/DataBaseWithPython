# PyMySQL 사용 절차

import pymysql

conn = pymysql.connect(host='localhost', user='root', password="COYG1995!!", db='kleague', charset='utf8')

cursor = conn.cursor()

sql = "INSERT INTO player(player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
cursor.execute(sql, ('2020001', '오바메양', 'K01', 'FW'))
conn.commit()

sql = "SELECT * FROM player"
cursor.execute(sql)
tuples = cursor.fetchall()
print(len(tuples))
print(tuples)
print()

sql = "DELETE FROM player WHERE player_id = %s"
cursor.execute(sql, '2020001')

conn.commit()

sql = "SELECT * FROM player"
cursor.execute(sql)
tuples = cursor.fetchall()
print(len(tuples))
print(tuples)
print()

conn.close()