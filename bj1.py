# -*- coding: utf-8 -*-

from pymongo import MongoClient
from PyQt5.QtWidgets import QApplication, QWidget , QVBoxLayout , QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 711, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 40, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 31, 20))
        self.lineEdit.setMaxLength(2)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 40, 54, 12))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 40, 31, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 40, 31, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 40, 41, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 40, 41, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(530, 40, 41, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(590, 40, 41, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(650, 40, 41, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(710, 40, 41, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(770, 40, 41, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(830, 40, 41, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(890, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 70, 381, 731))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(700, 70, 391, 731))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 810, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 10, 54, 12))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 40, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(140, 40, 31, 20))
        self.lineEdit_8.setMaxLength(1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setEnabled(True)
        self.listView.setGeometry(QtCore.QRect(30, 70, 201, 731))
        self.listView.setObjectName("listView")

        self.listModel = QStringListModel()
        listView = QListView()
        self.dds = ['无数据']
        self.listModel.setStringList(self.dds)
        self.listView.setModel(self.listModel)
        self.listView.clicked.connect(self.checkItem)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 810, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(860, 810, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(240, 70, 31, 731))
        self.listView_2.setObjectName("listView_2")

        self.listModel_2 = QStringListModel()
        self.dds_2 = ['无']
        self.listModel_2.setStringList(self.dds_2)
        self.listView_2.setModel(self.listModel_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.repaint)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文本分类"))
        self.pushButton.setText(_translate("MainWindow", "连接"))
        self.pushButton_2.setText(_translate("MainWindow", "下一批"))
        self.lineEdit.setInputMask(_translate("MainWindow", "20"))
        self.lineEdit.setText(_translate("MainWindow", "20"))
        self.label.setText(_translate("MainWindow", "操作："))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "3"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "7"))
        self.pushButton_10.setText(_translate("MainWindow", "8"))
        self.pushButton_11.setText(_translate("MainWindow", "9"))
        self.pushButton_12.setText(_translate("MainWindow", "10"))
        self.label_2.setText(_translate("MainWindow", "文本分类"))
        self.label_3.setText(_translate("MainWindow", "字段名："))
        self.label_4.setText(_translate("MainWindow", "未连接"))
        self.lineEdit_8.setInputMask(_translate("MainWindow", "0"))
        self.lineEdit_8.setText(_translate("MainWindow", "0"))

        self.pushButton.clicked.connect(lambda: self.connect_db())
        self.pushButton_2.clicked.connect(lambda: self.next_page())
        self.lineEdit_8.returnPressed.connect(lambda: self.list_res())
        self.comboBox.activated.connect(lambda: self.list_res())

        self.pushButton_3.clicked.connect(lambda: self.tag_loc(1))
        self.pushButton_4.clicked.connect(lambda: self.tag_loc(2))
        self.pushButton_5.clicked.connect(lambda: self.tag_loc(3))
        self.pushButton_6.clicked.connect(lambda: self.tag_loc(4))
        self.pushButton_7.clicked.connect(lambda: self.tag_loc(5))
        self.pushButton_8.clicked.connect(lambda: self.tag_loc(6))
        self.pushButton_9.clicked.connect(lambda: self.tag_loc(7))
        self.pushButton_10.clicked.connect(lambda: self.tag_loc(8))
        self.pushButton_11.clicked.connect(lambda: self.tag_loc(9))
        self.pushButton_12.clicked.connect(lambda: self.tag_loc(10))

        self.iid = ''

    # 下一页
    def next_page(self):
        print('next')
        page = self.lineEdit_8.text()
        num = self.lineEdit.text()
        res = self.conn[str(self.db)][self.col].find().skip((int(page) + 1) * int(num)).limit(int(num))
        self.dds = []
        self.dds_2 = []
        tag = self.comboBox.currentText()
        for r1 in res:
            self.dds.append(str(r1[tag]))
            if 'tag' in r1:
                self.dds_2.append(str(r1['tag']))
            else:
                self.dds_2.append('无')

        self.listModel.setStringList(self.dds)
        self.listView.setModel(self.listModel)

        self.listModel_2.setStringList(self.dds_2)
        self.listView_2.setModel(self.listModel_2)

        self.lineEdit_8.setText(str(int(page) + 1))

    def connect_db(self):
        print('hello')
        ip = self.lineEdit_4.text()
        port = self.lineEdit_5.text()

        # self.db = self.lineEdit_6.text()
        self.db = 'jinrongjie'
        # self.col = self.lineEdit_7.text()
        self.col = 'gupiao_companys_name_copy'

        # self.conn = MongoClient(ip, int(port))
        self.conn = MongoClient('127.0.0.1', 27017)
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("MainWindow", "已连接"))
        self.list_res()

    # 列出数据库中结果
    def list_res(self):
        print('hello2')
        page = self.lineEdit_8.text()
        num = self.lineEdit.text()
        res = self.conn[str(self.db)][self.col].find().skip(int(page) * int(num)).limit(int(num))
        cols = []
        if self.comboBox.currentText() != '':
            key = self.comboBox.currentText()
        else:
            key = '_id'
        ss = []
        self.dds = []
        self.dds_2 = []
        for r1 in res:
            cols = list(r1.keys())
            self.dds.append(str(r1[key]))
            if 'tag' in r1:
                self.dds_2.append(str(r1['tag']))
            else:
                self.dds_2.append('无')
            # self.listView.addItem(r1['_id'])
        if key == '_id':
            self.comboBox.clear()
            self.comboBox_2.clear()
            self.comboBox_3.clear()
            self.comboBox.addItems(cols)
            self.comboBox_2.addItems(cols)
            self.comboBox_3.addItems(cols)
        self.listModel.setStringList(self.dds)
        self.listView.setModel(self.listModel)
        self.listModel_2.setStringList(self.dds_2)
        self.listView_2.setModel(self.listModel_2)

    def checkItem(self, index):
        # QMessageBox.information(self, "ListView", "选择项是：%d" % (index.row()))
        page = self.lineEdit_8.text()
        num = self.lineEdit.text()
        ind = int(page) * int(num) + index.row()
        res = self.conn[str(self.db)][self.col].find().skip(ind).limit(1)
        for r1 in res:
            key1 = self.comboBox_2.currentText()
            self.textBrowser.setText(str(r1[str(key1)]))
            key2 = self.comboBox_3.currentText()
            self.textBrowser_2.setText(str(r1[str(key2)]))
            self.iid = r1['_id']

    # 保存标记到指定位置
    def tag_loc(self, i=0):
        if self.iid == '':
            QMessageBox.information(self, " ", "还没选择项")
        else:
            self.conn[str(self.db)][self.col].update({'_id': self.iid}, {'$set': {'tag': i}})

