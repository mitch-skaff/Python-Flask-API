Getting Started
---------------

I used `poetry` to setup this project. `poetry` provides packaging and
dependency management for python projects. You can find documentation for
how to use `poetry` at the project website (see the Resources section below).
You will need to install poetry with pip first so you can use it to manage
dependencies for this project. ::

  pip install poetry

Then you'll need to install the project dependencies. In this directory, run ::

  poetry install


When adding dependencies, running the development server or tests, make sure you
have the virtual environment active. To activate the virtual environment for the
project, run ::

  poetry shell


Once the virtual environment is active, you will have access to the locally
installed dependencies like the `flask` CLI, in your shell.

With the dependencies installed and your virtual environment active, you can run
the server by navigating to the `whoami` directory and running ::

  flask run

To run tests, just run ::

  pytest

By default, this will find and run each function that begins with `test_` in each file that
begins with `test_` in the `tests` directory. Consult the pytest documentation (see the link
in the Resources section below) for more details and options.


Resources
---------

* `Poetry documentation <https://python-poetry.org/>`_
* `Flask documentation <https://flask.palletsprojects.com/en/2.0.x/>`_
* `pytest documentation <https://docs.pytest.org/en/6.2.x/contents.html>`_
