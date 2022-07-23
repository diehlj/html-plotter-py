html-plotter
------------

A quick hack to make matplotlib plot onto disk, with img-references added to a html-file.

Example usage::

   import html_plotter
   from matplotlib import pyplot as plt
   plt.plot( range(1,10), [x**2 for x in range(1,10)] )
   html_plotter.show( plt )
   # => plot viewable in= /tmp/matplotlib/index.html

Installation
------------

Install with::

    pip install git+https://github.com/diehlj/html-plotter-py

Copyright © 2019 Joscha Diehl

Distributed under the `Eclipse Public License <https://opensource.org/licenses/eclipse-1.0.php>`_.
