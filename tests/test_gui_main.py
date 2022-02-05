"""This module tests that the GUI opens"""

from gatorconfig.gui.homepage import Homepage
from gatorconfig.gui.check_file import CheckFile
from gatorconfig.gui.form import Form
from gatorconfig.gui.cwidgets import CFilePicker


def test_file_picker(qtbot):
    """Test that the file picker is a file picker"""
    application = CFilePicker()
    qtbot.addWidget(application)
    assert isinstance(application, CFilePicker)


def test_homepage(qtbot):
    """Check that the gui opens"""
    application = Homepage()
    qtbot.addWidget(application)
    assert isinstance(application, Homepage)


def test_form(qtbot):
    """Check that form is actually a form"""
    application = Form()
    qtbot.addWidget(application)
    assert isinstance(application, Form)


def test_checkfile(qtbot):
    """Check that CheckFile is actually a CheckFile"""
    check = CheckFile()
    qtbot.addWidget(check)
    assert isinstance(check, CheckFile)
