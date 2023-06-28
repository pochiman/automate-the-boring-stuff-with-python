import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')

import subprocess
paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')
paintProc.poll() == None

paintProc.wait()  # Doesn't return until MS Paint closes.
paintProc.poll()

# Passing Command Line Arguments to the Popen() Function
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\Al\\hello.txt'])

# Running Other Python Scripts
subprocess.Popen(['C:\\Users\\<YOUR USERNAME>\\AppData\\Local\\Programs\\Python\\Python38\\python.exe', 'hello.py'])