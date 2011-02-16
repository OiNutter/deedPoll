#!c:\Python31\python.exe
#Filename: deedPoll.py

#import gui libraries
from PyQt4 import QtCore, QtGui, uic

import os
import sys

#for arg in sys.argv:
#	print(arg)

#target = sys.argv[1]
#name = sys.argv[2]

#os.rename(target,name);


class MainWindow(QtGui.QMainWindow):

	def __init__(self,parent=None):
		super(MainWindow,self).__init__(parent)
		QtGui.QMainWindow.__init__(self)
		self.ui = uic.loadUi('main.ui', self)
		
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())