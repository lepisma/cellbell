=============================
cellbell
=============================

Bell magic for IPython. Rings a bell when cell evaluation (IPython shell or
Jupyter notebook) is complete.

``pip install cellbell``

Use as cell or line magic::

    # Import
    import cellbell
    
    # line magic
    %ding my_long_function()
    
    # cell magic
    %%ding
    time.sleep(4)
    my_long_function()
    time.sleep(2)
    print("done")

Can also be used directly by calling ``ding``::

    # Import
    import cellbell

    cellbell.ding()


Inspired by `ipython-bell <https://github.com/samwhitehall/ipython-bell>`_, but
works on all systems by playing a wav.
