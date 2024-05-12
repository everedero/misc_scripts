# Tracecompass scripts

## Installing TraceCompass with scripting modules

Go in Eclipse downloads and find the latest TraceCompass tar.gz with all the incubator features included, for instance [here](https://www.eclipse.org/downloads/download.php?file=/tracecompass.incubator/master/rcp/trace-compass-0.9.0-20240508-0458-linux.gtk.x86_64.tar.gz&mirror_id=1285).

You can also download TraceCompass and try adding the modules:
* Scripting
* Scripting Javascript
* Scripting Python

But in my case it fails with [this error](https://github.com/ge-high-assurance/VERDICT/issues/75).

## Importing the module

    File -> Open Trace -> zephyr_thread_states.js

Then open the trace, and run the script with:

    Run As... -> Ease Script



