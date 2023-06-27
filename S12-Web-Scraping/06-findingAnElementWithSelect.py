import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems)  # elems is a list of Tag objects.

len(elems)

type(elems[0])

str(elems[0])  # The Tag object as a string.

elems[0].getText()

elems[0].attrs

pElems = exampleSoup.select('p')
str(pElems[0])

pElems[0].getText()

str(pElems[1])

pElems[1].getText()

str(pElems[2])

pElems[2].getText()