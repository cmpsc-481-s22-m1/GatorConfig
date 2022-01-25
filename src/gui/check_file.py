from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os


class CheckFile(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent=None)

        # self.box = QGroupBox()
        self.outer_lay = QVBoxLayout()

        self.file = None

        # ----File Browser----#
        # Hbox Layout
        lay = QHBoxLayout()
        self.check_label = QLabel("File ")
        self.path_text = QLineEdit()
        self.path_button = QPushButton("Open",
                                       clicked=lambda: self.get_path_from_file(self.path_text, self.path_button))
        self.file_params = QPlainTextEdit()

        # Add widgets to hbox layout
        lay.addWidget(self.check_label)
        lay.addWidget(self.path_text)
        lay.addWidget(self.path_button)

        self.outer_lay.addLayout(lay)
        self.outer_lay.addWidget(self.file_params)


        # ----File Params----#

        # self.add_param_button = QPushButton("Add New Check", clicked=lambda: self.add_param())

        # self.outer_lay.addWidget(self.add_param_button)



        # self.box.setLayout(self.outer_lay)

        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.HLine)
        self.frame.setFrameShadow(QFrame.Sunken)

        self.outer_lay.addWidget(self.frame)

        self.setLayout(self.outer_lay)

    def get_path_from_file(self, targetText, targetButton):
        self.file = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        targetText.setText(self.file)
        tabs = self.parentWidget().parentWidget()
        tabs.setTabText(tabs.currentIndex(), os.path.basename(self.file))

    def get_data(self):
        if self.file is None:
            self.file = self.path_text.text()
        return self.file, self.file_params.toPlainText().split()

    def add_param(self):
        self.outer_lay.insertWidget(self.outer_lay.count() - 1, Param(self.outer_lay.count() - 1))


class Param(QWidget):
    def __init__(self, check_num, parent=None):
        super(QWidget, self).__init__(parent)

        self.label = QLabel("Check " + str(check_num))
        self.line = QLineEdit()

        lay = QHBoxLayout()
        lay.addWidget(self.label)
        lay.addWidget(self.line)

        self.setLayout(lay)

