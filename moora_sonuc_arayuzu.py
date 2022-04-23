# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MLC/Desktop/programs/Design2Py/ui_projects/moora_sonuc_pencere.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Moora_sonuc_penceresi(object):
    def setupUi(self, Moora_sonuc_penceresi):
        Moora_sonuc_penceresi.setObjectName("Moora_sonuc_penceresi")
        Moora_sonuc_penceresi.resize(422, 300)
        Moora_sonuc_penceresi.setMinimumSize(QtCore.QSize(422, 300))
        Moora_sonuc_penceresi.setMaximumSize(QtCore.QSize(422, 16777215))
        Moora_sonuc_penceresi.setBaseSize(QtCore.QSize(422, 300))
        self.centralwidget = QtWidgets.QWidget(Moora_sonuc_penceresi)
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
        self.tableWidget_sonuc_moora = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_sonuc_moora.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_sonuc_moora.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_sonuc_moora.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.tableWidget_sonuc_moora.setFont(font)
        self.tableWidget_sonuc_moora.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableWidget_sonuc_moora.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sonuc_moora.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sonuc_moora.setRowCount(2)
        self.tableWidget_sonuc_moora.setObjectName("tableWidget_sonuc_moora")
        self.tableWidget_sonuc_moora.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_moora.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_moora.setHorizontalHeaderItem(1, item)
        self.tableWidget_sonuc_moora.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_sonuc_moora.horizontalHeader().setMinimumSectionSize(198)
        self.tableWidget_sonuc_moora.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget_sonuc_moora)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        Moora_sonuc_penceresi.setCentralWidget(self.centralwidget)

        self.retranslateUi(Moora_sonuc_penceresi)
        QtCore.QMetaObject.connectSlotsByName(Moora_sonuc_penceresi)

    def retranslateUi(self, Moora_sonuc_penceresi):
        _translate = QtCore.QCoreApplication.translate
        Moora_sonuc_penceresi.setWindowTitle(_translate("Moora_sonuc_penceresi", "MOORA"))
        self.label.setText(_translate("Moora_sonuc_penceresi", "<html><head/><body><p align=\"center\">Sonuçlar</p></body></html>"))
        self.tableWidget_sonuc_moora.setSortingEnabled(True)
        item = self.tableWidget_sonuc_moora.horizontalHeaderItem(0)
        item.setText(_translate("Moora_sonuc_penceresi", "Futbolcular"))
        item = self.tableWidget_sonuc_moora.horizontalHeaderItem(1)
        item.setText(_translate("Moora_sonuc_penceresi", "Alternatiflerin Tüm Kriterlere\n"
"Göre Normalleştirilmiş Hali"))

