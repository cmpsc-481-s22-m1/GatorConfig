from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.check_file import CheckFile


class Form(QTabWidget):
    def __init__(self, parent=None):
        super(QTabWidget, self).__init__(parent)

        # Create tabs
        self.basic = QWidget()
        self.advanced = QWidget()

        # Add form to tabs
        self.addTab(self.basic, "Basic")
        self.addTab(self.advanced, "Advanced")
        self.basic_tab()
        self.advanced_tab()

    def basic_tab(self):
        # Create a QFormLayout instance
        form_layout = QFormLayout()

        # Add widgets to the form
        self.fast_fail = QCheckBox()
        self.break_fail = QCheckBox()
        self.generate_readme = QCheckBox()

        self.grader_version = QLineEdit("v0.2.0")

        self.assignment_name = QLineEdit("Default")

        form_layout.addRow("Fast Fail:", self.fast_fail)
        form_layout.addRow("Break:", self.break_fail)
        form_layout.addRow("Generate ReadMe:", self.generate_readme)
        form_layout.addRow("GatorGrader Version:", self.grader_version)
        form_layout.addRow("Assignment Name:", self.assignment_name)

        # Create VBox for group
        group_lay = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(lambda index: self.tabs.removeTab(index))

        # Checked Files Controls
        # Create add file button
        add_file_button = QPushButton("Add New Checked File", clicked=lambda: self.add_checked_file())

        # Add button to layout
        group_lay.addWidget(add_file_button)

        # group.setLayout(group_lay)
        form_layout.addRow(self.tabs)
        form_layout.addRow(group_lay)

        self.setTabText(0, "Basic")
        self.basic.setLayout(form_layout)

    def advanced_tab(self):
        # Create a QFormLayout instance
        form_layout = QFormLayout()

        # Add widgets to the form

        # ---Indent Size---#
        self.indent_size = QSpinBox()
        self.indent_size.setValue(4)
        self.indent_size.setMinimum(1)

        form_layout.addRow("Indent Size:", self.indent_size)

        # ---Startup Script---#

        # Hbox Layout
        self.lay = QHBoxLayout()
        self.startup_script_text = QLineEdit()
        self.startup_script_button = QPushButton("Open",
                                                 clicked=lambda: self.get_path_from_file(self.startup_script_text,
                                                                                         self.startup_script_button))

        # connect button to file dialog
        # self.startup_script_button.clicked.connect()

        # Add widgets to hbox layout
        self.lay.addWidget(self.startup_script_text)
        self.lay.addWidget(self.startup_script_button)

        form_layout.addRow("Startup Script:", self.lay)

        self.description_input2 = QPlainTextEdit()

        # submit_button = QPushButton("Submit", clicked = lambda: self.submit_clicked())
        # submit_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.setTabText(1, "Advanced")
        self.advanced.setLayout(form_layout)

    def add_checked_file(self):
        self.tabs.addTab(CheckFile(), "File " + str(self.tabs.count() + 1))
        self.tabs.setCurrentIndex(self.tabs.currentIndex() + 1)

        # group_lay.insertWidget(group_lay.count() - 1, CheckFile(group_lay.count()))

    def change_tab_text(self, text):
        self.tabs.setTabText(self.tabs.currentIndex(), text)

    def submit_form(self):
        files = {}

        for index in range(self.tabs.count()):
            widget = self.tabs.widget(index)
            key, val = widget.get_data()
            files[key] = val

        full_data = {"name": self.assignment_name.text(),
                     "break": self.break_fail.isChecked(),
                     "fastfail": self.fast_fail.isChecked(),
                     "indent": int(self.indent_size.text()),
                     "idcommand": "echo $TRAVIS_REPO_SLUG",
                     "version": self.grader_version.text(),
                     "executables": "cat, bash",
                     "startup": self.startup_script_text.text(),
                     "reflection": "./",
                     "files": files
                     }

        print("Form Submitted!")
        print(full_data)
