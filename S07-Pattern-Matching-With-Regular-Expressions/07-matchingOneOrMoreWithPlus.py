import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None