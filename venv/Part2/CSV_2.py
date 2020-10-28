# DB Table을 읽어서, CSV 파일로 쓰는 예제

import  pymysql
import csv

class DB_Utils:

    def queryExecutor(self, db, sql, params):
        conn = pymysql.connect(host='localhost', user='root', password='COYG1995!!', db=db, charset='utf8')

        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, params)
                tuples = cursor.fetchall()
                return tuples
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:

    def selectPlayerUsingPosition(self, position):
        sql = "SELECT * FROM player WHERE position = %s"
        params = (position)

        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)

        return tuples

def readDB_writeCSV():

    # DB 검색문 실행
    query = DB_Queries()
    players = query.selectPlayerUsingPosition("GK")

    print(players)
    print()

    # CSV 파일을 쓰기 모드로 생성
    with open('playerGK.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)

        # 테읻블 헤더 출력
        columnNames = list(players[0].keys())
        print(columnNames)
        print()

        wr.writerows(columnNames)

        for rowIDX in range(len(players)):
            row = list(players[rowIDX].values())
            print(row)
            wr.writerow(row)

readDB_writeCSV()
