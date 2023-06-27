from pathlib import Path
p = Path('C:/Users/Al/Desktop')
p.glob('*')

list(p.glob('*'))  # Make a list from the generator.

list(p.glob('*.txt'))  # Lists all text files.

list(p.glob('project?.docx'))

list(p.glob('*.?x?'))

p = Path('C:/Users/Al/Desktop')
for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj)  # Prints the Path object as a string.
    # Do something with the text file.