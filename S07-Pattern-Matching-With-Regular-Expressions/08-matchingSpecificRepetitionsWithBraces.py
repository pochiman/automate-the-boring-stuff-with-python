import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

mo2 = haRegex.search('Ha')
mo2 == None