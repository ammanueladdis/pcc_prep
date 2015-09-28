Setup Instructions: Linux
===

- Checking your current version of Python
- Installing Python 3.5
- Installing a Text Editor

Checking your current version of Python
---

Python is probably already installed on your system. Find out which version is your default by issuing the command `python --version`:

    $ python --version
    Python 2.7.3

If you see something like this, Python 2.7 is your default version. You should also see if you have Python 3 installed:

    $ python3 --version
    Python 3.4.0

If you have Python 3.4 or later, you should use the installed version. If you have Python 3.3 or earlier, it's probably worth installing Python 3.5.

Installing Python 3.5
---

The following instructions should work on Ubuntu, and most Debian-based systems that use the apt package manager.

Add the *deadsnakes* package, and then install Python 3.5:

    $ sudo add-apt-repository ppa:fkrull/deadsnakes
    $ sudo apt-get update
    $ sudo apt-get install python3.5

You can confirm that the installation was successful:

    $ python3.5 --version
    Python 3.5.0

Now to start a Python terminal session, you'll use the command `python3.5`:

    $ python3.5
    Python 3.5.0 (default, Sep 17 2015, 00:00:00) 
    [GCC 4.8.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>




