import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QGridLayout

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Calculator')

        layout = QVBoxLayout()

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        buttons_layout = QGridLayout()

        buttons = [
            ('7', 0, 0),
            ('8', 0, 1),
            ('9', 0, 2),
            ('/', 0, 3),
            ('4', 1, 0),
            ('5', 1, 1),
            ('6', 1, 2),
            ('*', 1, 3),
            ('1', 2, 0),
            ('2', 2, 1),
            ('3', 2, 2),
            ('-', 2, 3),
            ('0', 3, 0),
            ('.', 3, 1),
            ('=', 3, 2),
            ('+', 3, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_clicked)
            buttons_layout.addWidget(button, row, col)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def button_clicked(self):
        button = self.sender()
        if button.text() == '=':
            self.calculate()
        else:
            self.input_field.setText(self.input_field.text() + button.text())

    def calculate(self):
        expression = self.input_field.text()
        try:
            result = eval(expression)
            self.result_label.setText(f'Result: {result}')
        except Exception as e:
            self.result_label.setText(f'Error: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleCalculator()
    window.show()
    sys.exit(app.exec_())

