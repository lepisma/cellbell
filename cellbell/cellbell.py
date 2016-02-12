# -*- coding: utf-8 -*-

import pyglet
import os
from IPython.core.magic import Magics, magics_class, line_cell_magic

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
