from PyQt5.QtCore import QTimer


class Stopwatch():

    def __init__(self, clock):
        self.clock = clock
        self.time = 0
        self.started = False
        self.timer = QTimer(clock)
        self.timer.timeout.connect(self.updateStopwatch)

    def start(self):
        if not self.started:
            self.timer.start(10)
            self.clock.ui.stopwatch_start_button.setText("Stop")
            self.started = True
        else:
            self.timer.stop()
            self.clock.ui.stopwatch_start_button.setText("Start")
            self.started = False

    def reset(self):
        self.timer.stop()
        self.clock.ui.stopwatch_start_button.setText("Start")
        self.started = False
        self.time = 0
        self.updateText()

    def updateText(self):
        decimal = self.time % 100
        seconds = self.time // 100
        minutes = seconds // 60
        hours = minutes // 60

        string = f"{seconds}.{decimal:02d}"
        if minutes:
            string = f"{minutes}:{seconds % 60:02d}.{decimal:02d}"
        if hours:
            string = f"{hours}:{minutes % 60:02d}:{seconds % 60:02d}.{decimal:02d}"

        self.clock.ui.stopwatch_label.setText(string)

    def updateStopwatch(self):
        self.time += 1
        self.updateText()
