import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class FactorialCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the window properties
        self.setWindowTitle('Factorial Calculator')

        # Create layout
        layout = QVBoxLayout()

        # Create and add widgets to the layout
        self.label = QLabel('Enter a number:')
        layout.addWidget(self.label)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate_factorial)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        # Set the layout for the main window
        self.setLayout(layout)

    def calculate_factorial(self):
        try:
            number = int(self.entry.text())
            if number < 0:
                self.result_label.setText("Please enter a non-negative integer")
                return
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            self.result_label.setText(f"The factorial of {number} is {factorial}")
        except ValueError:
            self.result_label.setText("Please enter a valid integer")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FactorialCalculator()
    window.show()

    sys.exit(app.exec_())
