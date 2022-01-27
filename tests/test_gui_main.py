"""This module tests that the GUI opens"""

from gatorconfig.gui.homepage import Homepage
from gatorconfig.gui.check_file import CheckFile


def test_homepage(qtbot):
    """Check that the gui opens"""
    application = Homepage()
    qtbot.addWidget(application)
    assert isinstance(application, Homepage)


def test_checkfile(qtbot):
    """Check that CheckFile is actually a CheckFile"""
    check = CheckFile()
    qtbot.addWidget(check)
    assert isinstance(check, CheckFile)
