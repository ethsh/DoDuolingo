'This script receives as an argument a command line to run in hidden mode (no cmd popup)

CreateObject("Wscript.Shell").Run "" & WScript.Arguments(0) & "", 0, False