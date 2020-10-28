# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\parameters.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_parametersWindow(object):
    def setupUi(self, parametersWindow):
        parametersWindow.setObjectName("parametersWindow")
        parametersWindow.resize(390, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(parametersWindow.sizePolicy().hasHeightForWidth())
        parametersWindow.setSizePolicy(sizePolicy)
        parametersWindow.setMinimumSize(QtCore.QSize(390, 290))
        parametersWindow.setMaximumSize(QtCore.QSize(390, 290))
        parametersWindow.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(parametersWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(parametersWindow)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_button = QtWidgets.QPushButton(parametersWindow)
        self.reset_button.setMinimumSize(QtCore.QSize(0, 20))
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)
        self.confirm_button = QtWidgets.QPushButton(parametersWindow)
        self.confirm_button.setMinimumSize(QtCore.QSize(0, 20))
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout.addWidget(self.confirm_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(parametersWindow)
        QtCore.QMetaObject.connectSlotsByName(parametersWindow)

    def retranslateUi(self, parametersWindow):
        _translate = QtCore.QCoreApplication.translate
        parametersWindow.setWindowTitle(_translate("parametersWindow", "Parameters"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("parametersWindow", "Lower Rate Limit"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("parametersWindow", "Upper Rate Limit"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("parametersWindow", "Atrial Amplitude"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("parametersWindow", "Atrial Pulse Width"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("parametersWindow", "Ventricular Amplitude"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("parametersWindow", "Ventricular Pulse Width"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("parametersWindow", "VRP"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("parametersWindow", "ARP"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("parametersWindow", "Values"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.reset_button.setText(_translate("parametersWindow", "Reset to defaults"))
        self.confirm_button.setText(_translate("parametersWindow", "Confirm changes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    parametersWindow = QtWidgets.QDialog()
    ui = Ui_parametersWindow()
    ui.setupUi(parametersWindow)
    parametersWindow.show()
    sys.exit(app.exec_())
