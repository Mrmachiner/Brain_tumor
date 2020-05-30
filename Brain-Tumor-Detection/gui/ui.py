from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Brain-Tumor_Detection-App")


    label1 = QtWidgets.QLabel(win)
    label1.setText("first label")
    label1.move(50, 50)
    win.show()
    sys.exit(app.exec_())

window()