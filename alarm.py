from PyQt5.QtCore import QTime, QTimer, QThread
import simpleaudio as sa


class Alarm():

    def __init__(self, clock):
        self.clock = clock
        self.alarms = [[QTime(7, 0, 00), ["Mon", "Tue", "Wed", "Thu", "Fri"], True], [QTime(7, 10, 00), ["Mon", "Tue", "Wed", "Thu", "Fri"], False]]
        self.sound = SoundThread()
        self.current = None

    def start(self, alarm):
        if not alarm:
            return
        self.sound.start()
        self.clock.ui.alarm_hour_label.setText(alarm[0].toString("h ap")[:-3])
        self.clock.ui.alarm_minute_label.setText(
            alarm[0].toString("mm ap")[:-3])
        self.clock.ui.alarm_ampm_label.setText(alarm[0].toString("ap").lower())
        self.clock.ui.alarm_stacked_widget.setCurrentIndex(1)
        self.clock.ui.pages_widget.setCurrentIndex(1)
        self.current = alarm

    def snooze(self):
        self.sound.stop()
        self.clock.ui.pages_widget.setCurrentIndex(0)
        self.clock.ui.alarm_stacked_widget.setCurrentIndex(0)
        current_alarm = self.current
        QTimer.singleShot(300000, lambda: self.start(current_alarm))

    def dismiss(self):
        self.sound.stop()
        self.clock.ui.pages_widget.setCurrentIndex(0)
        self.clock.ui.alarm_stacked_widget.setCurrentIndex(0)

    def toggle(self, index):
        self.alarms[index][2] = not self.alarms[index][2]
        self.clock.ui.alarm_buttons[index].setText("On" if self.alarms[index][2] else "Off")


class Alarm_object():

    def __init__(self, time, days):
        self.time = time
        self.days = days


class SoundThread(QThread):
    play = None

    def run(self):
        wave = sa.WaveObject.from_wave_file("alarm.wav")
        self.playing = True
        while self.playing:
            self.play = wave.play()
            self.play.wait_done()

    def stop(self):
        if self.play:
            self.play.stop()
        self.playing = False
