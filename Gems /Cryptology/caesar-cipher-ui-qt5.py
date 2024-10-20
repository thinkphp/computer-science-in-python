import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QSpinBox

class CaesarCipherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.input_label = QLabel("Enter text:")
        self.input_text = QLineEdit()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)

        self.shift_label = QLabel("Shift value:")
        self.shift_spinbox = QSpinBox()
        self.shift_spinbox.setRange(0, 25)
        layout.addWidget(self.shift_label)
        layout.addWidget(self.shift_spinbox)

        self.radio_layout = QHBoxLayout()
        self.encrypt_radio = QRadioButton("Encrypt")
        self.decrypt_radio = QRadioButton("Decrypt")
        self.encrypt_radio.setChecked(True)
        self.radio_layout.addWidget(self.encrypt_radio)
        self.radio_layout.addWidget(self.decrypt_radio)
        layout.addLayout(self.radio_layout)

        self.process_button = QPushButton("Process")
        self.process_button.clicked.connect(self.process_text)
        layout.addWidget(self.process_button)

        self.result_label = QLabel("Result:")
        self.result_text = QLineEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

        self.setLayout(layout)
        self.setWindowTitle('Caesar Cipher')
        self.show()

    def process_text(self):
        text = self.input_text.text()
        shift = self.shift_spinbox.value()
        if self.encrypt_radio.isChecked():
            result = self.caesar_encrypt(text, shift)
        else:
            result = self.caesar_decrypt(text, shift)
        self.result_text.setText(result)

    def caesar_encrypt(self, text, shift):
        return ''.join([chr((ord(char) - 97 + shift) % 26 + 97) if char.isalpha() else char for char in text.lower()])

    def caesar_decrypt(self, text, shift):
        return ''.join([chr((ord(char) - 97 - shift) % 26 + 97) if char.isalpha() else char for char in text.lower()])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CaesarCipherApp()
    sys.exit(app.exec_())
