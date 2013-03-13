@ECHO OFF

rem Use this to compile Windows EXEs of PatchIt!

rem Windows x86 build
cd "C:\Program Files (x86)\Python33"
start python.exe Scripts\cxfreeze -O --target-dir %~p0\Compile\Windows32 --icon %~p0\Icons\PatchItIcon.ico %~p0\PatchIt.py

rem Windows x64 build
cd "C:\Program Files\Python33"
start python.exe Scripts\cxfreeze -O --target-dir %~p0\Compile\Windows64 --icon %~p0\Icons\PatchItIcon.ico %~p0\PatchIt.py
exit