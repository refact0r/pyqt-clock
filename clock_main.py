from PyQt5 import QtWidgets
from clock import Ui_main_widget
from stopwatch import Stopwatch
from timer import Timer

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt

class ClockWindow(QWidget):

    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = Ui_main_widget()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 800, 480)        
        self.setFixedSize(800, 480)

        # set pointer for buttons
        for button in self.ui.page_buttons_frame.findChildren(QtWidgets.QPushButton):
            button.setCursor(Qt.PointingHandCursor)

        # set page buttons 
        self.ui.clock_button.clicked.connect(lambda: self.ui.pages_widget.setCurrentIndex(0))
        self.ui.alarm_button.clicked.connect(lambda: self.ui.pages_widget.setCurrentIndex(1))
        self.ui.stopwatch_button.clicked.connect(lambda: self.ui.pages_widget.setCurrentIndex(2))
        self.ui.timer_button.clicked.connect(lambda: self.ui.pages_widget.setCurrentIndex(3))

        # set clock timer
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.showTime)
        self.clock_timer.start(1000)

        # initialize stopwatch
        self.stopwatch = Stopwatch(self)
        self.ui.stopwatch_start_button.clicked.connect(lambda: self.stopwatch.startStopwatch())
        self.ui.stopwatch_reset_button.clicked.connect(lambda: self.stopwatch.resetStopwatch())

        self.timer = Timer(self)
        self.ui.timer_0_button.clicked.connect(lambda: self.timer.inputTime(0))
        self.ui.timer_1_button.clicked.connect(lambda: self.timer.inputTime(1))
        self.ui.timer_2_button.clicked.connect(lambda: self.timer.inputTime(2))
        self.ui.timer_3_button.clicked.connect(lambda: self.timer.inputTime(3))
        self.ui.timer_4_button.clicked.connect(lambda: self.timer.inputTime(4))
        self.ui.timer_5_button.clicked.connect(lambda: self.timer.inputTime(5))
        self.ui.timer_6_button.clicked.connect(lambda: self.timer.inputTime(6))
        self.ui.timer_7_button.clicked.connect(lambda: self.timer.inputTime(7))
        self.ui.timer_8_button.clicked.connect(lambda: self.timer.inputTime(8))
        self.ui.timer_9_button.clicked.connect(lambda: self.timer.inputTime(9))
        self.ui.timer_delete_button.clicked.connect(lambda: self.timer.deleteInput())
        self.ui.timer_start_button.clicked.connect(lambda: self.timer.inputTime(9))

    def showTime(self):
        current_time = QTime.currentTime()

        self.ui.clock_time_label.setText(current_time.toString("h:mm ap")[:-3])
        self.ui.clock_seconds_label.setText(current_time.toString("ss"))
        self.ui.clock_ampm_label.setText(current_time.toString("ap").lower())

App = QApplication(sys.argv)
window = ClockWindow()
window.setStyleSheet(open('clock_styles.qss', 'r').read())
window.show()
App.exit(App.exec_())
