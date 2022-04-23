# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MLC/Desktop/programs/Design2Py/ui_projects/vikor_sonuc_pencere.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Vikor_Sonuc_Penceresi(object):
    def setupUi(self, Vikor_Sonuc_Penceresi):
        Vikor_Sonuc_Penceresi.setObjectName("Vikor_Sonuc_Penceresi")
        Vikor_Sonuc_Penceresi.resize(850, 300)
        Vikor_Sonuc_Penceresi.setMinimumSize(QtCore.QSize(850, 300))
        Vikor_Sonuc_Penceresi.setMaximumSize(QtCore.QSize(850, 16777215))
        Vikor_Sonuc_Penceresi.setBaseSize(QtCore.QSize(850, 300))
        self.centralwidget = QtWidgets.QWidget(Vikor_Sonuc_Penceresi)
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
        self.tableWidget_sonuc_vikor = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_sonuc_vikor.sizePolicy().hasHeightForWidth())
        self.tableWidget_sonuc_vikor.setSizePolicy(sizePolicy)
        self.tableWidget_sonuc_vikor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.tableWidget_sonuc_vikor.setFont(font)
        self.tableWidget_sonuc_vikor.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableWidget_sonuc_vikor.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sonuc_vikor.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sonuc_vikor.setRowCount(2)
        self.tableWidget_sonuc_vikor.setObjectName("tableWidget_sonuc_vikor")
        self.tableWidget_sonuc_vikor.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_vikor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.tableWidget_sonuc_vikor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_vikor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_vikor.setHorizontalHeaderItem(3, item)
        self.tableWidget_sonuc_vikor.horizontalHeader().setDefaultSectionSize(210)
        self.tableWidget_sonuc_vikor.horizontalHeader().setMinimumSectionSize(70)
        self.tableWidget_sonuc_vikor.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget_sonuc_vikor)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        Vikor_Sonuc_Penceresi.setCentralWidget(self.centralwidget)

        self.retranslateUi(Vikor_Sonuc_Penceresi)
        QtCore.QMetaObject.connectSlotsByName(Vikor_Sonuc_Penceresi)

    def retranslateUi(self, Vikor_Sonuc_Penceresi):
        _translate = QtCore.QCoreApplication.translate
        Vikor_Sonuc_Penceresi.setWindowTitle(_translate("Vikor_Sonuc_Penceresi", "VIKOR"))
        self.label.setText(_translate("Vikor_Sonuc_Penceresi", "<html><head/><body><p align=\"center\">Sonuçlar</p></body></html>"))
        self.tableWidget_sonuc_vikor.setSortingEnabled(True)
        item = self.tableWidget_sonuc_vikor.horizontalHeaderItem(0)
        item.setText(_translate("Vikor_Sonuc_Penceresi", "Futbolcular"))
        item = self.tableWidget_sonuc_vikor.horizontalHeaderItem(1)
        item.setText(_translate("Vikor_Sonuc_Penceresi", "Alternatifler İçin Ortalama Grup\n"
"Skoru"))
        item = self.tableWidget_sonuc_vikor.horizontalHeaderItem(2)
        item.setText(_translate("Vikor_Sonuc_Penceresi", "Alternatifler İçin En Kötü Grup Skoru"))
        item = self.tableWidget_sonuc_vikor.horizontalHeaderItem(3)
        item.setText(_translate("Vikor_Sonuc_Penceresi", "Alternatifler İçin Nihai Skor"))

