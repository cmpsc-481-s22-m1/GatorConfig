"""A GUI to easily create GatorYAML configuration dictionaries"""
import sys

from PyQt5.QtWidgets import QApplication

from src.gui.homepage import Homepage


# from Form import Form
# from Homepage import Homepage

class Gui:
    """Main GUI object"""

    def __init__(self):
        """Initializes PyQT application"""
        # Create App
        self.app = QApplication(sys.argv)

        # Open the qss styles file and read
        # with open('./style.qss', 'r') as f:
        #     style = f.read()
        #
        #     # Set the stylesheet of the application
        #     app.setStyleSheet(style)
        # print(QStyleFactory.keys())

        # Make it look not as bad...
        # app.setStyle()

        self.data = None

        # Show Window
        self.win = Homepage(owner=self)
        self.win.setGeometry(400, 400, 400, 300)

        self.win.show()

        self.app.exec_()


    def close_window(self):
        """Closes the window. Added to appease lord PyLint"""
        self.win.close()

    def get_data(self):
        """Returns submitted form data"""
        return self.data

# gui = Gui()
# print(type(gui))