import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QPushButton, QLabel, QLineEdit,
                            QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class NumberGuessingGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Guessing Game")
        self.setMinimumSize(400, 500)

        # Initialize game variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10
        self.previous_guesses = []
        self.game_active = True

        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Create and style title label
        title_label = QLabel("Number Guessing Game")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Instructions label
        instructions = QLabel("I'm thinking of a number between 1 and 100.\nCan you guess it?")
        instructions.setFont(QFont("Arial", 12))
        instructions.setAlignment(Qt.AlignCenter)
        layout.addWidget(instructions)

        # Create input field and button
        input_layout = QHBoxLayout()
        self.guess_input = QLineEdit()
        self.guess_input.setPlaceholderText("Enter your guess")
        self.guess_input.setFont(QFont("Arial", 12))
        self.guess_input.returnPressed.connect(self.make_guess)
        input_layout.addWidget(self.guess_input)

        self.guess_button = QPushButton("Guess")
        self.guess_button.setFont(QFont("Arial", 12))
        self.guess_button.clicked.connect(self.make_guess)
        input_layout.addWidget(self.guess_button)
        layout.addLayout(input_layout)

        # Feedback labels
        self.feedback_label = QLabel("")
        self.feedback_label.setFont(QFont("Arial", 12))
        self.feedback_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.feedback_label)

        self.attempts_label = QLabel(f"Attempts: 0/{self.max_attempts}")
        self.attempts_label.setFont(QFont("Arial", 12))
        self.attempts_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.attempts_label)

        self.previous_guesses_label = QLabel("Previous guesses: ")
        self.previous_guesses_label.setFont(QFont("Arial", 12))
        self.previous_guesses_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.previous_guesses_label)

        # New Game button
        self.new_game_button = QPushButton("New Game")
        self.new_game_button.setFont(QFont("Arial", 12))
        self.new_game_button.clicked.connect(self.start_new_game)
        layout.addWidget(self.new_game_button)

        # Style the window
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
        """)

    def make_guess(self):
        if not self.game_active:
            return

        # Get and validate input
        try:
            guess = int(self.guess_input.text())
            if guess < 1 or guess > 100:
                QMessageBox.warning(self, "Invalid Input", "Please enter a number between 1 and 100.")
                return
            if guess in self.previous_guesses:
                QMessageBox.warning(self, "Duplicate Guess", "You already tried that number!")
                return
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            return

        # Process the guess
        self.attempts += 1
        self.previous_guesses.append(guess)

        # Update feedback
        if guess == self.secret_number:
            self.feedback_label.setText(f"Congratulations! You've won in {self.attempts} attempts!")
            self.feedback_label.setStyleSheet("color: green; font-weight: bold;")
            self.game_active = False
        elif guess < self.secret_number:
            self.feedback_label.setText("Too low!")
            self.feedback_label.setStyleSheet("color: orange;")
        else:
            self.feedback_label.setText("Too high!")
            self.feedback_label.setStyleSheet("color: red;")

        # Update labels
        self.attempts_label.setText(f"Attempts: {self.attempts}/{self.max_attempts}")
        self.previous_guesses_label.setText(f"Previous guesses: {sorted(self.previous_guesses)}")

        # Clear input
        self.guess_input.clear()

        # Check for game over
        if self.attempts >= self.max_attempts and guess != self.secret_number:
            self.feedback_label.setText(f"Game Over! The number was {self.secret_number}")
            self.feedback_label.setStyleSheet("color: red; font-weight: bold;")
            self.game_active = False

    def start_new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.previous_guesses = []
        self.game_active = True

        # Reset labels
        self.feedback_label.setText("")
        self.feedback_label.setStyleSheet("")
        self.attempts_label.setText(f"Attempts: 0/{self.max_attempts}")
        self.previous_guesses_label.setText("Previous guesses: ")
        self.guess_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumberGuessingGame()
    window.show()
    sys.exit(app.exec_())  # Note: in Qt5 it's exec_() not exec()
