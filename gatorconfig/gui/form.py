"""Form that makes up the configuration GUI"""
# pylint: disable=no-name-in-module
# RC file is not working.
import requests.exceptions
from PyQt6.QtWidgets import QTabWidget, \
    QWidget, QFormLayout, \
    QCheckBox, QLineEdit, \
    QVBoxLayout, QPushButton, \
    QSpinBox, QHBoxLayout, QPlainTextEdit, QFileDialog, QComboBox
from gatorconfig.gui.check_file import CheckFile
from gatorconfig import scrape_releases as scrape
from gatorconfig.gui.cwidgets import CFilePicker


# pylint: disable=too-many-instance-attributes
# pylint: disable=unnecessary-lambda
# Disabling too-many-instance-attributes because
# this is a main class. PyQt6 *requires* this type of code.
# Could split this into multiple classes if REALLY needed but that can wait until later.
# Also disabling unnecessary-lambda because the lambda is necessary.

class Form(QTabWidget):
    """Main form class, contains basic and advanced tabs."""

    def __init__(self, parent=None):
        """Init the form. Create the two tabs and populate them with widgets."""
        super().__init__(parent)

        # Create tabs
        self.basic = QWidget()
        self.advanced = QWidget()

        # Add form to tabs
        self.addTab(self.basic, "Basic")
        self.addTab(self.advanced, "Advanced")
        self.basic_tab()
        self.advanced_tab()

    def basic_tab(self):
        """Creates a new form and populates it with the widgets for basic configuration"""
        # Create a QFormLayout instance
        form_layout = QFormLayout()

        # Add widgets to the form
        self.fast_fail = QCheckBox()
        self.break_fail = QCheckBox()
        self.break_fail.setChecked(True)
        self.generate_readme = QCheckBox()

        # Get github releases
        try:
            grader_versions = scrape.get_github_releases("GatorEducator/GatorGrader")
            self.grader_version = QComboBox()
            self.grader_version.addItem("Latest")
            self.grader_version.addItems(grader_versions)
            self.grader_version.setMaxVisibleItems(15)
        except requests.exceptions.ConnectionError:
            self.grader_version = QLineEdit()

        try:
            gradle_versions = scrape.get_github_releases("GatorEducator/GatorGradle")
            self.gradle_version = QComboBox()
            self.gradle_version.addItems(gradle_versions)
            self.gradle_version.setMaxVisibleItems(15)
        except requests.exceptions.ConnectionError:
            self.gradle_version = QLineEdit()

        self.reflection = CFilePicker()

        self.assignment_name = QLineEdit("Default")

        form_layout.addRow("Fast Fail:", self.fast_fail)
        form_layout.addRow("Break:", self.break_fail)
        form_layout.addRow("Generate ReadMe:", self.generate_readme)
        form_layout.addRow("GatorGrader Version:", self.grader_version)
        form_layout.addRow("GatorGradle Version:", self.gradle_version)
        form_layout.addRow("Reflection:", self.reflection)
        form_layout.addRow("Assignment Name:", self.assignment_name)

        # Create VBox for group
        group_lay = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.tabs.removeTab)

        # Checked Files Controls
        # Create add file button
        add_file_button = QPushButton(
            "Add New Checked File", clicked=lambda: self.add_checked_file())

        # Add button to layout
        group_lay.addWidget(add_file_button)

        form_layout.addRow(self.tabs)
        form_layout.addRow(group_lay)

        self.setTabText(0, "Basic")
        self.basic.setLayout(form_layout)

    def advanced_tab(self):
        """Creates the form for the advanced tab and populates it with the required widgets."""
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
        self.startup_script_button = QPushButton("Browse...",
                                                 clicked=lambda: self.get_path_from_file(
                                                     self.startup_script_text))

        self.executables = QLineEdit()
        self.idcommand = QLineEdit()

        # connect button to file dialog
        # self.startup_script_button.clicked.connect()

        # Add widgets to hbox layout
        self.lay.addWidget(self.startup_script_text)
        self.lay.addWidget(self.startup_script_button)

        form_layout.addRow("Startup Script:", self.lay)
        form_layout.addRow("Executables:", self.executables)
        form_layout.addRow("Id Command:", self.idcommand)

        self.description_input2 = QPlainTextEdit()

        self.setTabText(1, "Advanced")
        self.advanced.setLayout(form_layout)

    def add_checked_file(self):
        """Creates a new CheckFile and adds it to the basic config's file tabs."""
        self.tabs.addTab(CheckFile(), "File " + str(self.tabs.count() + 1))
        self.tabs.setCurrentIndex(self.tabs.currentIndex() + 1)

    def get_path_from_file(self, target_text):
        """Opens a file dialog to select a new file.
        Sets self.file to the file name and sets the tab text."""
        file = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        target_text.setText(file)

    def change_tab_text(self, text):
        """Changes the current tab's text."""
        self.tabs.setTabText(self.tabs.currentIndex(), text)

    def submit_form(self):
        """Submits the data from both the basic and advanced tabs."""
        files = {}

        for index in range(self.tabs.count()):
            widget = self.tabs.widget(index)
            key, val = widget.get_data()
            files[key] = val

        full_data = {
                        "header": {
                            "name": self.assignment_name.text(),
                            "break": self.break_fail.isChecked(),
                            "fastfail": self.fast_fail.isChecked(),
                            "indent": int(self.indent_size.text()),
                            "version": self.get_grader_version(),
                        },
                        "body": files
                     }

        full_data = self.insert_checked_commands(full_data)
        print("Form Submitted!")
        return full_data

    def get_grader_version(self):
        """Returns GatorGrader version depending on the input type"""
        if isinstance(self.grader_version, QComboBox):
            if self.grader_version.currentText() == "Latest":
                return "master"
            return self.grader_version.currentText()
        return self.grader_version.text()

    def insert_checked_commands(self, data):
        """Returns full_data header with added idcommand, executables,
        reflection, and startup script if the user specified them."""
        if self.idcommand.text() != "":
            data["header"]["idcommand"] = self.idcommand.text()

        if self.executables.text() != "":
            data["header"]["executables"] = self.executables.text()

        if self.reflection.text() != "":
            data["header"]["reflection"] = self.reflection.text()

        if self.startup_script_text.text() != "":
            data["header"]["startup"] = self.startup_script_text.text()

        return data
