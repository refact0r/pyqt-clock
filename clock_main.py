from clock import Ui_main_widget
from stopwatch import Stopwatch
from timer import Timer
from alarm import Alarm

import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt, QDateTime


class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super(CustomWidget, self).__init__(parent)
        self.button = QtWidgets.QPushButton("on")
        lay = QtWidgets.QHBoxLayout(self)
        lay.addWidget(self.button, alignment=QtCore.Qt.AlignRight)
        lay.setContentsMargins(0, 0, 0, 0)


class ClockWindow(QWidget):

    def __init__(self):
        super().__init__()

        # setup ui
        self.ui = Ui_main_widget()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 800, 480)
        # self.setFixedSize(800, 480)
        # self.showMaximized()
        self.showFullScreen()

        # set pointer for buttons
        for button in self.ui.page_buttons_frame.findChildren(QtWidgets.QPushButton):
            button.setCursor(Qt.PointingHandCursor)

        # set page buttons
        self.ui.clock_button.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentIndex(0))
        self.ui.alarm_button.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentIndex(1))
        self.ui.stopwatch_button.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentIndex(2))
        self.ui.timer_button.clicked.connect(
            lambda: self.ui.pages_widget.setCurrentIndex(3))

        # set clock timer
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.showTime)
        start = QTime.currentTime().second()
        while True:
            if QTime.currentTime().second() != start:
                time.sleep(0.01)
                self.clock_timer.start(1000)
                break

        # initialize alarm
        self.alarm = Alarm(self)
        self.ui.alarm_snooze_button.clicked.connect(self.alarm.snooze)
        self.ui.alarm_dismiss_button.clicked.connect(self.alarm.dismiss)

        self.ui.alarm_list.setSpacing(10)
        self.ui.alarm_buttons = []
        toggle = lambda i: lambda : self.alarm.toggle(i)
        for i, a in enumerate(self.alarm.alarms):
            item = QtWidgets.QListWidgetItem(a[0].toString("h:mm ap").lower() + " - " + ",".join(a[1]))
            widget = QtWidgets.QWidget()

            widgetButton = QtWidgets.QPushButton("On" if a[2] else "Off")
            widgetButton.setObjectName("alarm_toggle_button")
            widgetButton.clicked.connect(toggle(i))
            self.ui.alarm_buttons.append(widgetButton)

            widgetLayout = QtWidgets.QHBoxLayout()
            widgetLayout.addWidget(widgetButton, alignment=QtCore.Qt.AlignRight)
            widgetLayout.setContentsMargins(0, 0, 0, 0)
            widget.setLayout(widgetLayout)

            self.ui.alarm_list.addItem(item)
            self.ui.alarm_list.setItemWidget(item, widget)
        # initialize stopwatch
        self.stopwatch = Stopwatch(self)
        self.ui.stopwatch_start_button.clicked.connect(self.stopwatch.start)
        self.ui.stopwatch_reset_button.clicked.connect(self.stopwatch.reset)

        # initialize timer
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
        self.ui.timer_delete_button.clicked.connect(self.timer.deleteInput)
        self.ui.timer_start_button.clicked.connect(self.timer.start)
        self.ui.timer_stop_button.clicked.connect(self.timer.stop)
        self.ui.timer_reset_button.clicked.connect(self.timer.reset)

    def showTime(self):
        current_time = QDateTime.currentDateTime()

        for a in self.alarm.alarms:
            if current_time.time().secsTo(a[0]) == 0 and current_time.toString("ddd") in a[1] and a[2]:
                self.alarm.start(a)

        self.ui.clock_hour_label.setText(current_time.toString("h ap")[:-3])
        self.ui.clock_minute_label.setText(current_time.toString("mm ap")[:-3])
        self.ui.clock_seconds_label.setText(current_time.toString("ss"))
        self.ui.clock_ampm_label.setText(current_time.toString("ap").lower())


App = QApplication(sys.argv)
window = ClockWindow()
window.setStyleSheet(open('clock_styles.qss', 'r').read())
window.show()
App.exit(App.exec_())
