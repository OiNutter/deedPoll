#!c:\Python31\python.exe
#Filename: deedPoll.py

#import gui libraries
from PyQt4 import QtCore, QtGui, uic

import os
import sys
import string

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
		
		#set class variables
		self.origFile = ""
		
		#set button events
		self.connect(self.browseButton,QtCore.SIGNAL('clicked()'),self.showFileDialog)
		self.connect(self.renameButton,QtCore.SIGNAL('clicked()'),self.renameFile)
			
	#show dialog to select initial file	
	def showFileDialog(self):
		#fileDialog = QtGui.QFileDialog(self)
		#fileDialog.setFileMode(QtGui.QFileDialog.ExistingFile)
		#file
		self.origFile = QtGui.QFileDialog.getOpenFileName(self,'Select File',"/")
		self.fileInput.setText(os.path.basename(self.origFile))
		
	#perform rename operation
	def renameFile(self):
		os.rename(self.origFile,os.path.dirname(self.origFile) + "/" + self.newName.text())
		
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())