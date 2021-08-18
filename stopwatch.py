from PyQt5.QtCore import QTimer

class Stopwatch():

    def __init__(self, clock):
        self.clock = clock
        self.stopwatch_time = 0
        self.started = False
        self.stopwatch_timer = QTimer(clock)
        self.stopwatch_timer.timeout.connect(self.updateStopwatchTime)

    def startStopwatch(self):
        if not self.started:
            self.stopwatch_timer.start(100)
            self.clock.ui.stopwatch_start_button.setText("Stop")
            self.started = True
        else:
            self.stopwatch_timer.stop()
            self.clock.ui.stopwatch_start_button.setText("Start")
            self.started = False

    def resetStopwatch(self):
        self.stopwatch_timer.stop()
        self.clock.ui.stopwatch_start_button.setText("Start")
        self.started = False
        self.stopwatch_time = 0
        self.updateStopwatch()

    def updateStopwatch(self):
        tenths = self.stopwatch_time % 10
        seconds = self.stopwatch_time // 10
        minutes = seconds // 60
        hours = minutes // 60

        string = f"{seconds}.{tenths}"
        if minutes:
            string = f"{minutes}:{self.formatTime(seconds % 60)}.{tenths}"
        if hours:
            string = f"{hours}:{self.formatTime(minutes % 60)}:{self.formatTime(seconds % 60)}.{tenths}"

        self.clock.ui.stopwatch_label.setText(string)

    def updateStopwatchTime(self):
        self.stopwatch_time += 1
        self.updateStopwatch()
    
    def formatTime(self, n):
        if n < 10:
            return "0" + str(n)
        return str(n)

    