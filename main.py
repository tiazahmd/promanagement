from PyQt5 import QtGui, QtCore, QtWidgets
import sys, os, psutil
import design, modules

class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.updateUi()
        self.btnKill.clicked.connect(self.kill_process)
        self.btnExit.clicked.connect(self.exit_program)

    def updateUi(self):
        extracted_tupple = modules.extract_all()
        self.tableWidget.setRowCount(extracted_tupple[3])
        for i in range(0, extracted_tupple[3]):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = self.tableWidget.item(i, 0)
            item.setText(str(extracted_tupple[0][i]))

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            item = self.tableWidget.item(i, 1)
            item.setText(str(extracted_tupple[1][i]))

            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(i, 2, item)
            item = self.tableWidget.item(i, 2)
            item.setText(str(extracted_tupple[2][i]))
        
    def kill_process(self):
        r = self.tableWidget.currentRow() # select the row
        # get the text on the selected row:
        current_pid = int(self.tableWidget.item(r,0).text())
        p = psutil.Process(current_pid) # connect to psutil
        p.kill()
        self.updateUi()
        

    def exit_program(self):
        # correct way to quit qt app instance
        self.close()

def main():
    app = QtWidgets.QApplication(sys.argv)
    proman = MainApp()
    proman.show()
    app.exec_()

if __name__ == "__main__":
    main()