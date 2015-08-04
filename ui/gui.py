import sys
from PyQt4 import QtGui

class MainApp:
    
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.label = QtGui.QLabel("Hellow!!!")
        self.label.show()
        self.label.move(1200, 500)

    def change_text(self, new_text):
        self.label.setText(new_text)

if __name__ == "__main__":
    MainApp()