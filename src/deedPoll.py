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
		
		#set class variables
		self.origFile = ""
		
		#set button events
		self.connect(self.browseButton,QtCore.SIGNAL('clicked()'),self.showFileDialog)
		self.connect(self.renameButton,QtCore.SIGNAL('clicked()'),self.renameFile)
		self.connect(self.newName,QtCore.SIGNAL('textEdited(QString)'),self.updatePreview)
			
	#show dialog to select initial file	
	def showFileDialog(self):
		self.origFile = QtGui.QFileDialog.getOpenFileName(self,'Select File',"/")
		self.fileInput.setText(os.path.basename(self.origFile))
		self.addPreviewRows()
		
	#perform rename operation
	def renameFile(self):
		os.rename(self.origFile,os.path.dirname(self.origFile) + "/" + self.newName.text())
		
	def addPreviewRows(self):
		self.previewList.insertRow(0)
		item = QtGui.QTableWidgetItem()
		item.setText(os.path.basename(self.origFile))
		newItem = QtGui.QTableWidgetItem()
		newItem.setText(item.text())
		self.previewList.setItem(0,0,item)
		self.previewList.setItem(0,1,newItem)
		
	def updatePreview(self):
		for row in range(0,self.previewList.rowCount()):
			newItem = self.previewList.item(row,1)
			newItem.setText(self.newName.text())
		
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())