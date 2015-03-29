# paste
This is a tiny script helping you paste texts from windows clipboard to any program.

How to use:
1. Copy paste.exe to local drive
2. Create a desktop shortcut for paste.exe
3. Edit shortcut property, use combined key(I recommand Alt+Shift+*Key*) as shortcut key
Ready to go.
Copy any texts, and switch to program window, press the combined  shortcut key.

How it works:
Quite simple, just take words from clipboard and convert to string, use sendkeys to emulate  keystrokes, it literally types the texts out.

How to play: 
In order to compile, these packages are required:
python-2.7
pywin32-217
SendKeys-0.3
If you want to build a python script to executive file, this file is needed:
pyinstaller-2.0
Input this command to generate .exe
#pyinstaller.py --onefile -w paste.pyw


This script is far from perfection, if you found any bug, feel free to fix it yourself;)
okay-dokey, have fun!
