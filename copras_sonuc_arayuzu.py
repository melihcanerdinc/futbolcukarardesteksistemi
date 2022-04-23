# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MLC/Desktop/programs/Design2Py/ui_projects/copras_sonuc_pencere.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Copras_sonuc_penceresi(object):
    def setupUi(self, Copras_sonuc_penceresi):
        Copras_sonuc_penceresi.setObjectName("Copras_sonuc_penceresi")
        Copras_sonuc_penceresi.resize(620, 310)
        Copras_sonuc_penceresi.setMinimumSize(QtCore.QSize(620, 310))
        Copras_sonuc_penceresi.setMaximumSize(QtCore.QSize(620, 16777215))
        Copras_sonuc_penceresi.setBaseSize(QtCore.QSize(620, 310))
        self.centralwidget = QtWidgets.QWidget(Copras_sonuc_penceresi)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget_sonuc_copras = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.tableWidget_sonuc_copras.setFont(font)
        self.tableWidget_sonuc_copras.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableWidget_sonuc_copras.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sonuc_copras.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sonuc_copras.setRowCount(2)
        self.tableWidget_sonuc_copras.setObjectName("tableWidget_sonuc_copras")
        self.tableWidget_sonuc_copras.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_copras.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_copras.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_copras.setHorizontalHeaderItem(2, item)
        self.tableWidget_sonuc_copras.horizontalHeader().setDefaultSectionSize(199)
        self.tableWidget_sonuc_copras.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget_sonuc_copras.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_sonuc_copras.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget_sonuc_copras)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        Copras_sonuc_penceresi.setCentralWidget(self.centralwidget)

        self.retranslateUi(Copras_sonuc_penceresi)
        QtCore.QMetaObject.connectSlotsByName(Copras_sonuc_penceresi)

    def retranslateUi(self, Copras_sonuc_penceresi):
        _translate = QtCore.QCoreApplication.translate
        Copras_sonuc_penceresi.setWindowTitle(_translate("Copras_sonuc_penceresi", "COPRAS"))
        self.label.setText(_translate("Copras_sonuc_penceresi", "<html><head/><body><p align=\"center\">Sonuçlar</p></body></html>"))
        self.tableWidget_sonuc_copras.setSortingEnabled(True)
        item = self.tableWidget_sonuc_copras.horizontalHeaderItem(0)
        item.setText(_translate("Copras_sonuc_penceresi", "Futbolcular"))
        item = self.tableWidget_sonuc_copras.horizontalHeaderItem(1)
        item.setText(_translate("Copras_sonuc_penceresi", "Alternatiflerin Göreli Önemleri"))
        item = self.tableWidget_sonuc_copras.horizontalHeaderItem(2)
        item.setText(_translate("Copras_sonuc_penceresi", "Alternatiflerin Fayda Oranları"))

