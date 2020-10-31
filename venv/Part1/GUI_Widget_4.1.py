import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("TableWidget 예제")
        self.setGeometry(0, 0, 400, 220)

        players = [
            {"PLAYER_ID" : "2020001", "PLAYER_NAME":"손흥민", "TEAM_ID":"K01", "POSITION":"FW"},
            {"PLAYER_ID" : "2020002", "PLAYER_NAME":"케인", "TEAM_ID":"K02", "POSITION":"FW"},
            {"PLAYER_ID" : "2020003", "PLAYER_NAME":"메시", "TEAM_ID":"K03", "POSITION":"FW"}
        ]
        columnNames = list(players[0].keys())

        # 테이블위젯 설정
        self.tableWidget = QTableWidget(self) # QTableWidget 객체 생성
        self.tableWidget.setGeometry(50, 50, 300, 120)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers) # ?
        self.tableWidget.setHorizontalHeaderLabels(columnNames)

        for rowIDX in range(len(players)):
            player = players[rowIDX]

            for k,v in player.items():
                columnIDX = columnNames.index(k)
                item = QTableWidgetItem(v)      # QTableWidgetItem 객체 생성
                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()