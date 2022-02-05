"""Custom PyQt Widgets"""
# pylint: disable=no-name-in-module
# RC file is not working.
import os

from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QFileDialog, QHBoxLayout


class CFilePicker(QWidget):
    """Custom file selection box"""
    # pylint: disable=W1113
    # This is the proper way to do this. Error in pylint. Check this issue:
    # https://github.com/PyCQA/pylint/issues/2481
    def __init__(self, parent=None, default=None, *args, **kwargs):
        """Initialize selection box widget"""
        super().__init__(parent, *args, **kwargs)

        self.line = QLineEdit()
        if default is not None:
            self.line.setText(default)
        self.button = QPushButton("Browse...",
                                  clicked=lambda: self.line.setText(
                                      QFileDialog.getOpenFileName(self, 'OpenFile')[0]))
        hbox = QHBoxLayout()
        hbox.addWidget(self.line)
        hbox.addWidget(self.button)
        self.setLayout(hbox)

    def set_textbox_text(self, text):
        """Set the textbox text"""
        self.line.setText(os.path.relpath(text))

    def text(self):
        """Return the file path from the text box"""
        if self.line.text() == "":
            return ""
        return os.path.relpath(self.line.text())
