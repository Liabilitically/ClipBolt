Set WshShell = CreateObject("WScript.Shell")
' This runs your python file without showing a black window
WshShell.Run "python main.py", 0
Set WshShell = Nothing