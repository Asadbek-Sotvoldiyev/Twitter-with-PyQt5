import json

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QScrollBar, QScrollArea

from add_post import AddPostPage
from styles import btn_style, post_style


class PostPage(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user

        self.setFixedSize(400, 450)
        self.setGeometry(800, 300, 400, 450)

        self.vertical = QVBoxLayout()


        self.add_post = QPushButton("Add Post", self)
        self.add_post.adjustSize()
        self.add_post.resize(self.add_post.width() + 30, self.add_post.height() + 10)
        self.add_post.setStyleSheet(btn_style)
        self.add_post.clicked.connect(self.add_new_post)


        self.my_posts = QPushButton("My Posts", self)
        self.my_posts.adjustSize()
        self.my_posts.resize(self.my_posts.width() + 30, self.my_posts.height() + 10)
        self.my_posts.setStyleSheet(btn_style)

        horizontal = QHBoxLayout()
        horizontal.addWidget(self.add_post)
        horizontal.addWidget(self.my_posts)

        self.vertical.addLayout(horizontal)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)

        self.load_posts()

        scroll_content.setLayout(self.scroll_layout)
        scroll.setWidget(scroll_content)

        self.vertical.addWidget(scroll)

        self.setLayout(self.vertical)

    def add_new_post(self):
        self.add_post_page = AddPostPage(self.user, self)
        self.add_post_page.show()
        self.close()

    def load_posts(self):
        with open("posts.json", "r") as file:
            posts = json.load(file)

        for post in posts['posts'][::-1]:
            text = f"Username: {post['username']}\nPost: {post['post']}\n\n"
            label = QLabel(text)
            label.setStyleSheet(post_style)
            self.scroll_layout.addWidget(label)


