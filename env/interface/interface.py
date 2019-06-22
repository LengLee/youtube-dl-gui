from PyQt5 import QtCore, uic, QtWidgets, QtGui
import sys
from gui import Ui_MainWindow

#Creating a UI Class for the main window
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        #Connecting the push button for the download
        dbutton = self.pushButton
        dbutton.clicked.connect(self.push)
    
    #Clicked Test button
    def push(self):
        print(self.plainTextEdit.toPlainText())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())