# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# { Import Required Services
import os, sys, res, time, logging, subprocess, mysql.connector, webbrowser
# }

class Ui_Interface(object):
    def setupUi(self, Interface):
        Interface.setObjectName("Interface")
        Interface.resize(625, 565)

# { remove background frame 
        Interface.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Interface.setAttribute(QtCore.Qt.WA_TranslucentBackground)
# }

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/picture/QC.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Interface.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Interface)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(204,0,19,1), stop:1 rgba(200,190,190,1));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(204,0,19,1), stop:1 rgba(200,190,190,1));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgba(255,255,255,255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color:rgba(131,96,53,255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91,88,53,255);\n"
"}")
        self.widget.setObjectName("widget")
        self.main_menu = QtWidgets.QLabel(self.widget)
        self.main_menu.setGeometry(QtCore.QRect(50, 30, 241, 430))
        self.main_menu.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-top-right-radius: 50px;\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 50px;\n"
"border-bottom-left-radius: 50px;")
        self.main_menu.setText("")
        self.main_menu.setObjectName("main_menu")
        self.log_process = QtWidgets.QLabel(self.widget)
        self.log_process.setGeometry(QtCore.QRect(270, 60, 274, 430))
        self.log_process.setStyleSheet("background-color:rgba(0,0,0,180);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom-left-radius: 50px;\n"
"border-bottom-right-radius: 50px;\n"
"border-top-right-radius: 50px;")
        self.log_process.setText("")
        self.log_process.setObjectName("log_process")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 80, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(24)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(76, 390, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(110, 50, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(0,0,40);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(70, 47, 30, 30))
        self.label_6.setStyleSheet("image: url(:/images/picture/QC.ico);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 290, 90, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 290, 90, 24))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 250, 90, 24))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 250, 90, 24))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setGeometry(QtCore.QRect(122, 330, 90, 24))
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(90, 110, 161, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(8, 20, 58, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(8, 36, 58, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 54, 141, 21))
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(297, 110, 240, 270))
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 236, 260))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setCursorWidth(0)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(340, 390, 160, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(154, 82, 28, 12))
        self.label_5.setObjectName("label_5")
        self.log_process.raise_()
        self.main_menu.raise_()
        self.pushButton_5.raise_()
        self.pushButton.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.gridLayoutWidget.raise_()
        self.label_5.raise_()

# { Graphic effect
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
# }

        self.retranslateUi(Interface)
        QtCore.QMetaObject.connectSlotsByName(Interface)

    def retranslateUi(self, Interface):
        _translate = QtCore.QCoreApplication.translate
        Interface.setWindowTitle(_translate("Interface", "QCDL FACTORY - V1.0 [HadiK IT]"))
        self.pushButton_5.setText(_translate("Interface", "ê"))
        self.pushButton.setText(_translate("Interface", "Log Out"))
        self.label_7.setText(_translate("Interface", "QCDL FACTORY"))
        self.pushButton_6.setText(_translate("Interface", "REMOVE MI"))
        self.pushButton_7.setText(_translate("Interface", "ADD LOADER"))
        self.pushButton_8.setText(_translate("Interface", "FACTORY RESET"))
        self.pushButton_9.setText(_translate("Interface", "ERASE EFS"))
        self.pushButton_10.setText(_translate("Interface", "REBOOT"))
        self.groupBox.setTitle(_translate("Interface", "Info : "))
        self.label.setText(_translate("Interface", "Username : "))
        self.label_2.setText(_translate("Interface", "Expired     :"))
        self.label_3.setText(_translate("Interface", "   add loader then continue..."))
        self.label_4.setText(_translate("Interface", "* If auto loader error, please"))
        self.groupBox_2.setTitle(_translate("Interface", "Log : "))
        self.pushButton_2.setText(_translate("Interface", "E"))
        self.pushButton_3.setText(_translate("Interface", "M"))
        self.pushButton_4.setText(_translate("Interface", ")"))
        self.label_5.setText(_translate("Interface", "V1.0"))

# { Button clicked function
        self.pushButton_5.clicked.connect(lambda:Interface.close())
        self.pushButton_2.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/f.hadikhoir'))
        self.pushButton_3.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/c/HadiKIT'))
        self.pushButton_4.clicked.connect(lambda: webbrowser.open('https://github.com/HadiKhoirudin/qcdl_factory'))
# }

# { Set-up Main app.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interface = QtWidgets.QWidget()
    ui = Ui_Interface()
    ui.setupUi(Interface)
    Interface.show()
    sys.exit(app.exec_())
# }