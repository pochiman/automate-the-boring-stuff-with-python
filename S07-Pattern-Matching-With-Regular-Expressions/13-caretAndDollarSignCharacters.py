import re
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world!')

beginsWithHello.search('He said hello.') == None

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')

endsWithNumber.search('Your number is forty two.') == None

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')

wholeStringIsNum.search('12345xyz67890') == None
wholeStringIsNum.search('12 34567890') == None