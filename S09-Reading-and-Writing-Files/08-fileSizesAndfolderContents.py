import os
os.path.getsize('C:\\Windows\\System32\\calc.exe')

os.listdir('C:\\Windows\\System32')

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)    