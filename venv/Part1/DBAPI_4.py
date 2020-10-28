# Dynamic SQL

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='COYG1995!!', db='kleague', charset='utf8')

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM player WHERE position = %s" #dynamic SQL
        params = "FW"
        cursor.execute(sql, params)
        players = cursor.fetchall()
        print(players)
except Exception as e:
    print(e)
    print(type(e))
finally:
    conn.close()