from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from ui_clock import Ui_Clock

class cr_clock(QtWidgets.QMainWindow, Ui_Clock):
	def __init__(self):
		super().__init__()
		self.hitungan = 60*25
		self.setupUi(self)
		self.show()
		self.ref = QTimer()
		self.ref.setInterval(1000)
		self.ref.timeout.connect(self.hitungmundur)
		self.play.clicked.connect(self.start)
		self.stop.clicked.connect(self.finish)
		self.replay.clicked.connect(self.ulang)

	# def start berfungsi untuk memulai timer
	def start(self):
		self.ref.start()

	# def ulang berfungsi untuk mengulang waktu ke menit semula
	def ulang(self):
		self.hitungan = 60*25
		self.ref.start()

	# def finish merupakan fungsi yang digunakan untuk menstop program,
	# ketika tombol stop ditekan

	def finish(self):
		self.ref.stop()


	def hitungmundur(self):
	# jika hitungan sampai detik ke 0 maka program stop
		if(self.hitungan == 0):
			self.ref.stop()
	# jika belum, program akan terus berjalan
		else:
			self.hitungan -=1 
			mins, secs = divmod(self.hitungan, 60)
			self.timers.setText(f'{mins:02d}:{secs:02d}')