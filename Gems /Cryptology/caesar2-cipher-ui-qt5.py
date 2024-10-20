import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QLabel, QSpinBox, QTextEdit, QPushButton,
                           QRadioButton, QMessageBox)
from PyQt5.QtCore import Qt

class CaesarCipher:
    @staticmethod
    def process_text(text, shift, mode='encrypt'):
        result = ''
        # Adjust shift for decryption
        if mode == 'decrypt':
            shift = -shift

        for char in text:
            if char.isalpha():
                # Preserve case
                is_upper = char.isupper()
                # Convert to 0-25 range
                char_num = ord(char.upper()) - ord('A')
                # Apply shift
                new_num = (char_num + shift) % 26
                # Convert back to character
                new_char = chr(new_num + ord('A'))
                # Restore original case
                if not is_upper:
                    new_char = new_char.lower()
                result += new_char
            else:
                # Preserve non-alphabetic characters
                result += char

        return result

class CaesarCipherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Caesar Cipher')
        self.setMinimumSize(600, 400)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 12px;
                font-weight: bold;
                color: #333;
            }
            QSpinBox {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
                min-width: 80px;
            }
            QTextEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
            }
            QPushButton {
                padding: 8px 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton#clearButton {
                background-color: #f44336;
            }
            QPushButton#clearButton:hover {
                background-color: #da190b;
            }
            QRadioButton {
                font-size: 12px;
                color: #333;
                margin: 5px;
            }
        """)

        # Create shift input
        shift_layout = QHBoxLayout()
        shift_label = QLabel('Shift Value (1-25):')
        self.shift_input = QSpinBox()
        self.shift_input.setRange(1, 25)
        self.shift_input.setValue(3)  # Default Caesar shift
        shift_layout.addWidget(shift_label)
        shift_layout.addWidget(self.shift_input)
        shift_layout.addStretch()
        layout.addLayout(shift_layout)

        # Create mode selection
        mode_layout = QHBoxLayout()
        self.encrypt_radio = QRadioButton('Encrypt')
        self.decrypt_radio = QRadioButton('Decrypt')
        self.encrypt_radio.setChecked(True)
        mode_layout.addWidget(self.encrypt_radio)
        mode_layout.addWidget(self.decrypt_radio)
        mode_layout.addStretch()
        layout.addLayout(mode_layout)

        # Create text areas
        input_label = QLabel('Input Text:')
        layout.addWidget(input_label)
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText('Enter text to encrypt/decrypt')
        layout.addWidget(self.input_text)

        output_label = QLabel('Output Text:')
        layout.addWidget(output_label)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Create buttons layout
        button_layout = QHBoxLayout()

        # Process button
        self.process_button = QPushButton('Process')
        self.process_button.clicked.connect(self.process_text)
        button_layout.addWidget(self.process_button)

        # Create brute force button
        self.brute_force_button = QPushButton('Show All Shifts')
        self.brute_force_button.clicked.connect(self.show_all_shifts)
        self.brute_force_button.setStyleSheet("""
            background-color: #2196F3;
        """)
        button_layout.addWidget(self.brute_force_button)

        # Clear button
        self.clear_button = QPushButton('Clear')
        self.clear_button.setObjectName('clearButton')
        self.clear_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)

    def process_text(self):
        text = self.input_text.toPlainText()
        shift = self.shift_input.value()

        if not text:
            QMessageBox.warning(self, 'Error', 'Please enter text to process!')
            return

        mode = 'encrypt' if self.encrypt_radio.isChecked() else 'decrypt'
        result = CaesarCipher.process_text(text, shift, mode)
        self.output_text.setText(result)

    def show_all_shifts(self):
        text = self.input_text.toPlainText()

        if not text:
            QMessageBox.warning(self, 'Error', 'Please enter text to process!')
            return

        all_shifts = "All possible shifts (1-25):\n\n"
        for shift in range(1, 26):
            result = CaesarCipher.process_text(text, shift, 'decrypt')
            all_shifts += f"Shift {shift}: {result}\n"

        self.output_text.setText(all_shifts)

    def clear_fields(self):
        self.shift_input.setValue(3)
        self.input_text.clear()
        self.output_text.clear()
        self.encrypt_radio.setChecked(True)

def main():
    app = QApplication(sys.argv)
    gui = CaesarCipherGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
