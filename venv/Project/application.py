import sys
import pymysql
from PyQt5.QtWidgets import *

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
    def selectAllplayer(self):
        sql = 'SELECT * FROM player'
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def selectDistinctTeam(self):
        sql = "SELECT DISTINCT team_id FROM player"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def selectDistinctPosition(self):
        sql = "SELECT DISTINCT position FROM player"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def selectDistinctNation(self):
        sql = "SELECT DISTINCT nation FROM player"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def selectPlayerUsingPosition (self, position):
        sql = 'SELECT * FROM player WHERE position = %s'
        params = (position)
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Application")
        self.setGeometry(0, 0, 600, 900)

        # set widget
        title = QLabel("선수검색", self)
        title.move(100,0)
        comboBox1 = QComboBox(self)
        comboTitle1 = QLabel("팀 명 : ", self)
        comboBox2 = QComboBox(self)
        comboTitle2 = QLabel("포지션", self)
        comboBox3 = QComboBox(self)
        comboTitle3 = QLabel("출신국", self)
        comboBox4 = QComboBox(self)
        comboTitle4 = QLabel("키", self)
        radioButton1 = QRadioButton("이상", self)
        radioButton2 = QRadioButton("이하", self)
        comboBox5 = QComboBox(self)
        comboTitle5 = QLabel("몸무게", self)
        radioButton3 = QRadioButton("이상", self)
        radioButton4 = QRadioButton("이하", self)

        pushButton1 = QPushButton("초기화", self)
        pushButton2 = QPushButton("검색", self)

        radioButton5 = QRadioButton("CSV", self)
        radioButton6 = QRadioButton("JSON", self)
        radioButton7 = QRadioButton("XML", self)
        pushButton3 = QPushButton("저장", self)



        # set layout
        qhinnerLayout1 = QHBoxLayout()
        qhinnerLayout1.addWidget(comboTitle1)
        qhinnerLayout1.addWidget(comboBox1)
        qhinnerLayout1.addWidget(comboTitle2)
        qhinnerLayout1.addWidget(comboBox2)
        qhinnerLayout1.addWidget(comboTitle3)
        qhinnerLayout1.addWidget(comboBox3)
        qhinnerLayout1.addWidget(pushButton1)

        qhinnerLayout2 = QHBoxLayout()
        # for height
        qHheightLayout = QHBoxLayout()
        qHheightLayout.addWidget(comboTitle4)
        qHheightLayout.addWidget(comboBox4)
        heightRadioLayout = QHBoxLayout()
        heightRadioLayout.addWidget(radioButton1)
        heightRadioLayout.addWidget(radioButton2)
        heightRadioGroup = QGroupBox()
        heightRadioGroup.setFlat(True)
        heightRadioGroup.setLayout(heightRadioLayout)
        qHheightLayout.addWidget(heightRadioGroup)
        # for weight
        qHweightLayout = QHBoxLayout()
        qHweightLayout.addWidget(comboTitle5)
        qHweightLayout.addWidget(comboBox5)
        weightRadioLayout = QHBoxLayout()
        weightRadioLayout.addWidget(radioButton3)
        weightRadioLayout.addWidget(radioButton4)
        weightRadioGroup = QGroupBox()
        weightRadioGroup.setFlat(True)
        weightRadioGroup.setLayout(weightRadioLayout)
        qHweightLayout.addWidget(weightRadioGroup)

        qhinnerLayout2.addLayout(qHheightLayout)
        qhinnerLayout2.addLayout(qHweightLayout)
        qhinnerLayout2.addWidget(pushButton2)

        qhinnerLayout3 = QHBoxLayout()
        qhinnerLayout3.addWidget(radioButton5)
        qhinnerLayout3.addWidget(radioButton6)
        qhinnerLayout3.addWidget(radioButton7)
        qhinnerLayout3.addWidget(pushButton3)



        query = DB_Queries()
        players = query.selectAllplayer()
        print(players[0])
        # Table settings
        columnNames = list(players[0].keys())
        tableWidget = QTableWidget(len(players), 13)
        tableWidget.setHorizontalHeaderLabels(columnNames)

        # Temp
        i = 0

        for player in players:
            i += 1
            j = 0
            for columnName in columnNames:
                tableWidget.setItem(i, j, QTableWidgetItem(str(player[columnName])))
                # print(player[columnName])
                j+=1


        # Team settings (comboBox 3)
        teams = query.selectDistinctTeam()
        teamName = list(teams[0].keys())[0]
        teamItems = ['없음' if team[teamName] == None else team[teamName] for team in teams]
        comboBox1.addItems(teamItems)

        # Position settings (comboBox2)
        positions = query.selectDistinctPosition()
        positionName = list(positions[0].keys())[0]
        positionItems = ['없음' if position[positionName] == None else position[positionName] for position in positions]
        comboBox2.addItems(positionItems)

        # Nation settings (comboBox 3)
        nations = query.selectDistinctNation()
        nationName = list(nations[0].keys())[0]
        nationItems = ['대한민국' if nation[nationName] == None else nation[nationName] for nation in nations]
        comboBox3.addItems(nationItems)
        # Out Layer
        qvinnerLayout = QVBoxLayout()
        qvinnerLayout.addWidget(title)
        qvinnerLayout.addLayout(qhinnerLayout1)
        qvinnerLayout.addLayout(qhinnerLayout2)
        qvinnerLayout.addWidget(tableWidget)
        qvinnerLayout.addLayout(qhinnerLayout3)

        self.setLayout(qvinnerLayout)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()