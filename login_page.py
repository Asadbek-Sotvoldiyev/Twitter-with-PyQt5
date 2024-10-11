import json

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QMessageBox

from post_page import PostPage
from styles import btn_style


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300, 350)
        self.setGeometry(800, 300, 300, 350)

        self.username = QLineEdit(self)
        self.username.adjustSize()
        self.username.resize(self.username.width() + 30, self.username.height() + 10)
        self.username.move((self.width() - self.username.width()) // 2, 100)
        self.username.setPlaceholderText("Username")

        self.password = QLineEdit(self)
        self.password.adjustSize()
        self.password.resize(self.password.width() + 30, self.password.height() + 10)
        self.password.move((self.width() - self.password.width()) // 2, 150)
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.submit = QPushButton("Login", self)
        self.submit.adjustSize()
        self.submit.resize(self.submit.width() + 30, self.submit.height() + 10)
        self.submit.move((self.width() - self.submit.width()) // 2, 280)
        self.submit.setStyleSheet(btn_style)

        self.submit.clicked.connect(self.login)

    def login(self):
        username_input = self.username.text()
        password_input = self.password.text()

        with open("users.json", "r") as file:
            users = json.load(file)
        user_logged = False
        for user in users['users']:
            if user['username'] == username_input and user['password'] == password_input:
                self.post_page = PostPage(user)
                user_logged = True
                self.post_page.show()
                self.close()

        if not user_logged:
            QMessageBox.warning(self, "Warning", "Username yoki password xato")




