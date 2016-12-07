from . import cellbell
from .cellbell import ding

try:
    ipy = get_ipython()
    ipy.register_magics(cellbell.CellBellMagic)
except NameError:
    print("""
    cellbell magic works only with IPython and Jupyter notebooks.
    Use `ding` function for other cases.
    """)
