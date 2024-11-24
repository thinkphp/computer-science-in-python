import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt  # Import Qt for alignment



def descompune_in_factori_primi(n):
    factori = []
    divisor = 2

    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factori.append((divisor, count))
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factori.append((n, 1))
            break

    return factori


class PrimeFactorizationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prime Factorization")
        self.setGeometry(200, 200, 400, 300)

        # Main layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Title label
        self.title_label = QLabel("Prime Factorization Tool", self)
        self.title_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.title_label.setStyleSheet("color: #4CAF50;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Input field
        self.input_label = QLabel("Enter a number:", self)
        self.input_label.setFont(QFont("Arial", 12))
        self.layout.addWidget(self.input_label)

        self.input_field = QLineEdit(self)
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setPlaceholderText("Enter a positive integer")
        self.input_field.returnPressed.connect(self.factorize_number)  # Trigger on Enter key
        self.layout.addWidget(self.input_field)

        # Submit button
        self.submit_button = QPushButton("Factorize", self)
        self.submit_button.setFont(QFont("Arial", 12))
        self.submit_button.setStyleSheet("background-color: #2196F3; color: white;")
        self.submit_button.clicked.connect(self.factorize_number)
        self.layout.addWidget(self.submit_button)

        # Result label
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setWordWrap(True)
        self.layout.addWidget(self.result_label)

    def factorize_number(self):
        try:
            number = int(self.input_field.text())
            if number <= 1:
                self.result_label.setText("Please enter a number greater than 1.")
                self.result_label.setStyleSheet("color: red;")
                return

            factors = descompune_in_factori_primi(number)
            result = " * ".join(f"{base}^{exponent}" for base, exponent in factors)
            self.result_label.setText(f"Prime Factorization: {result}")
            self.result_label.setStyleSheet("color: black;")
        except ValueError:
            self.result_label.setText("Invalid input. Please enter a valid integer.")
            self.result_label.setStyleSheet("color: red;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrimeFactorizationApp()
    window.show()
    sys.exit(app.exec_())
