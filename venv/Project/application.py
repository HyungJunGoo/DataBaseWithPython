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

    def selectDistinctHeight(self):
        sql = "SELECT DISTINCT height FROM player ORDER BY height ASC"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def selectDistinctWeight(self):
        sql = "SELECT DISTINCT weight FROM player ORDER BY weight ASC"
        params = ()
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def selectPlayerUsingTeam (self, Team):
        sql = 'SELECT * FROM player WHERE team_id = %s'
        params = (Team)
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def selectPlayerUsingPosition(self, Position):
        sql = 'SELECT * FROM player WHERE position = %s'
        params = (Position)
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples

    def intersection(self, team, position, nation):
        sql = "SELECT * FROM player WHERE team_id = %s AND position = %s AND nation = %s"
        sql = """PREPARE statement FROM 'SELECT * FROM player WHERE team_id = ? AND position = ? AND nation = ?;'
                 SET @a = (%s, %s, %s);
                 Execute statement using @a;
                """
        params = (team, position, nation)
        util = DB_Utils()
        tuples = util.queryExecutor(db='kleague', sql=sql, params=params)
        return tuples


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.condition_team_id = self.comboBox1.currentText()
        self.condition_position = self.comboBox2.currentText()
        self.condition_nation = self.comboBox3.currentText()
        self.condition_height = self.comboBox4.currentText()
        self.condition_weight = self.comboBox5.currentText()

    def setupUI(self):
        self.setWindowTitle("Application")
        self.setGeometry(0, 0, 600, 900)

        # set widget
        self.title = QLabel("선수검색", self)
        self.title.move(100,0)
        self.comboBox1 = QComboBox(self)
        self.comboBox1.activated.connect(self.team_id_activated)
        self.comboTitle1 = QLabel("팀 명 : ", self)
        self.comboBox2 = QComboBox(self)
        self.comboBox2.activated.connect(self.position_activated)
        self.comboTitle2 = QLabel("포지션", self)
        self.comboBox3 = QComboBox(self)
        self.comboBox3.activated.connect(self.nation_activated)
        self.comboTitle3 = QLabel("출신국", self)
        self.comboBox4 = QComboBox(self)
        self.comboTitle4 = QLabel("키", self)
        self.radioButton1 = QRadioButton("이상", self)
        self.radioButton2 = QRadioButton("이하", self)
        self.comboBox5 = QComboBox(self)
        self.comboTitle5 = QLabel("몸무게", self)
        self.radioButton3 = QRadioButton("이상", self)
        self.radioButton4 = QRadioButton("이하", self)

        self.pushButton1 = QPushButton("초기화", self)
        # pushButton1.clicked.connect()
        self.pushButton2 = QPushButton("검색", self)
        self.pushButton2.clicked.connect(self.searchButton_Clicked)


        self.radioButton5 = QRadioButton("CSV", self)
        self.radioButton6 = QRadioButton("JSON", self)
        self.radioButton7 = QRadioButton("XML", self)
        self.pushButton3 = QPushButton("저장", self)



        # set layout
        self.qhinnerLayout1 = QHBoxLayout()
        self.qhinnerLayout1.addWidget(self.comboTitle1)
        self.qhinnerLayout1.addWidget(self.comboBox1)
        self.qhinnerLayout1.addWidget(self.comboTitle2)
        self.qhinnerLayout1.addWidget(self.comboBox2)
        self.qhinnerLayout1.addWidget(self.comboTitle3)
        self.qhinnerLayout1.addWidget(self.comboBox3)
        self.qhinnerLayout1.addWidget(self.pushButton1)

        self.qhinnerLayout2 = QHBoxLayout()
        # for height
        self.qHheightLayout = QHBoxLayout()
        self.qHheightLayout.addWidget(self.comboTitle4)
        self.qHheightLayout.addWidget(self.comboBox4)
        self.heightRadioLayout = QHBoxLayout()
        self.heightRadioLayout.addWidget(self.radioButton1)
        self.heightRadioLayout.addWidget(self.radioButton2)
        self.heightRadioGroup = QGroupBox()
        self.heightRadioGroup.setFlat(True)
        self.heightRadioGroup.setLayout(self.heightRadioLayout)
        self.qHheightLayout.addWidget(self.heightRadioGroup)
        # for weight
        self.qHweightLayout = QHBoxLayout()
        self.qHweightLayout.addWidget(self.comboTitle5)
        self.qHweightLayout.addWidget(self.comboBox5)
        self.weightRadioLayout = QHBoxLayout()
        self.weightRadioLayout.addWidget(self.radioButton3)
        self.weightRadioLayout.addWidget(self.radioButton4)
        self.weightRadioGroup = QGroupBox()
        self.weightRadioGroup.setFlat(True)
        self.weightRadioGroup.setLayout(self.weightRadioLayout)
        self.qHweightLayout.addWidget(self.weightRadioGroup)

        self.qhinnerLayout2.addLayout(self.qHheightLayout)
        self.qhinnerLayout2.addLayout(self.qHweightLayout)
        self.qhinnerLayout2.addWidget(self.pushButton2)

        self.qhinnerLayout3 = QHBoxLayout()
        self.qhinnerLayout3.addWidget(self.radioButton5)
        self.qhinnerLayout3.addWidget(self.radioButton6)
        self.qhinnerLayout3.addWidget(self.radioButton7)
        self.qhinnerLayout3.addWidget(self.pushButton3)



        query = DB_Queries()
        players = query.selectAllplayer()
        # print(players[0])
        # Table settings
        columnNames = list(players[0].keys())
        self.tableWidget = QTableWidget(len(players), 13)
        self.tableWidget.setHorizontalHeaderLabels(columnNames)

        # # Temp
        i = 0

        for player in players:
            j = 0
            for columnName in columnNames:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(player[columnName])))
                # print(player[columnName])
                j+=1
            i += 1


        # Team settings (comboBox 1)
        teams = query.selectDistinctTeam()
        teamName = list(teams[0].keys())[0]
        teamItems = ['없음' if team[teamName] == None else team[teamName] for team in teams]
        teamItems.append('없음')
        self.comboBox1.addItems(teamItems)
        self.comboBox1.setCurrentText('없음')

        # Position settings (comboBox2)
        positions = query.selectDistinctPosition()
        positionName = list(positions[0].keys())[0]
        positionItems = ['없음' if position[positionName] == None else position[positionName] for position in positions]
        self.comboBox2.addItems(positionItems)
        self.comboBox2.setCurrentText('없음')

        # Nation settings (comboBox 3)
        nations = query.selectDistinctNation()
        nationName = list(nations[0].keys())[0]
        nationItems = ['대한민국' if nation[nationName] == None else nation[nationName] for nation in nations]
        nationItems.append('모두')
        self.comboBox3.addItems(nationItems)
        self.comboBox3.setCurrentText("모두")

        # Height settings (comboBox 4)
        heights = query.selectDistinctHeight()
        wholeHeights = list(heights[0].keys())[0]
        heightItems = ['없음' if height[wholeHeights] == None else str(height[wholeHeights]) for height in heights]
        self.comboBox4.addItems(heightItems)

        # Weight settings (comboBox 5)
        weights = query.selectDistinctWeight()
        wholeWeights = list(weights[0].keys())[0]
        weightItems = ['없음' if weight[wholeWeights] == None else str(weight[wholeWeights]) for weight in weights]
        self.comboBox5.addItems(weightItems)
        # Out Layer

        self.qvinnerLayout = QVBoxLayout()
        self.qvinnerLayout.addWidget(self.title)
        self.qvinnerLayout.addLayout(self.qhinnerLayout1)
        self.qvinnerLayout.addLayout(self.qhinnerLayout2)
        self.qvinnerLayout.addWidget(self.tableWidget)
        self.qvinnerLayout.addLayout(self.qhinnerLayout3)

        self.setLayout(self.qvinnerLayout)

    def team_id_activated(self):
        self.condition_team_id = self.comboBox1.currentText()
        print(self.condition_team_id)
        pass

    def position_activated(self):
        self.condition_position = self.comboBox2.currentText()
        print(self.condition_position)
        pass

    def nation_activated(self):
        self.condition_nation = self.comboBox3.currentText()
        print(self.condition_nation)
        pass

    def searchButton_Clicked(self):

        i = 0
        query = DB_Queries()
        if self.condition_team_id == '없음' and self.condition_position == '없음' and self.condition_nation == '모두':
            players = query.selectAllplayer()
        else:
            if self.condition_team_id == '없음':
                self.condition_team_id = '*'
            if self.condition_position == '없음':
                self.condition_position = '*'
            if self.condition_nation == '모두':
                self.condition_nation = '*'
            players = query.intersection(self.condition_team_id, self.condition_position, self.condition_nation)

        # if self.condition_team_id == '없음':
        #     players_by_team_id = query.selectAllplayer()
        # else:
        #     players_by_team_id = query.selectPlayerUsingTeam(self.condition_team_id)
        #
        # if self.condition_position == '없음':
        #     players_by_position = query.selectAllplayer()
        # else:
        #     players_by_position = query.selectPlayerUsingPosition(self.condition_position)
        #
        # players = list(set(players_by_team_id)&set(players_by_position))
        print(players)
        self.tableWidget.setRowCount(len(players))
        columnNames = list(players[0].keys())

        for player in players:
            print(player)
            j = 0
            for columnName in columnNames:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(player[columnName])))
                j += 1
            i += 1





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()