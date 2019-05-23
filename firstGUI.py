# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstGUI.py'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets
# from bj1 import Ui_MainWindow
from xulie import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setupUi(self)
        # self.actionOpen.triggered.connect(self.openMsg)

    def openMsg(self):
        file,ok = QFileDialog.getOpenFileName(self,"dakai","C:/","ALL FILES(*)")
        self.statusbar.showMessage(file)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
