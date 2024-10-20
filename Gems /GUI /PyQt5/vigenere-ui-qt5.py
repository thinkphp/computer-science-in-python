import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton,
                           QRadioButton, QButtonGroup, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class VigenereCipher:
    @staticmethod
    def process_text(text, key, mode='encrypt'):
        result = ''
        key = key.upper()
        key_index = 0
        
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char_num = ord(char.upper()) - ord('A')
                key_char = key[key_index % len(key)]
                key_num = ord(key_char) - ord('A')
                
                if mode == 'encrypt':
                    new_num = (char_num + key_num) % 26
                else:
                    new_num = (char_num - key_num + 26) % 26
                
                new_char = chr(new_num + ord('A'))
                if not is_upper:
                    new_char = new_char.lower()
                
                key_index += 1
                result += new_char
            else:
                result += char
        
        return result

class VigenereCipherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set window properties
        self.setWindowTitle('Vigenère Cipher')
        self.setMinimumSize(600, 400)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 12px;
                font-weight: bold;
                color: #333;
            }
            QLineEdit, QTextEdit {
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
            QRadioButton {
                font-size: 12px;
                color: #333;
            }
        """)
        
        # Create input fields
        key_layout = QHBoxLayout()
        key_label = QLabel('Key:')
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText('Enter encryption/decryption key')
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)
        
        # Create radio buttons for mode selection
        mode_layout = QHBoxLayout()
        self.encrypt_radio = QRadioButton('Encrypt')
        self.decrypt_radio = QRadioButton('Decrypt')
        self.encrypt_radio.setChecked(True)
        mode_layout.addWidget(self.encrypt_radio)
        mode_layout.addWidget(self.decrypt_radio)
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
        
        # Create process button
        self.process_button = QPushButton('Process')
        self.process_button.clicked.connect(self.process_text)
        layout.addWidget(self.process_button)
        
        # Create clear button
        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.clear_fields)
        self.clear_button.setStyleSheet("""
            background-color: #f44336;
        """)
        layout.addWidget(self.clear_button)
        
    def process_text(self):
        key = self.key_input.text().strip()
        text = self.input_text.toPlainText()
        
        if not key:
            QMessageBox.warning(self, 'Error', 'Please enter a key!')
            return
        
        if not text:
            QMessageBox.warning(self, 'Error', 'Please enter text to process!')
            return
        
        if not any(c.isalpha() for c in key):
            QMessageBox.warning(self, 'Error', 'Key must contain at least one letter!')
            return
        
        mode = 'encrypt' if self.encrypt_radio.isChecked() else 'decrypt'
        result = VigenereCipher.process_text(text, key, mode)
        self.output_text.setText(result)
        
    def clear_fields(self):
        self.key_input.clear()
        self.input_text.clear()
        self.output_text.clear()
        self.encrypt_radio.setChecked(True)

def main():
    app = QApplication(sys.argv)
    gui = VigenereCipherGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
