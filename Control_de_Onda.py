# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Control_de_Onda.ui'
#
# Created: Thu Jan 31 19:30:28 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
import serial, MM, sys;

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    NM = 0;
    LastNM=0;
    LastPos = 0;
    Step=0;
    Ser = serial.Serial(0,9600)
    Ser.cts = True
    Ser.dtr = True
    Ser.bytesize = 8
    MM.init(Ser, 0)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(299, 218)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(170, 10, 91, 31))
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(140, 70, 61, 31))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 160, 41, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 110, 91, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(15, 62, 111, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickHandle)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickHandleLess)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.buttonClickHandleMore)
        QtCore.QMetaObject.connectSlotsByName(Form)      
    #def ErrorMessage(self):
    #    QtGui.QMessageBox.information(self, 'Message Title', 'The Bosy Text',
    #                                   QtGui.MessageBox.No | QtGui.MessageBox.Yes || QtGui.MessageBox.Cancel)
    #    QMessageBox messageBox;
    #    messageBox.critical(0,"Error","ingresa valores enteros o Decimales");
    #    messageBox.setFixedSize(500,200);
        
    def buttonClickHandle(self):
            while type(self.NM)!= float:
                try:
                    self.NM = self.lineEdit.text()
                    self.NM = float(self.NM);
                except (ValueError, TypeError):
                    break;
                        #self.NM = 0
                        #self.lineEdit.clear()
# CORREGIR ERROR LETRAS Y NUMEROS QUITAR BREAK VER ERROR...
                        #break;
            if((self.NM < 1) or (self.NM > 1491)):
                MM.init(self.Ser, 0)
                self.lcdNumber.display(self.LastNM)
                self.lineEdit.clear()
                return 
            self.LastPos = MM.Calcula(self.Ser,self.NM,self.LastPos);
            self.lcdNumber.display(self.NM)
            self.LastNM = self.NM
            self.lineEdit.clear()
            self.NM=0
    def buttonClickHandleMore(self):
        self.Step = self.doubleSpinBox.value()
        self.LastNM += self.Step
        if self.LastNM > 1491:
            MM.init(self.Ser, 0)
            self.LastNM = 0
            self.lcdNumber.display(self.LastNM)
            self.lineEdit.clear()
            return
        self.LastPos = MM.Calcula(self.Ser,self.LastNM,self.LastPos);
        self.lcdNumber.display(self.LastNM)
    def buttonClickHandleLess(self):
        self.Step = self.doubleSpinBox.value()
        self.LastNM -= self.Step
        if self.LastNM < 0:
            MM.init(self.Ser, 0)
            self.LastNM = 0
            self.lcdNumber.display(self.LastNM)
            self.lineEdit.clear()
            return
        self.LastPos = MM.Calcula(self.Ser,self.LastNM,self.LastPos);
        self.lcdNumber.display(self.LastNM)
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Control en Longitud de Onda", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Longitud de Onda Actual(nm):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Ingresa Longitud(nm):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Ir", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "<- Paso Negativo", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Paso Positivo ->", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Tamaño de paso(nm):", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    #para cerrar el puerto una vez cerrado el programa:
    ui.Ser.close();