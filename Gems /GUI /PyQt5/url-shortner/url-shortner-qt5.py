import sys
import re
import pyshorteners
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt

class URLShortener(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle("URL Shortener")
        self.setFixedSize(400, 400)

        # Set background color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("#4a536b"))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Main layout
        main_layout = QVBoxLayout()

        # Background image (if you have the image file)
        background_label = QLabel(self)
        pixmap = QPixmap('bg3.png')
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)
        main_layout.addWidget(background_label)

        # URL Input Section
        url_label = QLabel("Enter URL Here")
        url_label.setStyleSheet("color: #EAECEE; font: bold 13pt Poppins;")
        main_layout.addWidget(url_label)

        self.url_input = QLineEdit()
        self.url_input.setStyleSheet("font: 12pt Poppins;")
        main_layout.addWidget(self.url_input)

        # Shorten Button
        shorten_btn = QPushButton("Shorten URL")
        shorten_btn.setStyleSheet("""
            background-color: #F8C471;
            color: #1e1e1e;
            font: bold 11pt Poppins;
        """)
        shorten_btn.clicked.connect(self.convert)
        main_layout.addWidget(shorten_btn)

        # Shortened URL Section
        short_url_label = QLabel("Shortened URL")
        short_url_label.setStyleSheet("color: white; font: bold 13pt Poppins;")
        main_layout.addWidget(short_url_label)

        self.short_url_input = QLineEdit()
        self.short_url_input.setStyleSheet("font: 12pt Poppins;")
        self.short_url_input.setReadOnly(True)
        main_layout.addWidget(self.short_url_input)

        # Clipboard Label
        self.clipboard_label = QLabel()
        self.clipboard_label.setStyleSheet("""
            background-color: #49f6b3;
            color: #1e1e1e;
            font: 9pt Poppins;
            padding: 5px;
        """)
        main_layout.addWidget(self.clipboard_label)

        self.setLayout(main_layout)

    def is_valid_url(self, url):
        if not url:
            return False
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def convert(self):
        url_text = self.url_input.text().strip()

        # Validate URL
        if not self.is_valid_url(url_text):
            QMessageBox.critical(self, "Invalid URL", "Please enter a valid URL.")
            return

        try:
            # Shorten URL
            s = pyshorteners.Shortener().tinyurl.short(url_text)

            # Set shortened URL
            self.short_url_input.setText(s)

            # Copy to clipboard
            clipboard = QApplication.clipboard()
            clipboard.setText(s)

            # Show clipboard notification
            self.clipboard_label.setText("Shortened URL is copied to clipboard")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

def main():
    app = QApplication(sys.argv)
    shortener = URLShortener()
    shortener.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
