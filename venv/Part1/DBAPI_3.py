# For Error Handling
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='COYG1995!!', db='kleague', charset='utf8')

try:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM player"
        cursor.execute(sql)
        players = cursor.fetchall()
        print(players)
except Exception as e:
    print(e)
    print(type(e))
finally:
    conn.close()