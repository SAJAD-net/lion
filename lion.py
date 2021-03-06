# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lion-v0.5.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView 


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(808, 606)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget#widget{\n"
"    border : 4px solid rgb(45, 45, 45);\n"
"    border-top-left-radius:30px;\n"
"    border-top-right-radius:30px;"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"    background-color:rgb(20,20,20);\n"
"    border-top-left-radius:25px;\n"
"    border-top-right-radius:25px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    background-color:rgb(20,20,20);\n"
"    color:rgb(144, 144, 144);\n"
"    border-radius:11px;\n"
"    font:bold;\n"
"    font-size:50;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color:rgb(71, 79, 91);\n"
"    color:rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover{\n"
"    background-color:rgb(250, 50, 50);\n"
"    color:rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover{\n"
"    background-color:rgb(71, 79, 91);\n"
"    color:rgb(144, 144, 144);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#pushButton_4:hover{\n"
"    background-color:rgb(71, 79, 91);\n"
"    color:rgb(144, 144, 144);\n"
"}\n"
"\n"
"\n"
"QPushButton#pushButton_5:hover{\n"
"    background-color:rgb(71, 79, 91);\n"
"    color:rgb(144, 144, 144);\n"
"}\n"
"\n"
"QPushButton#pushButton_6:hover{\n"
"    background-color:rgb(71, 79, 91);\n"
"    color:rgb(144, 144, 144);\n"
"}\n"
"\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(12, 9, 12, 9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMinimumSize(QtCore.QSize(15, 15))
        self.label_6.setMaximumSize(QtCore.QSize(15, 15))
        self.label_6.setStyleSheet("background-color:rgb(142, 190, 27);\n"
"border-radius:7px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setMinimumSize(QtCore.QSize(15, 15))
        self.label_5.setMaximumSize(QtCore.QSize(15, 15))
        self.label_5.setStyleSheet("background-color:rgb(250, 50, 50);\n"
"border-radius:7px;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(15, 15))
        self.label_4.setMaximumSize(QtCore.QSize(15, 15))
        self.label_4.setStyleSheet("background-color:rgb(0, 100, 170);\n"
"border-radius:7px;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMinimumSize(QtCore.QSize(600, 12))
        self.label_3.setMaximumSize(QtCore.QSize(60000, 12))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(94, 92, 100);")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setStyleSheet("font-size:10px;")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setStyleSheet("background-color:rgb(31 ,31 ,31);\n"
"border-radius:9px;\n"
"color:rgb(144, 144, 144);\n"
"margin-right:100px;"
"padding-left:2px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.webEngineView = QWebEngineView(self.widget)
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.verticalLayout.addWidget(self.widget)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "LION"))
        self.pushButton.setText(_translate("Form", "???"))
        self.pushButton_3.setText(_translate("Form", "???"))
        self.pushButton_2.setText(_translate("Form", "???"))
        self.pushButton_4.setText(_translate("Form", "???"))
        self.pushButton_5.setText(_translate("Form", "???"))
        self.pushButton_6.setText(_translate("Form", "???"))
        self.lineEdit.setPlaceholderText(_translate("Form", "???? enter address"))
        
       
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
