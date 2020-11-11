import sys
import pymysql
from PyQt5.QtWidgets import *
import csv
import json
import xml

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

class DB_Updates:

    def createNewPlayerTable(self, t_name):
        sql = f"""CREATE TABLE {t_name} (
                        player_id     CHAR(7) 		NOT NULL,
                        player_name   VARCHAR(20) 	NOT NULL,
                        team_id       CHAR(3) 		NOT NULL,
                        e_player_name VARCHAR(40),
                        nickname      VARCHAR(30),
                        join_YYYY     CHAR(4),
                        position      VARCHAR(10),
                        back_no       TINYINT,
                        nation        VARCHAR(20),
                        birth_date    DATE,
                        solar         CHAR(1),
                        height        SMALLINT,
                        weight        SMALLINT,
                        CONSTRAINT 	  pk_player 		PRIMARY KEY (player_id)
                    )"""
        params = ()
        util = DB_Utils()
        util.updateExecutor(db='kleague', sql=sql, params=params)

    def populateNewPlayerTable(self, player_id, player_name, team_id, e_player_name, nickname, join_YYYY, position, back_no, nation, birth_date, solar, height, weight):
        sql = "INSERT INTO playerGK VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (player_id, player_name, team_id, e_player_name, nickname, join_YYYY, position, back_no, nation, birth_date, solar, height, weight)
        util = DB_Utils()
        util.updateExecutor(db="kleague", sql=sql, params=params)

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


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.condition_team_id = self.comboBox1.currentText()
        self.condition_position = self.comboBox2.currentText()
        self.condition_nation = self.comboBox3.currentText()
        self.condition_height = self.comboBox4.currentText()
        self.condition_height_lower = self.radioButton1.isChecked()
        self.condition_height_higher = self.radioButton2.isChecked()
        self.condition_weight = self.comboBox5.currentText()
        self.condition_weight_lower = self.radioButton3.isChecked()
        self.condition_weight_higher = self.radioButton4.isChecked()
        self.condition_CSV = self.radioButton5.isChecked()
        self.condition_JSON = self.radioButton6.isChecked()
        self.condition_XML = self.radioButton7.isChecked()
        self.filtered_player = []

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
        self.comboBox4.activated.connect(self.height_activated)
        self.comboTitle4 = QLabel("키", self)
        self.radioButton1 = QRadioButton("이상", self)
        self.radioButton1.clicked.connect(self.radio1_checked)
        self.radioButton2 = QRadioButton("이하", self)
        self.radioButton2.clicked.connect(self.radio2_checked)
        self.comboBox5 = QComboBox(self)
        self.comboBox5.activated.connect(self.weight_activated)
        self.comboTitle5 = QLabel("몸무게", self)
        self.radioButton3 = QRadioButton("이상", self)
        self.radioButton3.clicked.connect(self.radio3_checked)
        self.radioButton4 = QRadioButton("이하", self)
        self.radioButton4.clicked.connect(self.radio4_checked)

        self.pushButton1 = QPushButton("초기화", self)
        self.pushButton1.clicked.connect(self.clearButton_Clicked)
        self.pushButton2 = QPushButton("검색", self)
        self.pushButton2.clicked.connect(self.searchButton_Clicked)


        self.radioButton5 = QRadioButton("CSV", self)
        self.radioButton5.clicked.connect(self.radio5_checked)
        self.radioButton6 = QRadioButton("JSON", self)
        self.radioButton6.clicked.connect(self.radio6_checked)
        self.radioButton7 = QRadioButton("XML", self)
        self.radioButton7.clicked.connect(self.radio7_checked)
        self.pushButton3 = QPushButton("저장", self)
        self.pushButton3.clicked.connect(self.saveButton_Clicked)



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

        # Table settings
        columnNames = list(players[0].keys())
        self.tableWidget = QTableWidget(len(players), 13)
        self.tableWidget.setHorizontalHeaderLabels(columnNames)

        # Temp
        i = 0

        for player in players:
            j = 0
            for columnName in columnNames:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(player[columnName])))
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

    def position_activated(self):
        self.condition_position = self.comboBox2.currentText()

    def nation_activated(self):
        self.condition_nation = self.comboBox3.currentText()

    def height_activated(self):
        self.condition_height = self.comboBox4.currentText()
    def radio1_checked(self):
        self.condition_height_higher = True
    def radio2_checked(self):
        self.condition_height_lower = True

    def weight_activated(self):
        self.condition_weight = self.comboBox5.currentText()
    def radio3_checked(self):
        self.condition_weight_higher = True
    def radio4_checked(self):
        self.condition_weight_lower = True

    def radio5_checked(self):
        self.condition_CSV = True
        self.condition_JSON = False
        self.condition_XML = False
    def radio6_checked(self):
        self.condition_JSON = True
        self.condition_CSV = False
        self.condition_XML = False
    def radio7_checked(self):
        self.condition_XML = True
        self.condition_JSON = False
        self.condition_CSV = False

    def clearButton_Clicked(self):
        i = 0
        query = DB_Queries()
        players = query.selectAllplayer()
        columnNames = list(players[0].keys())
        self.tableWidget.setRowCount(len(players))
        for player in players:
            j = 0
            for columnName in columnNames:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(player[columnName])))
                j += 1
            i += 1

    def searchButton_Clicked(self):
        i = 0
        query = DB_Queries()
        players = query.selectAllplayer()
        columnNames = list(players[0].keys())
        self.filtered_player = []
        for player in players:
            status_Team = False
            status_Position = False
            status_nation = False
            status_height = False
            status_weight = False
            for columnName in columnNames:
                if columnName == 'TEAM_ID':
                    if self.condition_team_id == '없음':
                        status_Team = True
                    elif self.condition_team_id == player[columnName]:
                        status_Team = True
                    else: status_Team = False
                if columnName == 'POSITION':
                    if self.condition_position == '없음':
                        status_Position = True
                    elif self.condition_position == player[columnName]:
                        status_Position = True
                    else: status_Position = False
                if columnName == 'NATION':
                    if self.condition_nation == '모두':
                        status_nation = True
                    elif self.condition_nation != '모두':
                        if player[columnName] is None:
                            if self.condition_nation == '대한민국':
                                player[columnName] = '대한민국'
                                status_nation = True
                        else:
                            if self.condition_nation == player[columnName]:
                                status_nation = True
                    else: status_nation = False
                if columnName == 'HEIGHT':
                    if self.condition_height == '없음':
                        status_height = True
                    else:
                        if self.condition_height_lower:
                            if player[columnName] is not None and int(player[columnName]) <= int(self.condition_height):
                                status_height = True
                        elif self.condition_height_higher:
                            if player[columnName] is not None and int(player[columnName]) >= int(self.condition_height):
                                status_height = True
                        else: status_height = False
                if columnName == 'WEIGHT':
                    if self.condition_weight == '없음':
                        status_weight = True
                    else:
                        if self.condition_weight_lower:
                            if player[columnName] is not None and int(player[columnName]) <= int(self.condition_weight):
                                status_weight = True
                        elif self.condition_weight_higher:
                            if player[columnName] is not None and int(player[columnName]) >= int(self.condition_weight):
                                status_weight = True
                        else: status_weight = False

            if status_Team and status_Position and status_nation and status_height and status_weight:
                self.filtered_player.append(player)

        self.tableWidget.setRowCount(len(self.filtered_player))
        for player in self.filtered_player:
            # print(player)
            j = 0
            for columnName in columnNames:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(player[columnName])))
                j += 1
            i += 1

    def saveButton_Clicked(self):
        # query = DB_Queries()
        # print(self.filtered_player)
        row_count = self.tableWidget.rowCount()
        column_count = self.tableWidget.columnCount()
        if self.condition_CSV:
            pass # write CSV
        elif self.condition_JSON:
            pass #write JSON
        elif self.condition_XML:
            pass #write XML
        else:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()