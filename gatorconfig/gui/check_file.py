"""Checked File widgets"""
# pylint: disable=no-name-in-module
# RC file is not working.
import os
from PyQt6.QtWidgets import QWidget, \
    QVBoxLayout, QLabel, \
    QHBoxLayout, QLineEdit, QPushButton, \
    QPlainTextEdit, QFrame, \
    QFileDialog


class CheckFile(QWidget):
    """QWidget class for a checked file"""

    def __init__(self, parent=None):
        """Init QWidget parent and the widgets that make up a checked file widget"""
        super().__init__(parent)
        self.outer_lay = QVBoxLayout()

        self.file = None

        # ----File Browser----#
        # Hbox Layout
        lay = QHBoxLayout()
        self.check_label = QLabel("File ")
        self.path_text = QLineEdit()
        self.path_button = QPushButton("Browse...",
                                       clicked=lambda: self.get_path_from_file(self.path_text))
        self.file_params = QPlainTextEdit()

        # Add widgets to hbox layout
        lay.addWidget(self.check_label)
        lay.addWidget(self.path_text)
        lay.addWidget(self.path_button)

        self.outer_lay.addLayout(lay)
        self.outer_lay.addWidget(self.file_params)

        # Horizontal line separator
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)

        self.outer_lay.addWidget(self.frame)

        self.setLayout(self.outer_lay)

    def get_path_from_file(self, target_text):
        """Opens a file dialog to select a new file.
        Sets self.file to the file name and sets the tab text."""
        self.file = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        self.file = os.path.relpath(self.file, os.curdir)
        target_text.setText(self.file)
        tabs = self.parentWidget().parentWidget()
        tabs.setTabText(tabs.currentIndex(), os.path.basename(self.file))

    def get_data(self):
        """Gets all the data of the checked files and returns their file paths and params."""
        if self.file is None:
            self.file = self.path_text.text()
        return self.file, self.file_params.toPlainText().split("\n")
