# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1080, 720))
        Form.setMaximumSize(QtCore.QSize(1080, 720))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1080, 720))
        self.label.setStyleSheet("border-image: url(:/newPrefix/images/background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(30, 30, 1021, 81))
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 700 25pt \"Arial\";\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.5625 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.display = QtWidgets.QLabel(Form)
        self.display.setGeometry(QtCore.QRect(210, 150, 841, 531))
        self.display.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.801136 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.display.setText("")
        self.display.setObjectName("display")
        self.astar = QtWidgets.QPushButton(Form)
        self.astar.setGeometry(QtCore.QRect(40, 470, 131, 41))
        self.astar.setStyleSheet("font: 700 15pt \"Arial\";\n"
"background-color: rgb(111, 111, 111);")
        self.astar.setObjectName("astar")
        self.ucs = QtWidgets.QPushButton(Form)
        self.ucs.setGeometry(QtCore.QRect(40, 530, 131, 41))
        self.ucs.setStyleSheet("font: 700 15pt \"Arial\";\n"
"background-color: rgb(111, 111, 111);")
        self.ucs.setObjectName("ucs")
        self.browse = QtWidgets.QPushButton(Form)
        self.browse.setGeometry(QtCore.QRect(40, 180, 81, 29))
        self.browse.setStyleSheet("font: 700 8pt \"Arial\";\n"
"background-color: rgb(111, 111, 111);")
        self.browse.setObjectName("browse")
        self.filename = QtWidgets.QLineEdit(Form)
        self.filename.setGeometry(QtCore.QRect(40, 210, 151, 21))
        self.filename.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filename.setObjectName("filename")
        self.dropbox_start = QtWidgets.QComboBox(Form)
        self.dropbox_start.setGeometry(QtCore.QRect(40, 310, 130, 22))
        self.dropbox_start.setObjectName("dropbox_start")
        self.dropbox_goal = QtWidgets.QComboBox(Form)
        self.dropbox_goal.setGeometry(QtCore.QRect(40, 370, 130, 22))
        self.dropbox_goal.setObjectName("dropbox_goal")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 289, 131, 20))
        self.label_2.setStyleSheet("font: 700 8pt \"Arial\";\n"
"background-color: rgb(111, 111, 111);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(40, 349, 131, 20))
        self.label_3.setStyleSheet("font: 700 8pt \"Arial\";\n"
"background-color: rgb(111, 111, 111);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Menentukan Lintasan Terpendek"))
        self.astar.setText(_translate("Form", "A*"))
        self.ucs.setText(_translate("Form", "UCS"))
        self.browse.setText(_translate("Form", "Browse"))
        self.label_2.setText(_translate("Form", "Start"))
        self.label_3.setText(_translate("Form", "Goal"))
import resources_rc
