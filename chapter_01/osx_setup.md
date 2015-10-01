Setup Instructions: OS X
===

- [Checking your current version of Python](#current_version)
- [Installing Python 3.5](#python3.5)
- [Installing Sublime Text](#installing_st)
    - [Configuring Sublime Text](#configuring_st)

<a name='current_version'></a>Checking your current version of Python
---

Python is probably already installed on your system. To check if it's installed, go to **Applications>Utilities** and click on **Terminal**. (You can also press command-spacebar, type *terminal*, and then press Enter.)

Find out which version of Python is installed by issuing the command `python --version`:

    $ python --version
    Python 2.7.5

If you see something like this, Python 2.7 is your default version. You should also see if you have Python 3 installed:

    $ python3 --version
    Python 3.4.0

If you have Python 3.4 or later, it's fine to start out by using the installed version. If you have Python 3.3 or earlier, it's probably worth installing Python 3.5.

[top](#)

<a name='python3.5'></a>Installing Python 3.5
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

You'll use this command when you configure your text editor, and when you run programs from the terminal.

[top](#)

<a name='installing_st'></a>Installing Sublime Text
---

You can download an installer for Sublime Text by clicking on the OS X link at [http://www.sublimetext.com/3](http://www.sublimetext.com/3). Sublime Text has a liberal licensing policy; it's free as long as you want to use it, but the author requests that you purchase a license if you like the program and want to continue using it.

After you've downloaded the installer, drag the file into your *Applications* folder.

[top](#)

<a name='configuring_st'></a>
### Configuring Sublime Text for Python 3

If you use the simple command `python` to start a terminal session on your system, you shouldn't have to configure Sublime Text at all. But if you use a command like `python3` or `python3.5`, you'll have to modify Sublime Text slightly so it uses the correct version of Python to run your programs.

Find the path to your Python interpreter:

    $ type -a python3
    python3 is /usr/local/bin/python3

Open an empty file in Sublime Text and save it as *hello_world.py*. The file should have one line in it:

    print("Hello Python world!")

Go to **Tools>Build System>New Build System**, which will open a new configuration file. Delete what you see, and enter the following:

    {
        "cmd": ["/usr/local/bin/python3", "-u", "$file"],
    }

This tells Sublime Text to use your system's **python3** command when running programs. Make sure you use the path you found when running **type -a python3**, not necessarily the path you see here. Save the file as *Python3.sublime-build* in the directory that Sublime Text opens when you choose Save.

Now you can run programs by selecting **Build>Execute**, clicking the Execute icon with a set of gears on it, or by pressing **F5**.

[top](#)



