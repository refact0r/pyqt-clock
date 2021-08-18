from PyQt5.QtCore import QTimer

class Timer():

    def __init__(self, clock):
        self.clock = clock
        self.timer_input = ""
        self.started = False
        self.timer_timer = QTimer(clock)
        # self.timer_timer.timeout.connect()

    def inputTime(self, value):
        self.timer_input += str(value)
        self.addColons()
        self.clock.ui.timer_input_label.setText(self.timer_input)

    def deleteInput(self):
        self.timer_input = self.timer_input[0:-1]
        self.addColons()
        self.clock.ui.timer_input_label.setText(self.timer_input)

    def addColons(self):
        if len(self.timer_input) < 3:
            return
        split = "".join(self.timer_input.split(":"))
        list = []
        for i in range(len(split), 0, -2):
            if i - 2 < 0:
                list = [split[i-1:i]] + list
            else:
                list = [split[i-2:i]] + list
        self.timer_input = ":".join(list)