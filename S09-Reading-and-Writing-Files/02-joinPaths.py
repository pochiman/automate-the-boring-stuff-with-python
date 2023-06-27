from pathlib import Path
Path('spam') / 'bacon' / 'eggs'

Path('spam') / Path('bacon/eggs')

Path('spam') / Path('bacon', 'eggs')

homeFolder = r'C:\Users\Al'
subFolder = 'spam'
homeFolder + '\\' + subFolder

'\\'.join([homeFolder, subFolder])

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
homeFolder / subFolder

str(homeFolder / subFolder)

'spam' / 'bacon' / 'eggs'