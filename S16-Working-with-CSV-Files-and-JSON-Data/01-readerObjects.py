import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData

exampleData[0][0]

exampleData[0][1]

exampleData[0][2]

exampleData[1][1]

exampleData[6][1]