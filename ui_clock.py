# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clock.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Clock(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("*{\n"
"    background: #16a085;\n"
"}\n"
"QFrame{\n"
"    background: #67e6dc;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 70, 641, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(190, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.icon = QtWidgets.QLabel(self.frame)
        self.icon.setGeometry(QtCore.QRect(120, 10, 71, 61))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("gambar/fast-time.png"))
        self.icon.setObjectName("icon")
        self.play = QtWidgets.QPushButton(Form)
        self.play.setGeometry(QtCore.QRect(40, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play.setStyleSheet("QPushButton{\n"
"    background: #2ecc71;\n"
"    font-size: 15 px;\n"
"    border:none;\n"
"    border-radius:15px;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: #B3B3B3;\n"
"}")
        self.play.setObjectName("play")
        self.stop = QtWidgets.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(420, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop.setStyleSheet("QPushButton{\n"
"    background: #c0392b;\n"
"    font-size: 15 px;\n"
"    border: none;\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: #B3B3B3;\n"
"}")
        self.stop.setObjectName("stop")
        self.timers = QtWidgets.QLabel(Form)
        self.timers.setGeometry(QtCore.QRect(190, 210, 261, 111))
        font = QtGui.QFont()
        font.setFamily("White Rabbit")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.timers.setFont(font)
        self.timers.setStyleSheet("background:#16a085;")
        self.timers.setAlignment(QtCore.Qt.AlignCenter)
        self.timers.setObjectName("timers")
        self.replay = QtWidgets.QPushButton(Form)
        self.replay.setGeometry(QtCore.QRect(230, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.replay.setFont(font)
        self.replay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.replay.setStyleSheet("QPushButton{\n"
"    background: #3498db;\n"
"    font-size: 15 px;\n"
"    border:none;\n"
"    border-radius:15px;\n"
"    border-color:black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: #B3B3B3;\n"
"}")
        self.replay.setObjectName("replay")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "POMODORO TIMER"))
        self.play.setText(_translate("Form", "PLAY"))
        self.stop.setText(_translate("Form", "STOP"))
        self.timers.setText(_translate("Form", "25:00"))
        self.replay.setText(_translate("Form", "REPLAY"))
