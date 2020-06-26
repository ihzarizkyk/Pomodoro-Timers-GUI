import sys
from PyQt5.QtWidgets import QApplication
from control_clock import cr_clock

app = QApplication(sys.argv)
timer = cr_clock()
sys.exit(app.exec_())