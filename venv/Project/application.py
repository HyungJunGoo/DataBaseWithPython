import sys
import pymysql
from PyQt5.QtWidgets import *

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

        tableWidget = QTableWidget(50, 6)

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