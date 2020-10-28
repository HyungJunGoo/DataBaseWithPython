# PyMySQL 사용 절차 (검색문)

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='COYG1995!!', db='kleague', charset='utf8')

cursor = conn.cursor()

sql = "SELECT * FROM player"
cursor.execute(sql)

tuples = cursor.fetchall()
print(tuples)
print(len(tuples))

print(tuples[0])

for rowIDX in range(len(tuples)):
    for columnIDX in range(len(tuples[0])):
        print(tuples[rowIDX][columnIDX], end=" ")
    print("")

conn.close()
