import pyinputplus as pyip
response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# XLII
# response

response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
# xlii
# response

import pyinputplus as pyip
response = pyip.inputNum(blockRegexes=[r'[02468]$'])
# 42

# 44

# 43
# response

import pyinputplus as pyip
response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
# cat

# catastrophe

# category
# response