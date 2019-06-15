# ffmpeg gui, video/audio converter
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
 
class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)
        self.pushButtonSelectFile.clicked.connect(self.onOpen)
        self.pushButtonConvert.clicked.connect(self.onClick)
        self.comboBox.addItem("mpg")
        self.comboBox.addItem("mp3")
        self.comboBox.addItem("mp4")
        self.comboBox.addItem("wav")

    def onClick(self):
        if len(self.path) < 1:
           QMessageBox.critical(self, "Invalid Input", "No input file selected")
        else:
           self.path
           outFormat = self.comboBox.itemText(1)
           self.out = self.path[:-3] + outFormat
           cmd = "ffmpeg -i " + self.path + " -qscale:v 1 " + self.out
           QMessageBox.critical(self, "Command", cmd)
           os.system(cmd)


    def onOpen(self):
       self.path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Video files (*.mp4);Audio files (*.wav);All files (*.*)")


app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())