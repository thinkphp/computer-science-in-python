import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoanCalculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Loan Calculator')
        self.setGeometry(300, 300, 300, 200)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label_loan_amount = QLabel('Loan Amount:')
        self.entry_loan_amount = QLineEdit()
        layout.addWidget(self.label_loan_amount)
        layout.addWidget(self.entry_loan_amount)

        self.label_interest_rate = QLabel('Interest Rate (%):')
        self.entry_interest_rate = QLineEdit()
        layout.addWidget(self.label_interest_rate)
        layout.addWidget(self.entry_interest_rate)

        self.label_loan_term = QLabel('Loan Term (years):')
        self.entry_loan_term = QLineEdit()
        layout.addWidget(self.label_loan_term)
        layout.addWidget(self.entry_loan_term)

        self.button_calculate = QPushButton('Calculate')
        self.button_calculate.clicked.connect(self.calculate_loan)
        layout.addWidget(self.button_calculate)

        self.label_result = QLabel('')
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def calculate_loan(self):
        try:
            loan_amount = float(self.entry_loan_amount.text())
            interest_rate = float(self.entry_interest_rate.text()) / 100 / 12
            loan_term = int(self.entry_loan_term.text()) * 12

            if interest_rate == 0:
                monthly_payment = loan_amount / loan_term
            else:
                monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate) ** -loan_term)

            self.label_result.setText(f'Monthly Payment: ${monthly_payment:.2f}')
        except ValueError:
            QMessageBox.critical(self, 'Input Error', 'Please enter valid numbers.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = LoanCalculator()
    calculator.show()
    sys.exit(app.exec_())
