import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, Qt, QElapsedTimer


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.elapsed = 0
        self.clock = QElapsedTimer()

        self.time_label = QLabel("00:00:00:00")
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(700, 300, 500, 300)

        self.setStyleSheet("""
            QWidget {
                background-color: black;
            }
            QLabel {
                color: red;
                font-family: Arial;
                font-size: 40px;
                font-weight: bold;
            }
            QPushButton {
                color: red;
                background-color: black;
                border: 2px solid red;
                font-family: Arial;
                font-size: 18px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #330000;
            }
        """)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    def start(self):
        if not self.timer.isActive():
            self.clock.start()
            self.timer.start(10)

    def stop(self):
        if self.timer.isActive():
            self.elapsed += self.clock.elapsed()
            self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.elapsed = 0
        self.time_label.setText("00:00:00:00")

    def format_time(self, milliseconds):
        hours = milliseconds // 3600000
        minutes = (milliseconds // 60000) % 60
        seconds = (milliseconds // 1000) % 60
        centiseconds = (milliseconds % 1000) // 10

        return (f"{hours:02}:{minutes:02}:"
                f"{seconds:02}:{centiseconds:02}")

    def update_display(self):
        current_time = self.elapsed + self.clock.elapsed()
        self.time_label.setText(
            self.format_time(current_time)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())