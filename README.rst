Python/Javascript Blending Experiments
======================================

This is a set of experiments to see ways in which Python and
Javascript can be combined.

At the moment, it implements a simple function to perform a 2D affine
transformation on 128,000 points in a number of different ways in
order to compare the performance and benefits of different approaches.

In the future, this test example should be made more complex and
involve classes and complex interactions between them.

Below is a list of the different benchmarks available, and how to
build and run them.

Pure Python
-----------

Implemented in pure Python.

Running::

    ./test_pure_python.py

Numpy
-----

Implemented using vector operations on Numpy arrays.

Requirements:

   - `Numpy <http://www.numpy.org>`_

Running::

    ./test_numpy.py

C
-

Implemented using a C extension.  The assumption here is that the data
is in native C format (by, for example, using Numpy arrays.  Actually
placing values in Python objects inside of Python lists would be much
slower, but this test provides a "best case" scenario.

Requirements:

   - Python development headers (`apt-get install python-dev` or `yum
     install python-devel`).  The location of the headers is
     hard-coded in the build file.

   - The gcc compiler

Building::

   ./make_c

Running::

   ./test_c.py

Raw JS
------

This tests a hand-written JavaScript implementation.

Running:

   Open `test_raw_js.html` in your browser.  Press the "Run" button
   and the benchmark results will be logged to the Javascript console.

Skulpt
------

`Skulpt <http://www.skulpt.org>`_ is a Python interpreter written in
Javascript that runs in the web browser.

Requirements:

   - A copy of skulpt is included in the py-js-blending-experiments
     source tree.

Building::

   ./make_skulpt

Running:

   Open `test_skulpt.html` in your browser.  Press the "Run" button and
   the benchmark timing will be output to the JavaScript console.

PyJS
----

`PyJS <http://www.pyjs.org>`_ (formerly Pyjamas) is a
Python-to-Javascript converter, as well as a framework for developing
client-side web applications in Python.

Requirements:

   - Download PyJS and run the `bootstrap.py` script.

Building::

   > export PYJS_HOME=/path/to/pyjs_checkout
   > ./make_pyjs

Running:

   - Start a simple webserver using the `serve.py` script.

   - Open `http://127.0.0.1:8890/output/test_pyjs.html` in your browser.

PyV8
----

`PyV8 <http://code.google.com/p/pyv8/>`_ embeds the open source V8
Javascript engine (from Google Chrome) in the CPython interpreter.  It
allows for running Javascript code from Python, calling into Python
code from Javascript and sharing objects somewhat transparently
between the two sides.

Requirements:

   - Download and install PyV8

Running::

   ./test_v8.py
