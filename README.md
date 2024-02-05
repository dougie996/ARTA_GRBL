# ARTA_GRBL
Simple Interface between ARTA and a GRBL Stepper Motor Device

ARTA_GRBL is a software translator of ARTA Commands into a GRBL compatible Stepper Driver

Aim was to keep it simple and without any modifications neccessary in ARTA
So only few commands hat to be translated:

ARTA_GRBL is available as Python3 Skript and as Windows x64 Executable

ARTA_GRBL xxx where xxx is a number between 0 and 360, drives the Stepper to the given Position 
ARTA_GRBL -r  performs a stop and resets the current position to zero
              Note: -r is a kind of emergency shutdown and puts GRBL into the ALARM state, where no further Movement is possible, befor the Alarm State has been cleared. 
ARTA_GRBL $X  Clears the Alarm State
ARTA_GRBL ?   Returns the current status and position
