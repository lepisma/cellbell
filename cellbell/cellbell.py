# -*- coding: utf-8 -*-

import os

import pyglet
from IPython.core.magic import Magics, line_cell_magic, magics_class

BELL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bell.wav")

bell = pyglet.media.load(BELL_PATH, streaming=False)

@magics_class
class CellBellMagic(Magics):

    @line_cell_magic
    def ding(self, line, cell=None):
        if cell:
            code = cell
        else:
            code = line

        self.shell.run_cell(code)
        bell.play()

def ding():
    """
    Standalone function for ringing bell
    """

    bell.play()
