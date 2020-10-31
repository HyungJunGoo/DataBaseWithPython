import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("TableWidget 예제")
        self.setGeometry(0, 0, 400, 220)

        players = {
            'PLAYER_ID': ['2020001', '2020002', '2020003'],
            'PLAYER_NAME': ['손홍민', '호날두', '메시'],
            'TEAM_ID': ['K01', 'K02', 'K03'],
            'POSITION': ['FW', 'FW', 'FW']
        }
        columnNames = list(players.keys())

        # 테이블 위젯 설정
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 300, 120)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setHorizontalHeaderLabels(columnNames)

        for k, v in players.items():
            columnIDX = columnNames.index(k)

            for rowIDX, val in enumerate(v):
                item = QTableWidgetItem(val)
                if columnIDX == 1:
                    item.setTextAlignment(Qt.AlignRight)
                self.tableWidget.setItem(rowIDX, columnIDX, item)

        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()

################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()