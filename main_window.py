# -*- coding: utf-8 -*-
QString = str
################################################################################
## Form generated from reading UI file 'sklad.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(664, 513)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 651, 451))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 20, 331, 20))
        self.dateEdit = QDateEdit(self.tab_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(10, 20, 110, 22))
        self.dateEdit.setCurrentSection(QDateTimeEdit.MonthSection)
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(470, 20, 171, 23))
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 80, 171, 23))
        self.checkBox = QCheckBox(self.tab_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 50, 70, 18))
        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(470, 50, 171, 23))
        self.progressBar = QProgressBar(self.tab_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(137, 80, 321, 23))
        self.progressBar.setValue(0)
        self.tabWidget.addTab(self.tab_2, QString())
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 10, 113, 20))
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(270, 10, 113, 20))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 10, 61, 16))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 71, 16))
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QRect(410, 10, 75, 23))
        self.pushButton_3.setCheckable(False)
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 41, 611, 381))
        self.tabWidget.addTab(self.tab, QString())
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 664, 22))
        self.menuSklad = QMenu(self.menubar)
        self.menuSklad.setObjectName(u"menuSklad")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSklad.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u044b \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM.yyyy", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438 \u043f\u0430\u043f\u043a\u0443 \u0441 \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u043f\u0430\u043c\u044f\u0442\u044c", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" \u041a\u043e\u0434 \u043f\u0440\u043e\u0434.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u0441\u043a\u043e\u043f\u0438\u0440\u0443\u0439 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u043f\u0430\u043c\u044f\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430", None))
        self.menuSklad.setTitle(QCoreApplication.translate("MainWindow", u"Sklad", None))
    # retranslateUi

