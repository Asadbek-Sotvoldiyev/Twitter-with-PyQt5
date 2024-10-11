from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from login_page import LoginPage
from styles import btn_style


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 350)
        self.setGeometry(800, 300, 300, 350)

        self.label = QLabel("Login Oynasi", self)
        self.label.setStyleSheet("""
            font-size: 30px;
        
        """)

        self.label.adjustSize()
        self.label.move((self.width()-self.label.width())//2, 60)

        self.loginBtn = QPushButton("Login", self)
        self.loginBtn.adjustSize()
        self.loginBtn.resize(self.loginBtn.width() + 30, self.loginBtn.height() + 10)
        self.loginBtn.move((self.width() - self.loginBtn.width()) // 2, 150)
        self.loginBtn.setStyleSheet(btn_style)
        self.loginBtn.clicked.connect(self.loginBtnClicked)



        self.registerBtn = QPushButton("Register", self)
        self.registerBtn.adjustSize()
        self.registerBtn.resize(self.registerBtn.width() + 30, self.registerBtn.height() + 10)
        self.registerBtn.move((self.width() - self.registerBtn.width()) // 2, 200)
        self.registerBtn.setStyleSheet(btn_style)

    def loginBtnClicked(self):
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()



app = QApplication([])
window = MainPage()
window.show()
app.exec()


