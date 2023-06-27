import re
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()

robocop.search('ROBOCOP protects the innocent.').group()

robocop.search('Al, why does your programming book talk about robocop so much?').group()