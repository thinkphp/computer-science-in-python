import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox

class SimpleApp(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the layout
        layout = QVBoxLayout()

        # Create a button and add it to the layout
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.showMessage)
        layout.addWidget(self.button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set main window properties
        self.setWindowTitle('Simple PyQt App')
        self.setGeometry(100, 100, 300, 200)

    def showMessage(self):
        # Show a message box when the button is clicked
        QMessageBox.information(self, 'Message', 'Hello, PyQt!')

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create an instance of the application window and show it
    window = SimpleApp()
    window.show()

    # Execute the application's main loop
    sys.exit(app.exec_())
