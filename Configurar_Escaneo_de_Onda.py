# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Configurar_Escaneo_de_Onda.ui'
#
# Created: Fri Mar 15 18:44:34 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui;

import serial, MM, LIA, xlwt;

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    N = 0;
    eNd=0;
    Step=0;
    LastPos = 0;
    NumAprom = 0.0;
    j=0;
    SerMon = serial.Serial(0,9600)
    SerMon.cts = True
    SerMon.dtr = True
    SerMon.bytesize = 8
    MM.init(SerMon, 0)
    SerAmp = serial.Serial(2,9600)
    SerAmp.cts = True
    SerAmp.dtr = True
    SerAmp.dce = True
    SerAmp.bytesize = 8
    wb = xlwt.Workbook()
    ws = wb.add_sheet('analisis1')
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(562, 189)
        Dialog.setMinimumSize(QtCore.QSize(562, 189))
        Dialog.setMaximumSize(QtCore.QSize(562, 189))
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 150, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(200, 30, 113, 20))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 60, 113, 20))
        self.lineEdit_2.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 90, 113, 20))
        self.lineEdit_3.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 171, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 120, 113, 20))
        self.lineEdit_4.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 50, 160, 80))
        self.verticalLayoutWidget.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_2 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(350, 20, 171, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(320, 10, 20, 141))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(130, 0, 141, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 140, 531, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(270, 0, 281, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(10, 10, 20, 141))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(20, 0, 101, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(540, 10, 16, 141))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.radioButton_3.setChecked(True)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonClickHandle)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def buttonClickHandle(self):
        try:
            self.N = self.lineEdit.text()
            self.N = float(self.N);
        except (ValueError, TypeError):
            self.N=0;return;
        if self.radioButton_2.isChecked()== True:
            self.N = self.N / 10
            print self.N
        elif self.radioButton.isChecked() == True:
            self.N = self.N * 1000
            print self.N
        if((self.N < 1) or (self.N > 1491)):
            self.N=0;return;
        try:
            self.eNd = self.lineEdit_2.text()
            self.eNd = float(self.eNd);
        except (ValueError, TypeError):
            self.eNd=0;return;
        if self.radioButton_2.isChecked()== True:
            self.eNd = self.eNd / 10
            print self.eNd
        elif self.radioButton.isChecked() == True:
            self.eNd = self.eNd * 1000
            print self.eNd       
        if((self.eNd < 1) or (self.eNd > 1491)):
            self.eNd=0;return;
        try:
            self.Step = self.lineEdit_3.text()
            self.Step = float(self.Step);
        except (ValueError, TypeError):
            self.Step=0;return;
        if self.radioButton_2.isChecked()== True:
            self.Step = self.Step / 10
            print self.Step
        elif self.radioButton.isChecked() == True:
            self.Step = self.Step * 1000
            print self.Step 
        try:
            self.NumAprom = self.lineEdit_4.text()
            self.NumAprom = int(self.NumAprom);
        except (ValueError, TypeError):
            self.NumAprom=0.0;return;     
        self.Ejecuta()
        
            
    def Ejecuta(self):
        self.LastPos = MM.Calcula(self.SerMon,self.N,self.LastPos);
        if self.N < self.eNd:
            while self.N <= self.eNd: 
                self.LastPos = MM.Calcula(self.SerMon, self.N, self.LastPos)
                A = LIA.PromVolt(self.SerAmp, self.NumAprom)
                self.ws.write(self.j, 0, self.N)
                self.ws.write(self.j, 1, A)
                self.N += self.Step
                self.j+=1
                print "EL PASO ACTUAL ES: %f" % self.N
                print "El Promedio es: %f" % A
                print "los microspasos totales son: %d" % self.LastPos;
        elif self.N > self.eNd:
            while self.N >= self.eNd: 
                self.LastPos = MM.Calcula(self.SerMon, self.N, self.LastPos)
                A = LIA.PromVolt(self.SerAmp, self.NumAprom)
                self.ws.write(self.j, 0, self.N)
                self.ws.write(self.j, 1, A)
                self.N -= self.Step
                self.j+=1
                print "EL PASO ACTUAL ES: %f" % self.N
                print "El Promedio es: %f" % A
                print "los microspasos totales son: %d" % self.LastPos;
        else:
            return  
        self.wb.save('test1.xls')
        self.N=0
        self.eNd=0
        self.Step=0
        self.NumAprom=0.0    
            
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configurar Escaneo de Onda", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Longitud de Onda Inicial:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Longitud de Onda Final:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Tamanio de Paso:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Muestras Promedio por Paso:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Dialog", "Angstroms (A)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("Dialog", "Nanometros (nm)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Dialog", "Micrometros (um)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Unidades de Longitud de Onda", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Parametros de escaneo", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    ui.SerMon.close();
    ui.SerAmp.close();

