import pyinputplus as pyip
response = pyip.inputNum('Enter num: ', min=4)
# 3
# 4
# response

response = pyip.inputNum('Enter num: ', greaterThan=4)
# 4
# 5
# response

response = pyip.inputNum('>', min=4, lessThan=6)
# 6
# 3
# 4
# response