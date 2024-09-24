import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

class FibonacciSequenceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Fibonacci Sequence")

        layout = QVBoxLayout()

        self.label = QLabel("Enter the number of terms:")
        layout.addWidget(self.label)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.button = QPushButton("Generate")
        self.button.clicked.connect(self.display_fibonacci_sequence)
        layout.addWidget(self.button)

        self.sequence_label = QLabel("")
        layout.addWidget(self.sequence_label)

        self.setLayout(layout)

    def display_fibonacci_sequence(self):
        try:
            n = int(self.entry.text())
            fibonacci_sequence = generate_fibonacci_sequence(n)
            self.sequence_label.setText("Fibonacci Sequence: " + ", ".join(map(str, fibonacci_sequence)))
        except ValueError:
            self.sequence_label.setText("Please enter a valid number.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FibonacciSequenceApp()
    window.show()
    sys.exit(app.exec_())
