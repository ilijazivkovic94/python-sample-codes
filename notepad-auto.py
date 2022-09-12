from autogui import *
open("notepad")
click("File")
click("Text Editor")
write("This is AutoGui ","Text Editor")
append(" writing, appending, and sending keys is easy!","Text Editor")
sendkey("{ENTER}")
read("Text Editor")
# close()