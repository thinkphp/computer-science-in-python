import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton,
                           QRadioButton, QMessageBox, QGridLayout)
from PyQt5.QtCore import Qt

class SubstitutionCipher:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.substitution_key = None

    def generate_random_key(self):
        """Generează o cheie aleatoare de substituție"""
        chars = list(self.alphabet)
        random.shuffle(chars)
        return ''.join(chars)

    def validate_key(self, key):
        """Verifică dacă cheia de substituție este validă"""
        key = key.upper()
        if len(key) != 26:
            return False
        if sorted(key) != sorted(self.alphabet):
            return False
        return True

    def process_text(self, text, key, mode='encrypt'):
        """Procesează textul folosind cifrul de substituție"""
        if mode == 'encrypt':
            trans = str.maketrans(self.alphabet, key)
        else:
            trans = str.maketrans(key, self.alphabet)

        result = ''
        for char in text:
            if char.isalpha():
                # Păstrează cazul (uppercase/lowercase)
                is_upper = char.isupper()
                processed_char = char.upper().translate(trans)
                result += processed_char if is_upper else processed_char.lower()
            else:
                result += char
        return result

class SubstitutionCipherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cipher = SubstitutionCipher()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cifru de Substituție')
        self.setMinimumSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Stilizare
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 12px;
                font-weight: bold;
                color: #333;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
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
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton#generateButton {
                background-color: #2196F3;
            }
            QPushButton#generateButton:hover {
                background-color: #1976D2;
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
            .keyDisplay {
                font-family: monospace;
                font-size: 14px;
            }
        """)

        # Secțiunea pentru cheie
        key_section = QVBoxLayout()

        # Afișare alfabet original
        alphabet_layout = QHBoxLayout()
        alphabet_label = QLabel('Alfabet:')
        self.alphabet_display = QLineEdit(self.cipher.alphabet)
        self.alphabet_display.setReadOnly(True)
        alphabet_layout.addWidget(alphabet_label)
        alphabet_layout.addWidget(self.alphabet_display)
        key_section.addLayout(alphabet_layout)

        # Input pentru cheia de substituție
        key_layout = QHBoxLayout()
        key_label = QLabel('Cheie de substituție:')
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText('Introduceți cheia de substituție sau generați una aleatoare')
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.key_input)
        key_section.addLayout(key_layout)

        # Butoane pentru cheie
        key_buttons = QHBoxLayout()
        self.generate_key_button = QPushButton('Generează Cheie')
        self.generate_key_button.setObjectName('generateButton')
        self.generate_key_button.clicked.connect(self.generate_key)
        key_buttons.addWidget(self.generate_key_button)
        key_section.addLayout(key_buttons)

        layout.addLayout(key_section)

        # Mod de operare (Criptare/Decriptare)
        mode_layout = QHBoxLayout()
        self.encrypt_radio = QRadioButton('Criptare')
        self.decrypt_radio = QRadioButton('Decriptare')
        self.encrypt_radio.setChecked(True)
        mode_layout.addWidget(self.encrypt_radio)
        mode_layout.addWidget(self.decrypt_radio)
        layout.addLayout(mode_layout)

        # Zone text
        input_label = QLabel('Text de intrare:')
        layout.addWidget(input_label)
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText('Introduceți textul pentru criptare/decriptare')
        layout.addWidget(self.input_text)

        output_label = QLabel('Text procesat:')
        layout.addWidget(output_label)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Butoane principale
        button_layout = QHBoxLayout()

        self.process_button = QPushButton('Procesează')
        self.process_button.clicked.connect(self.process_text)
        button_layout.addWidget(self.process_button)

        self.clear_button = QPushButton('Șterge Tot')
        self.clear_button.setObjectName('clearButton')
        self.clear_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.clear_button)

        layout.addLayout(button_layout)

    def generate_key(self):
        """Generează și afișează o cheie aleatoare"""
        key = self.cipher.generate_random_key()
        self.key_input.setText(key)

    def process_text(self):
        """Procesează textul conform modului selectat"""
        key = self.key_input.text().upper()
        text = self.input_text.toPlainText()

        if not text:
            QMessageBox.warning(self, 'Eroare', 'Introduceți text pentru procesare!')
            return

        if not key:
            QMessageBox.warning(self, 'Eroare', 'Introduceți sau generați o cheie de substituție!')
            return

        if not self.cipher.validate_key(key):
            QMessageBox.warning(self, 'Eroare',
                              'Cheia de substituție trebuie să conțină exact o dată fiecare literă din alfabet!')
            return

        mode = 'encrypt' if self.encrypt_radio.isChecked() else 'decrypt'
        result = self.cipher.process_text(text, key, mode)
        self.output_text.setText(result)

    def clear_fields(self):
        """Șterge toate câmpurile"""
        self.key_input.clear()
        self.input_text.clear()
        self.output_text.clear()
        self.encrypt_radio.setChecked(True)

def main():
    app = QApplication(sys.argv)
    gui = SubstitutionCipherGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
