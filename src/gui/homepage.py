from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.form import Form


class Homepage(QMainWindow):
    def __init__(self, owner=None, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setWindowTitle("New Configuration")

        self.owner = owner
        # Create Central Widget
        main_win = QWidget()

        # Create Layout
        lay = QVBoxLayout()

        # Create top label
        top_label = QLabel("New Configuration File", alignment=Qt.AlignHCenter)

        # Create Form
        form = Form()

        # Create Submit Button
        submit_button = QPushButton("Submit", clicked=lambda: self.submit_form(form))

        # Add widgets
        lay.addWidget(top_label)
        lay.addWidget(form)
        lay.addWidget(submit_button)
        lay.setAlignment(submit_button, Qt.AlignRight)
        lay.addStretch()

        # Set Layout
        main_win.setLayout(lay)

        # Set central widget
        self.setCentralWidget(main_win)

    def submit_form(self, form):
        data = form.submit_form()
        self.owner.data = data
        self.close()
