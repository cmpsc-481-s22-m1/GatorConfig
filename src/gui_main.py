import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.homepage import Homepage


# from Form import Form
# from Homepage import Homepage

class Gui:
    def __init__(self):
        # Create App
        app = QApplication(sys.argv)

        # Open the qss styles file and read
        # with open('./style.qss', 'r') as f:
        #     style = f.read()
        #
        #     # Set the stylesheet of the application
        #     app.setStyleSheet(style)
        # print(QStyleFactory.keys())

        # Make it look not as bad...
        # app.setStyle()

        # Show Window
        win = Homepage()
        win.setGeometry(400, 400, 400, 300)

        win.show()
        sys.exit(app.exec_())


gui = Gui()
