fileObj = open('hello.txt', 'w')
fileObj.write('Hello, world!')

fileObj.close()
import subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)

# On macOS, the open program is used for opening both document files and programs.
subprocess.Popen(['open', '/Applications/Calculator.app/'])