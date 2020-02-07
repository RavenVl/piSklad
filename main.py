import sys
import os
import pickle
import dataset
from dbfread import DBF
from shutil import copy
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile
from main_window import Ui_MainWindow
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QTableWidgetItem
db = dataset.connect('sqlite:///:memory:')
table = db['sklad']

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conf = {}
        file = open("data\\nastr", 'rb')
        self.conf = pickle.load(file)

        file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    if len(window.conf) > 0:
        window.ui.lineEdit.setText(window.conf["dir"])
        window.ui.checkBox.setChecked(window.conf["svod"])
        window.ui.dateEdit.setDate(window.conf["period"])
    window.show()


    # logik

    def selectFile():
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        window.conf["dir"] = QFileDialog.getExistingDirectory()
        window.ui.lineEdit.setText(window.conf["dir"])
        file = open("data\\nastr", 'wb')
        pickle.dump(window.conf, file)
        file.close()

    def writeNastr():
        window.conf["period"] = window.ui.dateEdit.date()
        window.conf["svod"] = window.ui.checkBox.isChecked()
        dat = window.ui.dateEdit.text()[1] + window.ui.dateEdit.text()[-2:]
        fileName = "sklad{0}.dbf".format(dat)
        # src = os.path.join(*window.conf["dir"].split("/"), fileName)
        src = window.conf["dir"].replace("/", "\\") + "\\" + fileName
        print(src)
        window.conf["src"] = src
        file = open("data\\nastr", 'wb')
        pickle.dump(window.conf, file)
        file.close()
        # copy(src, "data")


    def copyDataMem():
        # pathDBF = "e:\\KS\\basehdm\\sklad414.dbf"
        pathDBF = window.conf["src"]

        for record in DBF(pathDBF, lowernames=True):
            table.insert(record)
        print(len(table))

    def showResult():
        kodpolu = window.ui.lineEdit_3.text()
        kodpr = window.ui.lineEdit_2.text()
        all_rez = table.find(kodpr=kodpr, kodpl=kodpolu)
        n_row = len(list(all_rez))
        for rec in all_rez:
            print(rec)
        # rez_print = ["Дата               Номер док.    Получатель                        Товар                                          Цена  "]
        window.ui.tableWidget.setColumnCount(5)
        window.ui.tableWidget.setRowCount(n_row)
        window.ui.tableWidget.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3", "$", "5"])
        window.ui.tableWidget.setItem(0, 0, QTableWidgetItem("1"))
        i = 0
        for rec in all_rez:
            print(rec)
            window.ui.tableWidget.setItem(i, 0, QTableWidgetItem("1"))
            window.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(i)))
            window.ui.tableWidget.setItem(i, 2, QTableWidgetItem(rec["naim"]))
            window.ui.tableWidget.setItem(i, 3, QTableWidgetItem(rec["tovar"]))
            window.ui.tableWidget.setItem(i, 4, QTableWidgetItem(str(rec["cena"])))
            i += 1

    window.ui.pushButton.clicked.connect(selectFile)
    window.ui.pushButton_4.clicked.connect(writeNastr)
    window.ui.pushButton_4.clicked.connect(writeNastr)
    window.ui.pushButton_2.clicked.connect(copyDataMem)
    window.ui.pushButton_3.clicked.connect(showResult)

    sys.exit(app.exec_())
