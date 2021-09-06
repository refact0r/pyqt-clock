from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt, QDateTime


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.list = QtWidgets.QListWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.list)

    def addListItem(self, text):
        item = QtWidgets.QListWidgetItem(text)
        self.list.addItem(item)
        widget = QtWidgets.QWidget(self.list)
        button = QtWidgets.QToolButton(widget)
        layout = QtWidgets.QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()
        layout.addWidget(button)
        self.list.setItemWidget(item, widget)
        button.clicked.connect(
            lambda: self.handleButtonClicked(item))

    def handleButtonClicked(self, item):
        print(item.text())

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    for label in 'red blue green yellow purple'.split():
        window.addListItem(label)
    window.setGeometry(500, 300, 300, 200)
    window.show()
    sys.exit(app.exec_())