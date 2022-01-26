"""This module tests that the GUI opens"""

from src.gui_main import Gui
from src.gui.check_file import CheckFile


def test_gui():
    """Check that the gui opens"""
    gui = Gui(test=True)
    assert isinstance(gui, Gui)


def test_checkfile():
    """Check that CheckFile is actually a CheckFile"""
    check = CheckFile()
    assert isinstance(check, CheckFile)
