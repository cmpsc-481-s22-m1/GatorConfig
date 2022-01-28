"""Main page for the PyQT app"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from gatorconfig.gui.form import Form


class Homepage(QMainWindow):
    """Custom QMainWindow object"""
    def __init__(self, owner=None, parent=None):
        """Init the widget, populate it with the configuration form"""
        super().__init__(parent)
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
        """Gathers data from the form and closes the application"""
        data = form.submit_form()
        self.owner.data = data
        self.close()
