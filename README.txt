
IdleXL - IDLE Extensions for Python
==================================

Version 1.0

IdleXL is a port of IdleX, developed by Roger D. Serwy, to Python 3.6+.


Installing IdleX
================

Use *pip* to install IdleXL directly from pypi.


Running IdleX
=============

On Windows:
    1) Open a console window.
    2) Run:
        py -3 -m idlexl
    Optional:
       Run "scripts/EditWithIdleX.py" if you want 'Edit with IdleX'
       in the right-click context menu.

On Linux:
    1) Open a terminal.
    3) Run:
        $ python3 -m idlexl


Demos
=====

The "demos" directory has several .py files that detail the 
functionality of some of these extensions.

Acknowledgements
================

Acknowledgements may be found in idlexlib/ACKS.txt


Adding Extensions to Standard IDLE
==================================

If you want to include an extension in the standard IDLE,
copy the extension to "idlelib" and then modify
idlelib/config-extensions.def to include the contents
of "config_extension_def" found in the extension source code.


