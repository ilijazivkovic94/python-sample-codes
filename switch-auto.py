from autogui import * 
open("calc")
open("notepad") 
write("this is autogui","Text Editor")
setWindow("calculator")
click("One")
close("Untitled - Notepad")
close()