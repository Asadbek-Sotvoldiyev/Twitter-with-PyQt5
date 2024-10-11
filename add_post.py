import json
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit
from styles import btn_style


class AddPostPage(QWidget):
    def __init__(self, user, parent):
        super().__init__()
        self.user = user
        self.parent = parent

        self.setFixedSize(400, 350)
        self.setGeometry(800, 300, 400, 350)

        self.textarea = QTextEdit(self)
        self.textarea.adjustSize()
        self.textarea.resize(self.textarea.width() + 100, self.textarea.height() + 20)
        self.textarea.move((self.width() - self.textarea.width()) // 2, 30)
        self.textarea.setPlaceholderText("Post yozing...")

        self.post = QPushButton("Post", self)
        self.post.adjustSize()
        self.post.resize(self.post.width() + 100, self.post.height() + 10)
        self.post.move((self.width() - self.post.width()) // 2, 280)
        self.post.setStyleSheet(btn_style)

        self.post.clicked.connect(self.post_bosildi)

    def post_bosildi(self):
        posts = {}
        with open("posts.json", "r") as file:
            posts = json.load(file)

        username = self.user['username']
        text = self.textarea.toPlainText()

        post_dict = {
                      "username": username,
                      "post": text
                    }

        posts['posts'].append(post_dict)

        with open("posts.json", "w") as file_write:
            json.dump(posts, file_write)

        self.parent.show()
        self.parent.load_posts()
        self.close()








