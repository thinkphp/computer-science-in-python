from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer, QPoint, QSize
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont, QRadialGradient
import sys
import math
from datetime import datetime

class AnalogClock(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set up timer for updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Update every second

        # Set window background
        self.setStyleSheet("background-color: #2b2b2b;")

        # Set minimum size
        self.setMinimumSize(400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Smooth drawing

        # Calculate center and clock radius
        center = QPoint(self.width() // 2, self.height() // 2)
        radius = min(self.width(), self.height()) // 2 - 10

        self.drawClockFace(painter, center, radius)
        self.drawNumbers(painter, center, radius)
        self.drawHands(painter, center, radius)
        self.drawCenterPoint(painter, center)

    def drawClockFace(self, painter, center, radius):
        # Create gradient for clock face
        gradient = QRadialGradient(center, radius)
        gradient.setColorAt(0, QColor("#3a3a3a"))
        gradient.setColorAt(0.8, QColor("#303030"))
        gradient.setColorAt(1, QColor("#2b2b2b"))

        # Draw main clock circle
        painter.setPen(QPen(QColor("#444444"), 2, Qt.SolidLine))
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(center, radius, radius)

        # Draw tick marks
        painter.setPen(QPen(QColor("#dddddd"), 1, Qt.SolidLine))
        for i in range(60):
            angle = i * 6  # 360 / 60 = 6 degrees per minute
            if i % 5 == 0:  # Hour marks
                painter.setPen(QPen(QColor("#dddddd"), 2, Qt.SolidLine))
                self.drawTick(painter, center, radius, angle, 15)
            else:  # Minute marks
                painter.setPen(QPen(QColor("#666666"), 1, Qt.SolidLine))
                self.drawTick(painter, center, radius, angle, 7)

    def drawTick(self, painter, center, radius, angle, length):
        angle_rad = math.radians(angle - 90)
        outer_x = center.x() + (radius - 3) * math.cos(angle_rad)
        outer_y = center.y() + (radius - 3) * math.sin(angle_rad)
        inner_x = center.x() + (radius - length - 3) * math.cos(angle_rad)
        inner_y = center.y() + (radius - length - 3) * math.sin(angle_rad)
        painter.drawLine(int(outer_x), int(outer_y), int(inner_x), int(inner_y))

    def drawNumbers(self, painter, center, radius):
        font = QFont('Arial', radius // 15, QFont.Bold)
        painter.setFont(font)
        painter.setPen(QColor("#dddddd"))

        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)  # 360 / 12 = 30 degrees per hour
            x = center.x() + (radius - 35) * math.cos(angle)
            y = center.y() + (radius - 35) * math.sin(angle)

            # Center the numbers properly
            text = str(i)
            rect = painter.fontMetrics().boundingRect(text)
            painter.drawText(int(x - rect.width() // 2),
                           int(y + rect.height() // 2), text)

    def drawHands(self, painter, center, radius):
        time = datetime.now()

        # Hour hand
        hour_angle = (time.hour % 12 + time.minute / 60.0) * 30 - 90
        self.drawHand(painter, center, hour_angle, radius * 0.5,
                     QColor("#dddddd"), 4)

        # Minute hand
        minute_angle = (time.minute + time.second / 60.0) * 6 - 90
        self.drawHand(painter, center, minute_angle, radius * 0.7,
                     QColor("#dddddd"), 3)

        # Second hand
        second_angle = time.second * 6 - 90
        self.drawHand(painter, center, second_angle, radius * 0.8,
                     QColor("#ff4444"), 1)

    def drawHand(self, painter, center, angle, length, color, width):
        angle_rad = math.radians(angle)
        painter.setPen(QPen(color, width, Qt.SolidLine, Qt.RoundCap))
        painter.drawLine(center.x(), center.y(),
                        int(center.x() + length * math.cos(angle_rad)),
                        int(center.y() + length * math.sin(angle_rad)))

    def drawCenterPoint(self, painter, center):
        # Draw outer circle
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#dddddd"))
        painter.drawEllipse(center, 8, 8)

        # Draw inner circle
        painter.setBrush(QColor("#ff4444"))
        painter.drawEllipse(center, 4, 4)

    def sizeHint(self):
        return QSize(400, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create main window
    window = QMainWindow()
    window.setWindowTitle("Elegant Analog Clock")
    window.setStyleSheet("background-color: #2b2b2b;")

    # Create and set clock as central widget
    clock = AnalogClock()
    window.setCentralWidget(clock)

    # Show window
    window.show()
    sys.exit(app.exec_())
