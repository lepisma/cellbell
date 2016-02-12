from . import cellbell

try:
    ipy = get_ipython()
    ipy.register_magics(cellbell.CellBellMagic)
except NameError:
    print("cellbell works only with IPython and notebooks")
