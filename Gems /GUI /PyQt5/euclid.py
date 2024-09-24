import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class EuclidCalculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Euclid GCD Calculator')
        self.setGeometry(300, 300, 300, 150)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Input fields for the two numbers
        self.label_num1 = QLabel('Enter First Number:')
        self.entry_num1 = QLineEdit()
        layout.addWidget(self.label_num1)
        layout.addWidget(self.entry_num1)

        self.label_num2 = QLabel('Enter Second Number:')
        self.entry_num2 = QLineEdit()
        layout.addWidget(self.label_num2)
        layout.addWidget(self.entry_num2)

        # Button to trigger calculation
        self.button_calculate = QPushButton('Calculate GCD')
        self.button_calculate.clicked.connect(self.calculate_gcd)
        layout.addWidget(self.button_calculate)

        # Label to show the result
        self.label_result = QLabel('')
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def calculate_gcd(self):
        try:
            # Get input values
            num1 = int(self.entry_num1.text())
            num2 = int(self.entry_num2.text())

            # Calculate GCD using Euclid's algorithm
            gcd_result = self.euclid_gcd(num1, num2)

            # Display result
            self.label_result.setText(f'GCD: {gcd_result}')
        except ValueError:
            QMessageBox.critical(self, 'Input Error', 'Please enter valid integers.')

    def euclid_gcd(self, a, b):
        # Euclid's algorithm to compute GCD
        while b:
            a, b = b, a % b
        return a

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = EuclidCalculator()
    calculator.show()
    sys.exit(app.exec_())
