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
import time
import cv2
def is_an_image_file(filename):
    IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg']
    for ext in IMAGE_EXTENSIONS:
        if ext in filename:
            return True
    return False
class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.pre = Predict()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 540, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 351, 461))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../data_test/yes/Y1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 101, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 0, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 50, 181, 211))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Gaussian.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 50, 181, 211))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../abcd1.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 310, 181, 211))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../image crop.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 310, 181, 211))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../abcd2.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(900, 10, 71, 17))
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(850, 50, 181, 191))
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setObjectName("textEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 30, 71, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 30, 71, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(480, 290, 41, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(720, 290, 51, 17))
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Image"))
        self.label_2.setText(_translate("MainWindow", "Imag Original"))
        self.label_3.setText(_translate("MainWindow", "Preprocessing"))
        self.label_8.setText(_translate("MainWindow", "Prediction"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Predict Brain Tumor</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Processing Time: 0.12s</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Gaussian"))
        self.label_10.setText(_translate("MainWindow", "Threshold"))
        self.label_11.setText(_translate("MainWindow", "Crop"))
        self.label_12.setText(_translate("MainWindow", "Tumor"))
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
            start = time.time()

            self.process(filename[0])
            process_time = time.time() - start
            print("abcd", process_time)
    def process(self, path):
        pre, time, self.lst_img = self.pre.predict_img(path)
        str_pre = ""
        if pre[0][0] == 1:
            str_pre = "Predict Brain Tumor :" + "\n" + "Processing Time :" + str(round(time, 2)) + "s"
        else:
            str_pre = "Predict No Brain Tumor:" + "\n" + "Processing Time :" + str(round(time, 2)) + "s"
        self.textEdit.setText(str_pre)
        self.show_img()
        # print(filename[0])
    def show_img(self):
        img0 = QtGui.QImage(self.lst_img[0], self.lst_img[0].shape[1], self.lst_img[0].shape[0],QtGui.QImage.Format_Grayscale8)
        pixmap0 = QtGui.QPixmap.fromImage(img0)
        self.label_4.setPixmap(pixmap0)
        self.label_4.setScaledContents(True)

        img1 = QtGui.QImage(self.lst_img[1], self.lst_img[1].shape[1], self.lst_img[1].shape[0],QtGui.QImage.Format_Grayscale8)
        pixmap1 = QtGui.QPixmap.fromImage(img1)
        self.label_5.setPixmap(pixmap1)
        self.label_5.setScaledContents(True)

        img2 = QtGui.QImage(self.lst_img[2], self.lst_img[2].shape[1], self.lst_img[2].shape[0],QtGui.QImage.Format_Grayscale8)
        pixmap2 = QtGui.QPixmap.fromImage(img2)
        self.label_6.setPixmap(pixmap1)
        self.label_6.setScaledContents(True)

        
        # for i in self.lst_img:
        #     cv2.imshow("abcd", i)
        #     cv2.waitKey()
        
        img3 = QtGui.QImage(self.lst_img[3], self.lst_img[3].shape[1], self.lst_img[3].shape[0],QtGui.QImage.Format_Grayscale8)
        pixmap3 = QtGui.QPixmap.fromImage(img3)
        self.label_7.setPixmap(pixmap3)
        self.label_7.setScaledContents(True)
        
        
 
        # self.label5.setPixmap(self.lst_img[1])
        # self.label6.setPixmap(self.lst_img[2])
        # self.label7.setPixmap(self.lst_img[3])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

