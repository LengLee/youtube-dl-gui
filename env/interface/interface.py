from PyQt5 import QtCore, uic, QtWidgets, QtGui
import sys, os
from gui import Ui_MainWindow

#Creating a UI Class for the main window
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        #Connecting the push button for the download
        dbutton = self.pushButton
        dbutton.clicked.connect(self.push)
    
    #Once click, download static Elton John Link
    #TODO - Assign variable to static link so it can be dynamic and read from the self.plainTextEdit.toPlainText() function
    def push(self):
        print(self.plainTextEdit.toPlainText())
        os.system("sudo youtube-dl --no-check-certificate -o \"/Users/LengLee/Downloads/%(title)s-%(id)s.%(ext)s\" https://youtu.be/1sioip9Uc4o\\")
        return None



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())