import sys
from function import Hash
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QLabel, QPlainTextEdit, QLineEdit)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.hash = Hash()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyGenHash')
        self.setFixedWidth(350)
        self.setWindowIcon(QIcon('hashtag.svg'))
        self.setLayout(QVBoxLayout())

        font = QFont('Russo Sans Bold', 25)
        if not font.exactMatch():
            font_db = QFontDatabase()
            font_db.addApplicationFont("fonts/Russo Sans Bold.otf")
            font = QFont('Russo Sans Bold', 25)

        self.heading = QLabel('PyGenHash')
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setFont(font)

        hash_md5 = 'MD5 Hash'
        hash_sha1 = 'SHA1 Hash'
        hash_sha256 = 'SHA256 Hash'
        hash_sha512 = 'SHA512 Hash'

        inputString = QPlainTextEdit()
        inputString.setMaximumHeight(100)
        self.space = QLabel()
        self.qle_md5 = QLineEdit()
        self.qle_sha1 = QLineEdit()
        self.qle_sha256 = QLineEdit()
        self.qle_sha512 = QLineEdit()

        inputString.setPlaceholderText('Enter String to Generate Hashes')
        self.qle_md5.setPlaceholderText(hash_md5)
        self.qle_sha1.setPlaceholderText(hash_sha1)
        self.qle_sha256.setPlaceholderText(hash_sha256)
        self.qle_sha512.setPlaceholderText(hash_sha512)

        self.qle_md5.setReadOnly(True)
        self.qle_sha1.setReadOnly(True)
        self.qle_sha256.setReadOnly(True)
        self.qle_sha512.setReadOnly(True)

        self.layout().addWidget(self.heading)
        self.layout().addWidget(inputString)
        self.layout().addWidget(self.space)
        self.layout().addWidget(self.qle_md5)
        self.layout().addWidget(self.qle_sha1)
        self.layout().addWidget(self.qle_sha256)
        self.layout().addWidget(self.qle_sha512)

        inputString.textChanged.connect(
            lambda: self.genHash(inputString.toPlainText()))

        self.show()

    def genHash(self, string):
        if string == '':
            self.qle_md5.clear()
            self.qle_sha1.clear()
            self.qle_sha256.clear()
            self.qle_sha512.clear()
        else:
            self.qle_md5.setText(self.hash.md5(string))
            self.qle_sha1.setText(self.hash.sha1(string))
            self.qle_sha256.setText(self.hash.sha256(string))
            self.qle_sha512.setText(self.hash.sha512(string))


def main():

    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
