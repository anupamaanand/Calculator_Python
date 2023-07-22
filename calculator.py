valids = {'x': '[\'x\', \'+\', \'÷\', \'^\']', '+': '[\'x\', \'+\', \'÷\', \'^\']',
          '/': '[\'x\', \'+\', \'÷\', \'^\']',
          '^': '[\'x\', \'+\', \'÷\', \'^\']', '-': '[\'x\',\'÷\', \'^\']',
          '(': '[\'x\', \'+\', \'÷\', \'^\',\'(\']'}
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 450)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(165, 163, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 146, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 163, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 146, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 146, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 146, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)

        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CalcScreen = QtWidgets.QLabel(self.centralwidget)
        self.CalcScreen.setGeometry(QtCore.QRect(10, 15, 280, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 211, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.CalcScreen.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.CalcScreen.setFont(font)
        self.CalcScreen.setAutoFillBackground(True)
        self.CalcScreen.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.CalcScreen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CalcScreen.setLineWidth(1)
        self.CalcScreen.setMidLineWidth(0)
        self.CalcScreen.setText("")
        self.CalcScreen.setObjectName("CalcScreen")

        self.Calc1 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc1.setGeometry(QtCore.QRect(10, 120, 50, 40))
        self.Calc1.setAutoRepeat(False)
        self.Calc1.setObjectName("Calc1")

        self.Calc2 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc2.setGeometry(QtCore.QRect(70, 120, 50, 40))
        self.Calc2.setAutoRepeat(False)
        self.Calc2.setObjectName("Calc2")

        self.Calc3 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc3.setGeometry(QtCore.QRect(130, 120, 50, 40))
        self.Calc3.setAutoRepeat(False)
        self.Calc3.setObjectName("Calc3")

        self.Calc4 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc4.setGeometry(QtCore.QRect(10, 170, 50, 40))
        self.Calc4.setAutoRepeat(False)
        self.Calc4.setObjectName("Calc4")

        self.Calc5 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc5.setGeometry(QtCore.QRect(70, 170, 50, 40))
        self.Calc5.setAutoRepeat(False)
        self.Calc5.setObjectName("Calc5")

        self.Calc6 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc6.setGeometry(QtCore.QRect(130, 170, 50, 40))
        self.Calc6.setAutoRepeat(False)
        self.Calc6.setObjectName("Calc6")

        self.Calc7 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc7.setGeometry(QtCore.QRect(10, 220, 50, 40))
        self.Calc7.setAutoRepeat(False)
        self.Calc7.setObjectName("Calc7")

        self.Calc8 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc8.setGeometry(QtCore.QRect(70, 220, 50, 40))
        self.Calc8.setAutoRepeat(False)
        self.Calc8.setObjectName("Calc8")

        self.Calc9 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc9.setGeometry(QtCore.QRect(130, 220, 50, 40))
        self.Calc9.setAutoRepeat(False)
        self.Calc9.setObjectName("Calc9")

        self.Calc0 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc0.setGeometry(QtCore.QRect(70, 270, 50, 40))
        self.Calc0.setAutoRepeat(False)
        self.Calc0.setObjectName("Calc0")

        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(240, 120, 50, 40))
        self.Enter.setAutoRepeat(False)
        self.Enter.setObjectName("Enter")

        self.WDivide = QtWidgets.QPushButton(self.centralwidget)
        self.WDivide.setGeometry(QtCore.QRect(240, 160, 50, 40))
        self.WDivide.setAutoRepeat(False)
        self.WDivide.setObjectName("WDivide")

        self.WMinus = QtWidgets.QPushButton(self.centralwidget)
        self.WMinus.setGeometry(QtCore.QRect(240, 200, 50, 40))
        self.WMinus.setAutoRepeat(False)
        self.WMinus.setObjectName("WMinus")

        self.WCBracket = QtWidgets.QPushButton(self.centralwidget)
        self.WCBracket.setGeometry(QtCore.QRect(240, 240, 50, 40))
        self.WCBracket.setAutoRepeat(False)
        self.WCBracket.setObjectName("WCBracket")

        self.Backspace = QtWidgets.QPushButton(self.centralwidget)
        self.Backspace.setGeometry(QtCore.QRect(190, 120, 50, 40))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.Backspace.setFont(font)
        self.Backspace.setAutoRepeat(False)
        self.Backspace.setObjectName("Backspace")

        self.WMultiply = QtWidgets.QPushButton(self.centralwidget)
        self.WMultiply.setGeometry(QtCore.QRect(190, 160, 50, 40))
        self.WMultiply.setAutoRepeat(False)
        self.WMultiply.setObjectName("WMultiply")

        self.WPlus = QtWidgets.QPushButton(self.centralwidget)
        self.WPlus.setGeometry(QtCore.QRect(190, 200, 50, 40))
        self.WPlus.setAutoRepeat(False)
        self.WPlus.setObjectName("WPlus")

        self.WOBracket = QtWidgets.QPushButton(self.centralwidget)
        self.WOBracket.setGeometry(QtCore.QRect(190, 240, 50, 40))
        self.WOBracket.setAutoRepeat(False)
        self.WOBracket.setObjectName("WOBracket")

        self.CalcDecimal = QtWidgets.QPushButton(self.centralwidget)
        self.CalcDecimal.setGeometry(QtCore.QRect(130, 270, 50, 40))
        self.CalcDecimal.setAutoRepeat(False)
        self.CalcDecimal.setObjectName("CalcDecimal")

        self.WExponent = QtWidgets.QPushButton(self.centralwidget)
        self.WExponent.setGeometry(QtCore.QRect(210, 280, 50, 40))
        self.WExponent.setAutoRepeat(False)
        self.WExponent.setObjectName("WExponent")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.message = ''

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anupam's Calculator"))
        self.CalcScreen.setStatusTip(_translate("MainWindow", "Calculator Screen"))
        self.CalcScreen.setWhatsThis(_translate("MainWindow", "Screen"))

        self.Calc1.setStatusTip(_translate("MainWindow", "Number 1"))
        self.Calc1.setText(_translate("MainWindow", "1"))
        self.Calc1.setShortcut(_translate("MainWindow", "1"))
        self.Calc1.clicked.connect(self.clicked)


        self.Calc2.setStatusTip(_translate("MainWindow", "Number 2"))
        self.Calc2.setText(_translate("MainWindow", "2"))
        self.Calc2.setShortcut(_translate("MainWindow", "2"))
        self.Calc2.clicked.connect(self.clicked)


        self.Calc3.setStatusTip(_translate("MainWindow", "Number 3"))
        self.Calc3.setText(_translate("MainWindow", "3"))
        self.Calc3.setShortcut(_translate("MainWindow", "3"))
        self.Calc3.clicked.connect(self.clicked)


        self.Calc4.setStatusTip(_translate("MainWindow", "Number 4"))
        self.Calc4.setText(_translate("MainWindow", "4"))
        self.Calc4.setShortcut(_translate("MainWindow", "4"))
        self.Calc4.clicked.connect(self.clicked)


        self.Calc5.setStatusTip(_translate("MainWindow", "Number 5"))
        self.Calc5.setText(_translate("MainWindow", "5"))
        self.Calc5.setShortcut(_translate("MainWindow", "5"))
        self.Calc5.clicked.connect(self.clicked)


        self.Calc6.setStatusTip(_translate("MainWindow", "Number 6"))
        self.Calc6.setText(_translate("MainWindow", "6"))
        self.Calc6.setShortcut(_translate("MainWindow", "6"))
        self.Calc6.clicked.connect(self.clicked)


        self.Calc7.setStatusTip(_translate("MainWindow", "Number 7"))
        self.Calc7.setText(_translate("MainWindow", "7"))
        self.Calc7.setShortcut(_translate("MainWindow", "7"))
        self.Calc7.clicked.connect(self.clicked)


        self.Calc8.setStatusTip(_translate("MainWindow", "Number 8"))
        self.Calc8.setText(_translate("MainWindow", "8"))
        self.Calc8.setShortcut(_translate("MainWindow", "8"))
        self.Calc8.clicked.connect(self.clicked)


        self.Calc9.setStatusTip(_translate("MainWindow", "Number 9"))
        self.Calc9.setText(_translate("MainWindow", "9"))
        self.Calc9.setShortcut(_translate("MainWindow", "9"))
        self.Calc9.clicked.connect(self.clicked)


        self.Calc0.setStatusTip(_translate("MainWindow", "Number 0"))
        self.Calc0.setText(_translate("MainWindow", "0"))
        self.Calc0.setShortcut(_translate("MainWindow", "0"))
        self.Calc0.clicked.connect(self.clicked)


        self.Enter.setStatusTip(_translate("MainWindow", "Enter"))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.Enter.clicked.connect(self.Calculate)


        self.Enter.setShortcut(_translate("MainWindow", "Return"))


        self.WDivide.setStatusTip(_translate("MainWindow", "Divide"))
        self.WDivide.setText(_translate("MainWindow", "÷"))
        self.WDivide.clicked.connect(self.clicked)


        self.WDivide.setShortcut(_translate("MainWindow", "/"))
        self.WMinus.setStatusTip(_translate("MainWindow", "Minus"))


        self.WMinus.setText(_translate("MainWindow", "-"))
        self.WMinus.setShortcut(_translate("MainWindow", "-"))
        self.WMinus.clicked.connect(self.clicked)


        self.WCBracket.setStatusTip(_translate("MainWindow", "Closing Bracket"))
        self.WCBracket.setText(_translate("MainWindow", ")"))
        self.WCBracket.setShortcut(_translate("MainWindow", ")"))
        self.WCBracket.clicked.connect(self.clicked)


        self.Backspace.setStatusTip(_translate("MainWindow", "Backspace"))
        self.Backspace.setText(_translate("MainWindow", "Backspace"))
        self.Backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.Backspace.clicked.connect(self.delete)


        self.WMultiply.setStatusTip(_translate("MainWindow", "Multiply"))
        self.WMultiply.setText(_translate("MainWindow", "x"))
        self.WMultiply.setShortcut(_translate("MainWindow", "X"))
        self.WMultiply.clicked.connect(self.clicked)


        self.WPlus.setStatusTip(_translate("MainWindow", "Plus"))
        self.WPlus.setText(_translate("MainWindow", "+"))
        self.WPlus.setShortcut(_translate("MainWindow", "+"))
        self.WPlus.clicked.connect(self.clicked)


        self.WOBracket.setStatusTip(_translate("MainWindow", "Open Bracket"))
        self.WOBracket.setText(_translate("MainWindow", "("))
        self.WOBracket.setShortcut(_translate("MainWindow", "("))
        self.WOBracket.clicked.connect(self.clicked)


        self.CalcDecimal.setStatusTip(_translate("MainWindow", "Decimal"))
        self.CalcDecimal.setText(_translate("MainWindow", "."))
        self.CalcDecimal.setShortcut(_translate("MainWindow", "."))
        self.CalcDecimal.clicked.connect(self.clicked)


        self.WExponent.setStatusTip(_translate("MainWindow", "Exponent"))
        self.WExponent.setText(_translate("MainWindow", "^"))
        self.WExponent.setShortcut(_translate("MainWindow", "^"))
        self.WExponent.clicked.connect(self.clicked)

    def clicked(self):
        sender = self.sender()
        self.message += sender.text()
        self.CalcScreen.setText(self.message)

    def delete(self):
        self.message=self.message[:-1]
        self.CalcScreen.setText(self.message)

    def Calculate(self):
        state = True
        calculation = self.message
        for i, v in enumerate(calculation):  # iterates through the calc string
            if v in ['x', '+', '-', '÷', '^', '(']:  # doing a sign check
                if i + 1 == len(calculation):   # validating that the sign use is legal
                    state = False
                if calculation[i + 1] in valids:
                    state = False
                if calculation[-1] in ['x', '+', '-', '÷', '^','(']:
                        state = False
                if calculation.count('(') != calculation.count(')'):
                    state = False

        if state:
            self.maths()
        else:
            self.CalcScreen.setText("Invalid Input")
            self.message = ''


    def maths(self):
        calculation = '('+ str(self.message)+')'
        for i in range(len(calculation)):
            if (calculation[i]=='(' and calculation[i-1] not in ['x', '+', '-', '÷', '^', '(']) and (i != 0):
                calculation = calculation[:i]+'x'+calculation[i:]
                print(calculation)
        calculation = calculation.replace('x', '*')
        calculation = calculation.replace('÷', '/')
        calculation = calculation.replace('^', '**')

        ans = eval(calculation)
        print(ans)
        self.CalcScreen.setText(str(ans))

        self.message = ''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())