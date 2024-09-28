# PyQt5
```
pip install PyQt5
```


# Introduction to PyQt5 GUI App Development

PyQt5 is a comprehensive set of Python bindings for Qt v5. It allows you to create desktop applications with a native look and feel on various platforms. Let's look at three examples to get started.

## Course Outline

1. Introduction to PyQt5
   - What is PyQt5?
   - Setting up the development environment
   - Creating your first PyQt5 application

2. PyQt5 Widgets
   - Basic widgets (QLabel, QPushButton, QLineEdit)
   - Advanced widgets (QListWidget, QCheckBox, QRadioButton)
   - Container widgets (QWidget, QGroupBox)

3. Layout Management
   - QHBoxLayout and QVBoxLayout
   - QGridLayout
   - QFormLayout

4. Signals and Slots
   - Understanding the signal-slot mechanism
   - Connecting built-in signals and slots
   - Creating custom signals

5. Dialogs and Windows
   - Creating custom dialog windows
   - Using built-in dialogs (QMessageBox, QFileDialog)
   - Main window and MDI applications

6. Styling and Themes
   - Using Qt Style Sheets
   - Working with QSS (Qt Style Sheets)
   - Creating custom styles

7. Advanced Topics
   - QGraphicsView framework for 2D graphics
   - Working with multimedia (QMediaPlayer)
   - Database integration with QtSql

8. Best Practices and Project
   - Code organization with PyQt5
   - Error handling and debugging
   - Final project: Building a complete PyQt5 application

#### Example 1. This example creates a window with a centered "Hello, World!" label.
```
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt

class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        label = QLabel('Hello, World!', self)
        label.setAlignment(Qt.AlignCenter)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Hello, World!')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hw = HelloWorld()
    sys.exit(app.exec_())
```

#### Example 2. This example demonstrates how to create a button and handle a click event

```
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class ButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        button = QPushButton('Click me!', self)
        button.clicked.connect(self.on_click)
        layout.addWidget(button)
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Button Example')
        self.show()
        
    def on_click(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonExample()
    sys.exit(app.exec_())
```

#### Example 3 This example shows how to use a QLineEdit widget to get user input and display the result.

```
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel

class LineEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.label = QLabel('Enter your name:')
        layout.addWidget(self.label)
        
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)
        
        self.button = QPushButton('Submit')
        self.button.clicked.connect(self.on_submit)
        layout.addWidget(self.button)
        
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Line Edit Example')
        self.show()
        
    def on_submit(self):
        name = self.line_edit.text()
        self.result_label.setText(f'Hello, {name}!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LineEditExample()
    sys.exit(app.exec_())
```

#### Example 4. Advanced Widgets. This example shows the usage of QListWidget, QCheckBox, and QRadioButton widget

```
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QCheckBox, QRadioButton, QVBoxLayout

class AdvancedWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # QListWidget
        list_widget = QListWidget()
        list_widget.addItems(['Python', 'Java', 'C++'])
        layout.addWidget(list_widget)
        
        # QCheckBox
        checkbox = QCheckBox('Check me')
        layout.addWidget(checkbox)
        
        # QRadioButton
        radio1 = QRadioButton('Option 1')
        radio2 = QRadioButton('Option 2')
        layout.addWidget(radio1)
        layout.addWidget(radio2)
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Advanced Widgets')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdvancedWidgets()
    sys.exit(app.exec_())
```

#### Example 5. Container Widgets

```
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout

class ContainerWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        main_layout = QHBoxLayout()
        
        # QWidget as a container
        widget_container = QWidget()
        widget_layout = QVBoxLayout()
        widget_layout.addWidget(QPushButton('Button 1'))
        widget_layout.addWidget(QPushButton('Button 2'))
        widget_container.setLayout(widget_layout)
        main_layout.addWidget(widget_container)
        
        # QGroupBox
        group_box = QGroupBox('Group Box')
        group_layout = QVBoxLayout()
        group_layout.addWidget(QPushButton('Button 3'))
        group_layout.addWidget(QPushButton('Button 4'))
        group_box.setLayout(group_layout)
        main_layout.addWidget(group_box)
        
        self.setLayout(main_layout)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Container Widgets')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ContainerWidgets()
    sys.exit(app.exec_())
```
#### References:
https://pypi.org/project/PyQt5/

