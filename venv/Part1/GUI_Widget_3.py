# Radio Button Widget
import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 윈도우 설정
        self.setWindowTitle("RadioButton 예제")
        self.setGeometry(0, 0, 400, 150)

        # 스테이터스바 설정
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

        # 그룹박스 설정
        self.GroupBox = QGroupBox("다음 중 과일이 아닌 것은?", self)
        self.GroupBox.setGeometry(50, 20, 200, 100)

        # 라디오 버튼 설정
        self.radioBtn1 = QRadioButton("사과", self)
        self.radioBtn1.move(60, 40)
        self.radioBtn1.setChecked(True)
        self.radioBtn1.clicked.connect(self.radioBtn_Clicked)

        self.radioBtn2 = QRadioButton("딸기", self)
        self.radioBtn2.move(60, 60)
        self.radioBtn2.clicked.connect(self.radioBtn_Clicked)

        self.radioBtn3 = QRadioButton("곰", self)
        self.radioBtn3.move(60, 80)
        self.radioBtn3.clicked.connect(self.radioBtn_Clicked)

    def radioBtn_Clicked(self):
        msg = ""

        if self.radioBtn1.isChecked():
            msg = '사과'
        elif self.radioBtn2.isChecked():
            msg = "딸기"
        else:
            msg = '곰'
        QMessageBox.about(self, "선택된 항목", msg + " 선택됨")
        self.statusBar.showMessage(msg + " 선택됨")

##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()