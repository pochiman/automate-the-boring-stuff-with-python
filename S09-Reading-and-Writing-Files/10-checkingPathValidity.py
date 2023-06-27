from pathlib import Path
winDir = Path('C:/Windows')
notExistsDir = Path('C:/This/Folder/Does/Not/Exist')
calcFile = Path('C:/Windows/System32/calc.exe')
winDir.exists()

winDir.is_dir()

notExistsDir.exists()

calcFile.is_file()

calcFile.is_dir()

dDrive = Path('D:/')
dDrive.exists()