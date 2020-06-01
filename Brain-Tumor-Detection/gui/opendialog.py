# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opendiablog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from predict import Predict
from tensorflow.keras.models import load_model
import tensorflow as tf

def is_an_image_file(filename):
    IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg']
    for ext in IMAGE_EXTENSIONS:
        if ext in filename:
            return True
    return False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 450, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../brain_tumor_dataset/yes/Y1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.best_model = load_model(filepath='/home/minhhoang/Brain_tumor/Brain-Tumor-Detection/models/cnn-parameters-improvement-23-0.91.model')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Folder"))
        self.pushButton.clicked.connect(self.pushButton_handler)
    def pushButton_handler(self):
        self.open_diablog_box()

    def open_diablog_box(self):
        check = False
        filename = QtWidgets.QFileDialog.getOpenFileName()
        if is_an_image_file(filename[0]):
            self.label.setPixmap(QtGui.QPixmap(filename[0]))
            check = True
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Please open file .jpg .png .jpeg !!!")
            msg.setWindowTitle("Erro!!!")
            msg.exec_()


        if check:
            pre = Predict()
            pre, time = pre.predict_img(filename[0], self.best_model)
            print(pre)
            print(time)
        # print(filename[0])
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

