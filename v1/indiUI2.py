# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'indi2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1194, 901)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 420, 591, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2_3.setGeometry(QtCore.QRect(270, 40, 113, 20))
        self.lineEdit_2_3.setObjectName("lineEdit_2_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2_2.setGeometry(QtCore.QRect(150, 40, 113, 20))
        self.lineEdit_2_2.setObjectName("lineEdit_2_2")
        self.lineEdit_2_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2_1.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.lineEdit_2_1.setObjectName("lineEdit_2_1")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_2.setGeometry(QtCore.QRect(150, 90, 211, 31))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 111, 16))
        self.label_2.setObjectName("label_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 150, 531, 221))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(690, 420, 451, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_3_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3_2.setGeometry(QtCore.QRect(150, 40, 113, 20))
        self.lineEdit_3_2.setObjectName("lineEdit_3_2")
        self.lineEdit_3_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3_1.setGeometry(QtCore.QRect(30, 40, 113, 20))
        self.lineEdit_3_1.setObjectName("lineEdit_3_1")
        self.lineEdit_3_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3_4.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.lineEdit_3_4.setObjectName("lineEdit_3_4")
        self.lineEdit_3_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3_5.setGeometry(QtCore.QRect(270, 70, 113, 20))
        self.lineEdit_3_5.setObjectName("lineEdit_3_5")
        self.pushButton_3_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3_2.setGeometry(QtCore.QRect(110, 130, 75, 23))
        self.pushButton_3_2.setObjectName("pushButton_3_2")
        self.pushButton_3_1 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3_1.setGeometry(QtCore.QRect(30, 130, 75, 23))
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.lineEdit_3_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3_3.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.lineEdit_3_3.setObjectName("lineEdit_3_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 50, 591, 341))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 211, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, 531, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(690, 630, 451, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_4.setGeometry(QtCore.QRect(30, 30, 381, 131))
        self.listWidget_4.setObjectName("listWidget_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(690, 50, 451, 341))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_5_1 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5_1.setGeometry(QtCore.QRect(160, 30, 75, 23))
        self.pushButton_5_1.setObjectName("pushButton_5_1")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_5.setGeometry(QtCore.QRect(30, 70, 391, 241))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.pushButton_5_2 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5_2.setGeometry(QtCore.QRect(240, 30, 75, 23))
        self.pushButton_5_2.setObjectName("pushButton_5_2")
        self.lineEdit_2_4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_2_4.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit_2_4.setObjectName("lineEdit_2_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1194, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "나의 투자 분석"))
        self.lineEdit_2_3.setText(_translate("MainWindow", "목표 수익 (원)"))
        self.pushButton_2.setText(_translate("MainWindow", "조회"))
        self.lineEdit_2_2.setText(_translate("MainWindow", "계좌 비밀번호"))
        self.lineEdit_2_1.setText(_translate("MainWindow", "계좌번호"))
        self.label_2.setText(_translate("MainWindow", "목표 수익 달성률"))
        self.groupBox_3.setTitle(_translate("MainWindow", "주문"))
        self.lineEdit_3_2.setText(_translate("MainWindow", "계좌 비밀번호"))
        self.lineEdit_3_1.setText(_translate("MainWindow", "계좌번호"))
        self.lineEdit_3_4.setText(_translate("MainWindow", "주문수량"))
        self.lineEdit_3_5.setText(_translate("MainWindow", "주문가격"))
        self.pushButton_3_2.setText(_translate("MainWindow", "매도"))
        self.pushButton_3_1.setText(_translate("MainWindow", "매수"))
        self.lineEdit_3_3.setText(_translate("MainWindow", "종목코드"))
        self.groupBox.setTitle(_translate("MainWindow", "오늘의 종목"))
        self.label.setText(_translate("MainWindow", "추천 종목을 조회해보세요."))
        self.pushButton.setText(_translate("MainWindow", "조회"))
        self.groupBox_4.setTitle(_translate("MainWindow", "알림창"))
        self.groupBox_5.setTitle(_translate("MainWindow", "시세 조회"))
        self.pushButton_5_1.setText(_translate("MainWindow", "조회"))
        self.pushButton_5_2.setText(_translate("MainWindow", "중지"))
        self.lineEdit_2_4.setText(_translate("MainWindow", "종목코드"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())