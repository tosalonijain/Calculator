# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 30, 501, 91))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 160, 591, 301))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nine = QtGui.QPushButton(self.layoutWidget)
        self.nine.setObjectName(_fromUtf8("nine"))
        self.gridLayout.addWidget(self.nine, 1, 5, 1, 1)
        self.two = QtGui.QPushButton(self.layoutWidget)
        self.two.setObjectName(_fromUtf8("two"))
        self.gridLayout.addWidget(self.two, 0, 3, 1, 1)
        self.und = QtGui.QPushButton(self.layoutWidget)
        self.und.setObjectName(_fromUtf8("undo"))
        self.gridLayout.addWidget(self.und, 6, 0, 1, 1)
        self.pow = QtGui.QPushButton(self.layoutWidget)
        self.pow.setObjectName(_fromUtf8("pow"))
        self.gridLayout.addWidget(self.pow, 5, 6, 1, 1)
        self.cos = QtGui.QPushButton(self.layoutWidget)
        self.cos.setObjectName(_fromUtf8("cos"))
        self.gridLayout.addWidget(self.cos, 6, 3, 1, 1)
        self.six = QtGui.QPushButton(self.layoutWidget)
        self.six.setObjectName(_fromUtf8("six"))
        self.gridLayout.addWidget(self.six, 1, 1, 1, 1)
        self.zero = QtGui.QPushButton(self.layoutWidget)
        self.zero.setObjectName(_fromUtf8("zero"))
        self.gridLayout.addWidget(self.zero, 0, 0, 1, 1)
        self.into = QtGui.QPushButton(self.layoutWidget)
        self.into.setObjectName(_fromUtf8("into"))
        self.gridLayout.addWidget(self.into, 3, 3, 1, 1)
        self.seven = QtGui.QPushButton(self.layoutWidget)
        self.seven.setObjectName(_fromUtf8("seven"))
        self.gridLayout.addWidget(self.seven, 1, 3, 1, 1)
        self.pi = QtGui.QPushButton(self.layoutWidget)
        self.pi.setObjectName(_fromUtf8("pi"))
        self.gridLayout.addWidget(self.pi, 3, 5, 1, 1)
        self.equals = QtGui.QPushButton(self.layoutWidget)
        self.equals.setObjectName(_fromUtf8("equals"))
        self.gridLayout.addWidget(self.equals, 5, 1, 1, 1)
        self.four = QtGui.QPushButton(self.layoutWidget)
        self.four.setObjectName(_fromUtf8("four"))
        self.gridLayout.addWidget(self.four, 0, 5, 1, 1)
        self.plus = QtGui.QPushButton(self.layoutWidget)
        self.plus.setObjectName(_fromUtf8("plus"))
        self.gridLayout.addWidget(self.plus, 3, 0, 1, 1)
        self.log = QtGui.QPushButton(self.layoutWidget)
        self.log.setObjectName(_fromUtf8("log"))
        self.gridLayout.addWidget(self.log, 5, 3, 1, 1)
        self.minus = QtGui.QPushButton(self.layoutWidget)
        self.minus.setObjectName(_fromUtf8("minus"))
        self.gridLayout.addWidget(self.minus, 3, 1, 1, 1)
        self.by = QtGui.QPushButton(self.layoutWidget)
        self.by.setObjectName(_fromUtf8("by"))
        self.gridLayout.addWidget(self.by, 3, 4, 1, 1)
        self.log10 = QtGui.QPushButton(self.layoutWidget)
        self.log10.setObjectName(_fromUtf8("log10"))
        self.gridLayout.addWidget(self.log10, 5, 4, 1, 1)
        self.sqrt = QtGui.QPushButton(self.layoutWidget)
        self.sqrt.setObjectName(_fromUtf8("sqrt"))
        self.gridLayout.addWidget(self.sqrt, 5, 5, 1, 1)
        self.three = QtGui.QPushButton(self.layoutWidget)
        self.three.setObjectName(_fromUtf8("three"))
        self.gridLayout.addWidget(self.three, 0, 4, 1, 1)
        self.sin = QtGui.QPushButton(self.layoutWidget)
        self.sin.setObjectName(_fromUtf8("sin"))
        self.gridLayout.addWidget(self.sin, 6, 1, 1, 1)
        self.tan = QtGui.QPushButton(self.layoutWidget)
        self.tan.setObjectName(_fromUtf8("tan"))
        self.gridLayout.addWidget(self.tan, 6, 4, 1, 1)
        self.eight = QtGui.QPushButton(self.layoutWidget)
        self.eight.setObjectName(_fromUtf8("eight"))
        self.gridLayout.addWidget(self.eight, 1, 4, 1, 1)
        self.clear = QtGui.QPushButton(self.layoutWidget)
        self.clear.setObjectName(_fromUtf8("clear"))
        self.gridLayout.addWidget(self.clear, 5, 0, 1, 1)
        self.one = QtGui.QPushButton(self.layoutWidget)
        self.one.setObjectName(_fromUtf8("one"))
        self.gridLayout.addWidget(self.one, 0, 1, 1, 1)
        self.e = QtGui.QPushButton(self.layoutWidget)
        self.e.setObjectName(_fromUtf8("e"))
        self.gridLayout.addWidget(self.e, 1, 6, 1, 1)
        self.fac = QtGui.QPushButton(self.layoutWidget)
        self.fac.setObjectName(_fromUtf8("fac"))
        self.gridLayout.addWidget(self.fac, 0, 6, 1, 1)
        self.five = QtGui.QPushButton(self.layoutWidget)
        self.five.setObjectName(_fromUtf8("five"))
        self.gridLayout.addWidget(self.five, 1, 0, 1, 1)
        self.rem = QtGui.QPushButton(self.layoutWidget)
        self.rem.setObjectName(_fromUtf8("rem"))
        self.gridLayout.addWidget(self.rem, 3, 6, 1, 1)
        self.decimal = QtGui.QPushButton(self.layoutWidget)
        self.decimal.setObjectName(_fromUtf8("decimal"))
        self.gridLayout.addWidget(self.decimal, 6, 5, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
         
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.nine.setText(_translate("MainWindow", "9", None))
        self.two.setText(_translate("MainWindow", "2", None))
        self.und.setText(_translate("MainWindow", "backspace", None))
        self.pow.setText(_translate("MainWindow", "pow ^", None))
        self.cos.setText(_translate("MainWindow", "cos ", None))
        self.six.setText(_translate("MainWindow", "6", None))
        self.zero.setText(_translate("MainWindow", "0", None))
        self.into.setText(_translate("MainWindow", "*", None))
        self.seven.setText(_translate("MainWindow", "7", None))
        self.pi.setText(_translate("MainWindow", "pi", None))
        self.equals.setText(_translate("MainWindow", "=", None))
        self.four.setText(_translate("MainWindow", "4", None))
        self.plus.setText(_translate("MainWindow", "+", None))
        self.log.setText(_translate("MainWindow", "log", None))
        self.minus.setText(_translate("MainWindow", "-", None))
        self.by.setText(_translate("MainWindow", "/", None))
        self.log10.setText(_translate("MainWindow", "log10", None))
        self.sqrt.setText(_translate("MainWindow", "sqrt", None))
        self.three.setText(_translate("MainWindow", "3", None))
        self.sin.setText(_translate("MainWindow", "sin", None))
        self.tan.setText(_translate("MainWindow", "tan", None))
        self.eight.setText(_translate("MainWindow", "8", None))
        self.clear.setText(_translate("MainWindow", "clear", None))
        self.one.setText(_translate("MainWindow", "1", None))
        self.e.setText(_translate("MainWindow", "e", None))
        self.fac.setText(_translate("MainWindow", "fac!", None))
        self.five.setText(_translate("MainWindow", "5", None))
        self.rem.setText(_translate("MainWindow", "rem %", None))
        self.decimal.setText(_translate("MainWindow", ".", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

