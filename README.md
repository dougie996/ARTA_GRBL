ARTA_GRBL
Simple Interface between ARTA and a GRBL Stepper Motor Device

ARTA_GRBL is a software translator of ARTA Commands into a GRBL compatible Stepper Driver

Aim was to keep it simple and without any modifications neccessary in ARTA.
So only few commands had to be translated:

ARTA_GRBL is available as Python3 Skript and as Windows x64 Executable

<code>ARTA_GRBL xxx</code> where xxx is a number between 0 and 360, drives the Stepper to the given Position <br>
<code>ARTA_GRBL -r</code>  performs a stop and resets the current position to zero<br>
        Note: -r is a kind of emergency shutdown and puts GRBL into the ALARM state, while in motion.<br>
        No further Movement is possible, before the Alarm State hasn't been cleared. <br>
<code>ARTA_GRBL $X</code>  Clears the Alarm State<br>
<code>ARTA_GRBL ?</code>   Returns the current status and position<br>
<code>ARTA_GRBL $$</code>  Returns all GRBL settings<br>
