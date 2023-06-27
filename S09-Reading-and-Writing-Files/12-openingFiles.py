from pathlib import Path
helloFile = open(Path.home() / 'hello.txt')

helloFile = open('C:\\Users\\your_home_folder\\hello.txt')

helloFile = open('/Users/your_home_folder/hello.txt')

helloContent = helloFile.read()
helloContent

sonnetFile = open(Path.home() / 'sonnet29.txt')
sonnetFile.readlines()

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)