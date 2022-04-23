# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/MLC/Desktop/programs/Design2Py/ui_projects/topsis_sonuc_pencere.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Topsis_sonuc_penceresi(object):
    def setupUi(self, Topsis_sonuc_penceresi):
        Topsis_sonuc_penceresi.setObjectName("Topsis_sonuc_penceresi")
        Topsis_sonuc_penceresi.resize(600, 280)
        Topsis_sonuc_penceresi.setMinimumSize(QtCore.QSize(600, 280))
        Topsis_sonuc_penceresi.setMaximumSize(QtCore.QSize(600, 16777215))
        Topsis_sonuc_penceresi.setBaseSize(QtCore.QSize(600, 280))
        self.centralwidget = QtWidgets.QWidget(Topsis_sonuc_penceresi)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 68))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget_sonuc_topsis = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.tableWidget_sonuc_topsis.setFont(font)
        self.tableWidget_sonuc_topsis.setFrameShape(QtWidgets.QFrame.VLine)
        self.tableWidget_sonuc_topsis.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_sonuc_topsis.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sonuc_topsis.setRowCount(2)
        self.tableWidget_sonuc_topsis.setObjectName("tableWidget_sonuc_topsis")
        self.tableWidget_sonuc_topsis.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_topsis.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sonuc_topsis.setHorizontalHeaderItem(1, item)
        self.tableWidget_sonuc_topsis.horizontalHeader().setDefaultSectionSize(290)
        self.tableWidget_sonuc_topsis.horizontalHeader().setMinimumSectionSize(290)
        self.tableWidget_sonuc_topsis.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_sonuc_topsis.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget_sonuc_topsis)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        Topsis_sonuc_penceresi.setCentralWidget(self.centralwidget)

        self.retranslateUi(Topsis_sonuc_penceresi)
        QtCore.QMetaObject.connectSlotsByName(Topsis_sonuc_penceresi)

    def retranslateUi(self, Topsis_sonuc_penceresi):
        _translate = QtCore.QCoreApplication.translate
        Topsis_sonuc_penceresi.setWindowTitle(_translate("Topsis_sonuc_penceresi", "TOPSIS"))
        self.label.setText(_translate("Topsis_sonuc_penceresi", "<html><head/><body><p align=\"center\">Sonuçlar</p></body></html>"))
        self.tableWidget_sonuc_topsis.setSortingEnabled(True)
        item = self.tableWidget_sonuc_topsis.horizontalHeaderItem(0)
        item.setText(_translate("Topsis_sonuc_penceresi", "Futbolcular"))
        item = self.tableWidget_sonuc_topsis.horizontalHeaderItem(1)
        item.setText(_translate("Topsis_sonuc_penceresi", "İdeal Çözüme Göreli Yakınlık Katsayıları"))

