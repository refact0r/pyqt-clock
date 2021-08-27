from PyQt5.QtCore import QTimer


class Timer():

    def __init__(self, clock):
        self.clock = clock
        self.input = ""
        self.time = 0
        self.started = False
        self.timer = QTimer(clock)
        self.timer.timeout.connect(self.updateTimer)

    def inputTime(self, value):
        self.input += str(value)
        self.addColons()
        self.clock.ui.timer_input_label.setText(self.input)

    def deleteInput(self):
        self.input = self.input[0:-1]
        self.addColons()
        self.clock.ui.timer_input_label.setText(self.input)

    def start(self):
        if len(self.input) < 1:
            return
        times = [int(s) for s in self.input.split(":")]
        self.time += times[-1]
        if len(times) >= 2:
            self.time += 60 * times[-2]
        if len(times) >= 3:
            self.time += 60 * 60 * times[-3]
        if len(times) >= 4:
            self.time += 24 * 60 * 60 * times[-4]
        if self.time < 0:
            return
        self.updateTimerText()
        self.started = True
        self.clock.ui.timer_stacked_widget.setCurrentIndex(1)
        self.timer.start(1000)

    def stop(self):
        if not self.started:
            self.timer.start(1000)
            self.clock.ui.timer_stop_button.setText("Stop")
            self.started = True
        else:
            self.timer.stop()
            self.clock.ui.timer_stop_button.setText("Start")
            self.started = False

    def reset(self):
        self.timer.stop()
        self.input = ""
        self.time = 0
        self.clock.ui.timer_input_label.setText(self.input)
        self.clock.ui.timer_stacked_widget.setCurrentIndex(0)

    def updateTimer(self):
        self.time -= 1
        self.updateTimerText()

    def updateTimerText(self):
        seconds = self.time
        minutes = seconds // 60
        hours = minutes // 60
        days = hours // 24
 
        string = f"{minutes}:{seconds % 60:02d}"
        if hours:
            string = f"{hours}:{minutes % 60:02d}:{seconds % 60:02d}"
        if days:
            string = f"{days}:{hours % 24:02d}:{minutes % 60:02d}:{seconds % 60:02d}"

        self.clock.ui.timer_time_label.setText(string)

    def addColons(self):
        if len(self.input) < 3:
            return
        clean = "".join(self.input.split(":"))
        list = []
        for i in range(len(clean), 0, -2):
            if len(list) == 3:
                list = [clean[0:i]] + list
                break
            if i - 2 < 0:
                list = [clean[i - 1:i]] + list
            else:
                list = [clean[i - 2:i]] + list
        self.input = ":".join(list)
