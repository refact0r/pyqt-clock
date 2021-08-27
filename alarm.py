from PyQt5.QtCore import QTimer

class Alarm():

    def __init__(self, clock):
        self.clock = clock
        self.stopwatch_time = 0
        self.started = False
        self.stopwatch_timer = QTimer(clock)
        self.stopwatch_timer.timeout.connect(self.updateStopwatchTime)

    