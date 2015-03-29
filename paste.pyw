# -*- coding: cp936 -*-
import SendKeys
import time

import win32clipboard

SendKeys.SendKeys("%{ESC}")

win32clipboard.OpenClipboard()
c = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

"""Wait for the window to show up, else will be some chars missing"""
time.sleep(0.05)

c = c.replace("\r\n","\n").replace("+", "+=").replace("{","+[").replace("}","+]").replace("(", "+9").replace(")", "+0").replace("%","+5").replace("~","+`").replace("^","+6").replace("?","+/")

SendKeys.SendKeys(c, 0.00001, True, True, True, True)
