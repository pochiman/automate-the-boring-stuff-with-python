import zipfile, os
from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall()
exampleZip.close()

exampleZip.extract('spam.txt')

exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')

exampleZip.close()