from pathlib import Path
Path.cwd()

Path.cwd().parents[0]

Path.cwd().parents[1]

Path.cwd().parents[2]

Path.cwd().parents[3]

Path.cwd().parents[4]

Path.cwd().parents[5]

Path.cwd().parents[6]

import os
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(calcFilePath)

os.path.dirname(calcFilePath)

os.path.split(calcFilePath)

(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))

calcFilePath.split(os.sep)

'/usr/bin'.split(os. sep)