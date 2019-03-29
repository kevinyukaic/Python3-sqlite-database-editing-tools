import sqlite3

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
		QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
		QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
		QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
		QVBoxLayout, QWidget,QTableWidgetItem)


class WidgetGallery(QDialog):
	def __init__(self, parent=None):
		super(WidgetGallery, self).__init__(parent,\
			flags=Qt.WindowMinimizeButtonHint|Qt.WindowMaximizeButtonHint | Qt.WindowCloseButtonHint)


		self.originalPalette = QApplication.palette()

		AppComboBox = QComboBox()
		AppComboBox.addItems(["Message","Bank","Email","News"])

		AppLabel = QLabel("&Application:")
		AppLabel.setBuddy(AppComboBox)

		self.tableWidget = QTableWidget(10, 10)
		self.tableWidget.doubleClicked.connect(self.on_click)
		self.textEdit = QTextEdit()
		self.createTopLeftGroupBox(self.tableWidget)
		self.createTopRightGroupBox()

		self.DisplayData()
		self.loadDBData()



		topLayout = QHBoxLayout()
		topLayout.addWidget(AppLabel)
		topLayout.addWidget(AppComboBox)
		topLayout.addStretch(1)

		mainLayout = QGridLayout()
		mainLayout.addLayout(topLayout, 0, 0, 1, 2)
		mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
		mainLayout.addWidget(self.topRightGroupBox, 1, 1)

		#mainLayout.setRowStretch(1, 1)
		#mainLayout.setRowStretch(2, 1)
		mainLayout.setColumnStretch(0, 1)
		mainLayout.setColumnStretch(1, 1)
		self.setLayout(mainLayout)

		self.setWindowTitle("Fortitude Database Editing Tool")
		#self.changeStyle('Windows')



	def createTopLeftGroupBox(self, tableWidget):

		self.topLeftGroupBox = QTabWidget()
		self.topLeftGroupBox.setSizePolicy(QSizePolicy.Preferred,
				QSizePolicy.Ignored)

		tableWidget.setHorizontalHeaderLabels(["Cluster","ID","APP","Speaker","Content","Next","Summary","BankImpact","RelationshipID","RelationshipImpact"])
		tab1 = QWidget()
		

		tab1hbox = QHBoxLayout()
		tab1hbox.setContentsMargins(5, 5, 5, 5)
		tab1hbox.addWidget(tableWidget)
		tab1.setLayout(tab1hbox)

		self.topLeftGroupBox.addTab(tab1, "&Table")

	def createTopRightGroupBox(self):
		self.topRightGroupBox = QGroupBox("Text Editor")

		defaultPushButton = QPushButton("Apply")
		defaultPushButton.setDefault(True)

		layout = QVBoxLayout()
		


		

		self.textEdit.setPlainText("Twinkle, twinkle, little star,\n"
							  "How I wonder what you are.\n" 
							  "Up above the world so high,\n"
							  "Like a diamond in the sky.\n"
							  "Twinkle, twinkle, little star,\n" 
							  "How I wonder what you are!\n")
		layout.addWidget(self.textEdit)
		layout.addStretch(1)
		layout.addWidget(defaultPushButton)
		self.topRightGroupBox.setLayout(layout)

	def DisplayData(self):
		self.tableWidget.setItem(1,1,QTableWidgetItem("Test"))

	def on_click(self):
		print("\n")
		for currentQTableWidgetItem in self.tableWidget.selectedItems():
			print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
			self.textEdit.setPlainText(currentQTableWidgetItem.text())
 

	def loadDBData(self):
		conn = sqlite3.connect("Fortitude_db")
		c = conn.cursor()
		rowCount =0
		for row in c.execute('SELECT * FROM Text ORDER BY ID'):

			for i in range(len(row)):
				
				self.tableWidget.setItem(rowCount,i+1,QTableWidgetItem(str(row[i])))
			rowCount+=1
			print(row)

def createUI():
	
	app = QApplication(sys.argv)
	app.setStyle('Fusion')
	gallery = WidgetGallery()
	gallery.show()
	sys.exit(app.exec_()) 

	



	



if __name__ == '__main__':
	import sys
	#loadDBData()
	createUI()
	