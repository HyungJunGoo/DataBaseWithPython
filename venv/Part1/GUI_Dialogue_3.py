import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0,0,300,300)
        self.setWindowTitle("메인 윈도우와 서브 윈도우의 상호작용 예제")

        self.pushButton = QPushButton("Sign In")
        self.pushButton.clicked.connect(self.pushButton_Clicked)
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def pushButton_Clicked(self):
        dialogue = LogInSubwindow() # Qdialog 클래스의 subwindow 객체 생성
        dialogue.exec_()

        id = dialogue.id
        password = dialogue.password
        self.label.setText("id: %s password: %s" % (id, password))

class LogInSubwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        # 입력을 저장할 변수 정의
        self.id = None
        self.password = None

    def setupUI(self):
        self.setWindowTitle("ID와 PW 입력")
        self.setGeometry(0, 100, 300, 100)

        # 위젯 설정
        self.label1 = QLabel("아이디: ")
        self.label2 = QLabel("암 호: ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.pushButton = QPushButton("로그인")
        self.pushButton.clicked.connect(self.pushButton_Clicked)

        # 레이아웃의 생성, 위젯 연결, 레이아웃 설정
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.pushButton, 0, 2)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        self.setLayout(layout)

    def pushButton_Clicked(self):
        self.id = self.lineEdit1.text()
        self.password = self.lineEdit2.text()
        self.close()


#######################################

if __name__ == "__main__":
    app =QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()