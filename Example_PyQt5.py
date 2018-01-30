import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets


qtDesignerFile = "PyQt_GUI.ui" # GUI layout file.
Ui_MainWindow, QtBaseClass = uic.loadUiType( qtDesignerFile )


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	# Create signals here
	signal_to_emit = QtCore.pyqtSignal(str)
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

		# Can only connect functions after previous things are initialized
		self.my_pushButton.pressed.connect( lambda : self.signal_to_emit.emit( "You pushed the button" ) )
		self.signal_to_emit.connect( self.Pop_Up_Message )

	def Pop_Up_Message( self, message ):
		error = QtWidgets.QMessageBox()
		error.setIcon( QtWidgets.QMessageBox.Critical )
		error.setText( message )
		error.setWindowTitle( "Good Job" )
		error.exec_()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())

