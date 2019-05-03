import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer
from interfacefinal import Ui_Dialog

class ProgressBarDemo(QWidget):
                
	def __init__(self):
		super().__init__()

		self.progressBar = QProgressBar(self)
		self.progressBar.setGeometry(30, 40, 200, 25)

		self.btnStart = QPushButton('Start SIR', self)
		self.btnStart.move(30, 90)
		self.btnStart.clicked.connect(self.startProgress) 

		
		self.timer = QBasicTimer()
		self.step = 0

	

	def startProgress(self):
		if self.timer.isActive():
			self.timer.stop()
			self.btnStart.setText('Start SIR')
		else:
			self.timer.start(100, self)
			self.btnStart.setText('SIR will launch')

	def timerEvent(self, event):
		if self.step >= 100:
			self.timer.stop()
			self.btnStart.setText('Click here')
			return

		self.step +=1
		self.progressBar.setValue(self.step)

if __name__=='__main__':
	app = QApplication(sys.argv)

	demo = ProgressBarDemo()
	demo.show()

	sys.exit(app.exec_())
