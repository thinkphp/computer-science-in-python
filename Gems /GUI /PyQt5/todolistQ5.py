import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                           QHBoxLayout, QPushButton, QListWidget, QLineEdit,
                           QMessageBox, QInputDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f'Task "{task}" has been added successfully'

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return 'Task deleted!'
        return "Invalid index!"

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            return 'Task updated successfully!'
        return "Invalid index!"

    def list_tasks(self):
        return self.tasks

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.todo_list = TodoList()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle('Todo List Application')
        self.setGeometry(100, 100, 800, 600)  # Increased window size

        # Set up fonts
        button_font = QFont('Arial', 12, QFont.Bold)
        input_font = QFont('Arial', 12)
        list_font = QFont('Arial', 12)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)  # Increase spacing between elements

        # Create input field and add button
        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setFont(input_font)
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_input.setMinimumHeight(50)  # Make input field taller

        add_button = QPushButton('Add Task')
        add_button.setFont(button_font)
        add_button.setMinimumHeight(50)  # Make button taller
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_button)

        # Create list widget
        self.list_widget = QListWidget()
        self.list_widget.setFont(list_font)
        self.list_widget.setStyleSheet("""
            QListWidget {
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
            }
            QListWidget::item:selected {
                background-color: #e0e0e0;
                color: black;
            }
        """)

        # Create buttons
        button_layout = QHBoxLayout()
        delete_button = QPushButton('Delete Task')
        update_button = QPushButton('Update Task')

        # Style the action buttons
        for button in (delete_button, update_button):
            button.setFont(button_font)
            button.setMinimumHeight(50)
            button.setMinimumWidth(200)  # Make buttons wider

        delete_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)

        update_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)

        delete_button.clicked.connect(self.delete_task)
        update_button.clicked.connect(self.update_task)

        button_layout.addWidget(delete_button)
        button_layout.addWidget(update_button)
        button_layout.setSpacing(20)  # Add space between buttons

        # Add widgets to main layout
        layout.addLayout(input_layout)
        layout.addWidget(self.list_widget)
        layout.addLayout(button_layout)

        # Set margins for the main layout
        layout.setContentsMargins(20, 20, 20, 20)

        # Set up keyboard shortcuts
        self.task_input.returnPressed.connect(self.add_task)

        self.refresh_list()

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            message = self.todo_list.add_task(task)
            self.task_input.clear()
            self.refresh_list()
            self.show_message("Success", message)

    def delete_task(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            message = self.todo_list.delete_task(current_row)
            self.refresh_list()
            self.show_message("Success", message)
        else:
            self.show_message("Error", "Please select a task to delete!")

    def update_task(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            current_text = self.list_widget.currentItem().text()
            dialog = QInputDialog(self)
            dialog.setInputMode(QInputDialog.TextInput)
            dialog.setWindowTitle('Update Task')
            dialog.setLabelText('Enter new task description:')
            dialog.setTextValue(current_text)
            dialog.resize(500, 200)  # Make dialog bigger

            # Set font for input dialog
            dialog_font = QFont('Arial', 12)
            dialog.setFont(dialog_font)

            ok = dialog.exec_()
            new_task = dialog.textValue()

            if ok and new_task.strip():
                message = self.todo_list.update_task(current_row, new_task)
                self.refresh_list()
                self.show_message("Success", message)
        else:
            self.show_message("Error", "Please select a task to update!")

    def refresh_list(self):
        self.list_widget.clear()
        for task in self.todo_list.list_tasks():
            self.list_widget.addItem(task)

    def show_message(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setFont(QFont('Arial', 12))
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QPushButton {
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                min-width: 100px;
                min-height: 40px;
            }
        """)
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    todo_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
