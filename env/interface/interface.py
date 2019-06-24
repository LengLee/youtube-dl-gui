from PyQt5 import QtCore, uic, QtWidgets, QtGui
import sys, os
from gui2 import Ui_MainWindow

#Creating a UI Class for the main window
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        #Selecting directory to download vids into
        #Since python file already defines and init the UI just set variable to it
        treeview = self.treeView 
        
        #create a model which will be used for the File System Browser
        self.treemodel = QtWidgets.QFileSystemModel()
        self.treemodel.setRootPath('/Users/')

        #Set the Model(FileSystem) to display in your treeview
        treeview.setModel(self.treemodel)
        


        #Connecting the push button for the download
        downloadbutton = self.pushButton
        downloadbutton.clicked.connect(self.push)



    #Select directory function
    def directoryselect(self):
        #file = os.
        return None

    #TODO - Assign variable to static link so it can be dynamic and read from the self.plainTextEdit.toPlainText() function
    def push(self):
        link = str(self.plainTextEdit.toPlainText())
        print(self.plainTextEdit.toPlainText())
        #working cmd
        #os.system("youtube-dl --no-check-certificate -o \"/Users/LengLee/Downloads/%(title)s-%(id)s.%(ext)s\" " + str(link) )
        return None



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())