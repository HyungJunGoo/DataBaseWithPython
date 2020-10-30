import sys
from  PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 툴팁 설정
        QToolTip.setFont(QFont("SansSerif", 12))

        # 윈도우 설정
        self.setWindowTitle("윈도우 생성 예제")
        self.move(0, 0)
        self.resize(400, 300)

        # 버튼 설정
        self.pushButton = QPushButton("ToolTip 버튼", self)
        self.pushButton.move(50, 50)
        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton.setToolTip("버튼 툴팁")
        self.pushButton.clicked.connect(self.pushButton_Clicked) #button 객체의 "clicked" 시그널에 대해 pushButton_Clicked 라는 슬롯을 연결

    def pushButton_Clicked(self):
        QMessageBox.about(self, "메세지 박스", "Push Button Clicked")
        print("Push Button Clicked")

##########################################

if __name__ == "__main__":      # GUI_Widget_1.py 가 실행될 때 __main__ (True), import될 때는 모듈명(False)
    app = QApplication(sys.argv) # event loop 생성을 위해 QApplication 객체를 생성함.
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_() # 윈도우의 event loop에 들어감