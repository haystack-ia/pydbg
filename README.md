This is a package of pydbg that's (maybe) easier to install than the stock version

First off, install the [Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-us/download/details.aspx?id=44266).

Then, clone this repository, navigate to the repo folder, and install the package by:

`pip install -e . --process-dependency-links --allow-all-external`

This will download, compile, and install the pydasm package and then install pydbg.

Major hat-tip to axcheron for putting together the user-friendly pydasm install, and of course to Pedram Amini for writing pydbg.

