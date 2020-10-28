# Class

import pymysql

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

    def updateExecutor(self, db, sql, params):

        conn = pymysql.connect(host='localhost', user='root', password='COYG1995!!', db=db, charset='utf8')

        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
            print(type(e))
        finally:
            conn.close()

class DB_Queries:

    def selectPlayer(self, position):
        sql = 'SELECT * FROM player WHERE position = %s'
        params = (position)

        util = DB_Utils()
        tuples = util.queryExecutor(db="kleague", sql=sql, params=params)
        return tuples

class DB_Updates:

    def insertPlayer(self, player_id, player_name, team_id, position):
        sql = "INSERT INTO player(player_id, player_name, team_id, position) VALUES (%s, %s, %s, %s)"
        params = (player_id, player_name, team_id, position)

        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)


################################################################

if __name__ == "__main__":
    query = DB_Queries()
    players = query.selectPlayer("FW")
    print(len(players))
    print(players)

    update = DB_Updates()
    update.insertPlayer("202004", "메시", "K06", "FW")

    players = query.selectPlayer("FW")
    print(len(players))
    print(players)