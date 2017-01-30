from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import design1 #importing design code
from math import log, log10, sqrt, sin, cos, tan, radians #importing maths module
n = 0.0
new = 0.0
tot = 0.0
operator = ""
op = False
c = 0
a=0
class calculator(QtGui.QMainWindow, design1.Ui_MainWindow):
    def __init__(self, parent=None):

        super(calculator, self).__init__(parent)
        self.setupUi(self)
        self.textEdit.setReadOnly(True)
        self.textEdit.setText("0")
        self.zero.clicked.connect(self.nums)
        self.one.clicked.connect(self.nums)
        self.two.clicked.connect(self.nums)
        self.three.clicked.connect(self.nums)
        self.four.clicked.connect(self.nums)
        self.five.clicked.connect(self.nums)
        self.six.clicked.connect(self.nums)
        self.seven.clicked.connect(self.nums)
        self.eight.clicked.connect(self.nums)
        self.nine.clicked.connect(self.nums)
        self.equals.clicked.connect(self.Equal)
        self.into.clicked.connect(self.Operator)
        self.by.clicked.connect(self.Operator)
        self.plus.clicked.connect(self.Operator)
        self.minus.clicked.connect(self.Operator)
        self.rem.clicked.connect(self.Operator)
        self.fac.clicked.connect(self.fc)
        self.log.clicked.connect(self.Operator)
        self.log10.clicked.connect(self.Operator)
        self.sin.clicked.connect(self.Operator)
        self.cos.clicked.connect(self.Operator)
        self.tan.clicked.connect(self.Operator)
        self.sqrt.clicked.connect(self.Operator)
        self.pow.clicked.connect(self.Operator)
        self.clear.clicked.connect(self.Clear)
        self.und.clicked.connect(self.Undo)
        self.decimal.clicked.connect(self.Dec)
        self.pi.clicked.connect(self.Pie)
        self.e.clicked.connect(self.ee)


    def nums(self): #when digits are clicked
        global a
        global n
        global new
        global op
        sender = self.sender()
         
        a = int(sender.text())
        
        if op == False:
            self.textEdit.setText( self.textEdit.toPlainText()+ str(a))
 
 
        else:
            self.textEdit.setText(str(a))
            op = False

    def Operator(self): #carry different operations
        global c
        global n
        global op
        global operator
        global new
        global a
        global tot
        c=c+1
        
        if c > 1:
            self.Equal()

        sender = self.sender()
        n=float(self.textEdit.toPlainText())
        operator = sender.text()
        op = True



    def Equal(self): #showing answers
        global n
        global new
        global tot
        global operator
        global op
        global c
        global a
        c = 0 
        a=float(self.textEdit.toPlainText())
        if operator == "+":
            tot = float(n) + float(a)
 
        elif operator == "-":
            tot = float(n) - float(a)
 
        elif operator == "/":
            tot = float(n) / float(a)
 
        elif operator == "*":
            tot = float(n) * float(a)
        elif operator == "rem %" :
            tot = float(n) % float(a)
        elif operator =="log" :
            tot=log(float(a))
        elif operator=="log10":
            tot=log10(float(a))
        elif operator=="sin":
            x=float(a)
            y=radians(x)
            tot=sin(float(y))
        elif operator=="cos":
            x=float(a)
            y=radians(x)
            tot=cos(float(a))
        elif operator=="tan":
            x=float(a)
            y=radians(x)
            tot=tan(float(a))
        elif operator=="sqrt":
            tot=sqrt(float(a))
        elif operator=="pow ^":
            tot=pow(n,a)
        self.textEdit.setText(str(tot))
        op=True

    def fc(self):
        fac=1
        for i in xrange(1,int(self.textEdit.toPlainText())+1):
            fac=fac*i;
        tot=fac
             
        self.textEdit.setText(str(tot))
    def Clear(self): #clear
        self.textEdit.setText("0")
        n = 0.0
        new = 0.0
        tot = 0.0
        operator = ""
        op = False
        c = 0
        a=0
    def Undo(self):
        s=str(self.textEdit.toPlainText())
        l=len(s)
        ss=str(s[0:l-1])
        self.textEdit.setText(ss)
    def Dec(self): #decimal numbers
        if "." not in self.textEdit.toPlainText():
            self.textEdit.setText(self.textEdit.toPlainText() + ".")
    def Pie(self):
        self.textEdit.setText("3.1416")
    def ee(self):
        self.textEdit.setText("2.7182")

             
def main():
    app = QtGui.QApplication(sys.argv)
    form = calculator()
    form.setWindowTitle("calculator")
    p = form.palette()
    p.setColor(form.backgroundRole(), QtCore.Qt.blue) #changing back ground colour
    form.setPalette(p)
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()
