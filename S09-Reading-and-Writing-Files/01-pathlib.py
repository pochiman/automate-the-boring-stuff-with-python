from pathlib import Path
Path('spam', 'bacon', 'eggs')

str(Path('spam', 'bacon', 'eggs'))

from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))