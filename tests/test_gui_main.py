"""This module tests that the GUI opens"""

from src.gui_main import Gui
from src.gui.homepage import Homepage
from src.gui.check_file import CheckFile


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
