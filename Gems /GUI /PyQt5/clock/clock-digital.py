from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
import sys
from datetime import datetime

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create main layout
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(20, 20, 20, 20)

        # Create time label
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setFont(QFont('Arial', 72, QFont.Bold))
        self.time_label.setStyleSheet("""
            QLabel {
                color: #00ff00;
                background-color: #000000;
                border: 2px solid #333333;
                border-radius: 10px;
                padding: 20px;
            }
        """)

        # Create date label
        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFont(QFont('Arial', 18))
        self.date_label.setStyleSheet("""
            QLabel {
                color: #888888;
                margin-top: 10px;
            }
        """)

        # Add labels to layout
        layout.addWidget(self.time_label)
        layout.addWidget(self.date_label)

        # Set the layout
        self.setLayout(layout)

        # Set up timer for updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # Update every second

        # Initial update
        self.updateTime()

        # Set window style
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
            }
        """)

        # Set minimum size
        self.setMinimumSize(500, 200)

    def updateTime(self):
        current = datetime.now()

        # Update time with blinking colon
        time_text = current.strftime("%H:%M:%S")
        self.time_label.setText(time_text)

        # Update date
        date_text = current.strftime("%A, %B %d, %Y")
        self.date_label.setText(date_text)

    def toggleColon(self):
        # Get current text
        current_text = self.time_label.text()
        if ':' in current_text:
            # Replace colons with spaces
            new_text = current_text.replace(':', ' ')
        else:
            # Replace spaces with colons
            new_text = f"{current_text[:2]}:{current_text[3:5]}:{current_text[6:]}"
        self.time_label.setText(new_text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setCentralWidget(DigitalClock())
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a1a;
            }
        """)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
