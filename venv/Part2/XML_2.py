# DB Table을 읽어서, XML 파일에 쓰는 예제

import pymysql
import xml.etree.ElementTree as ET
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
        finally:
            conn.close()

class DB_Queries:

    def selectPlayerUsingPosition(self, position):
        sql = "SELECT * FROM player WHERE position = %s"
        params = (position)

        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

############################################################################################################

def readDB_writeXML():

    # DB 검색문 실행
    query = DB_Queries()
    players = query.selectPlayerUsingPosition("GK") # 딕셔너리 형태의 리스트
    print(players)
    print()

    # Attribute BIRTH_DATE의 값을 MySQL datetime 타입에서 스트링으로 변환하겠다. (CSV에서는 패키지가 변환을 해줌)
    for player in players:
        for k,v in player.items():
            if isinstance(v, datetime.date):
                player[k] = v.strftime('%Y-%m-%d')

    newDict = dict(playerGK=players)
    print(newDict)

    # XDM 트리 생성
    tableName = list(newDict.keys())[0]
    tableRows = list(newDict.values())[0]

    rootElement = ET.Element('Table')
    rootElement.attrib['name'] = tableName

    for row in tableRows: # row는 각각의 딕셔너리
        rowElement = ET.Element("Row")
        rootElement.append(rowElement)

        for columnName in list(row.keys()):
            if row[columnName] == None:
                rowElement.attrib[columnName] = ''
            else:
                rowElement.attrib[columnName] = row[columnName]
            if type(row[columnName]) == int:
                rowElement.attrib[columnName] = str(row[columnName])

    # XDM 트리를 화일에 출력
    ET.ElementTree(rootElement).write('playersGK.xml', encoding='utf-8', xml_declaration=True)


readDB_writeXML()