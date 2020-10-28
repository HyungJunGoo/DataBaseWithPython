# PyMySQL 사용 절차 (갱신문 n번 실행)

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='COYG1995!!', db='kleague', charset='utf8')

cursor = conn.cursor() # tuple based cursor

newPlayers = (
    ('202001', '손흥민', 'K01', 'FW'),
    ('202002', '케인', 'K02', 'FW'),
    ('202003', '로셀소', 'K01', 'MF')
)

sql = "INSERT INTO player(player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"

cursor.executemany(sql, newPlayers)
conn.commit()

sql = "SELECT * FROM player"
cursor.execute(sql)
tuples = cursor.fetchall()
print(len(tuples))
print(tuples)

conn.close()