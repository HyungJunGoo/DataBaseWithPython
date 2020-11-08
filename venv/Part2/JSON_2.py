# DB Table을 읽어서, JSON 파일에 쓰는 예제

import pymysql
import json
import datetime

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
            print()

        finally:
            conn.close()


class DB_Queries:

    def selectPlayerUsingPosition(self, position):
        sql = "SELECT * FROM player WHERE position = %s"
        params = (position)

        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

#############################################

def readDB_writeJSON():

    # DB 검색문 실행
    query = DB_Queries()
    players = query.selectPlayerUsingPosition("GK") # 딕셔너리의 리스트
    print(players)
    print()

    # Attribyte BIRTH_DATE의 값을 MySQL datetime 타입에서 스트링으로 변환 (CSV에서는 패키지가 변환함)
    for player in players:
        for k, v in player.items():
            if isinstance(v, datetime.date):
                player[k] = v.strftime('%Y-%m-%d') #키가 k인 item의 값 v를 수정
                print(player[k])

    print()

    newDict = dict(playerGK = players)
    print(newDict)

    # JSON 파일에 쓰기
    # dump()에 의해 모든 작은 따옴표('')는 큰 따옴표("")로 변환됨
    with open('playerGK.json', 'w', encoding='utf-8') as f:
        json.dump(newDict, f, ensure_ascii=False)

    with open("playerGK_indent.json", 'w', encoding='utf-8') as f:
        json.dump(newDict, f, indent=4, ensure_ascii=False)

readDB_writeJSON()
