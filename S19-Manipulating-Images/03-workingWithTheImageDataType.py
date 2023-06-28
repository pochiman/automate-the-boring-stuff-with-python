from PIL import Image
catIm = Image.open('zophie.png')
catIm.size

width, height = catIm.size
width

height

catIm.filename

catIm.format

catIm.format_description

catIm.save('zophie.jpg')

# Pillow also provides the Image.new() function, which returns an Image object
# —much like Image.open(), except the image represented by Image.new()’s object 
# will be blank. The arguments to Image.new() are as follows:
from PIL import Image
im = Image.new('RGBA', (100, 200), 'purple')
im.save('purpleImage.png')
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')

# Cropping Images
from PIL import Image
catIm = Image.open('zophie.png')
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')

# Copying and Pasting Images onto Other Images
from PIL import Image
catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

# Let’s continue the shell example by pasting a smaller image onto catCopyIm.
faceIm = catIm.crop((335, 345, 565, 560))
faceIm.size

catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')

# Say you want to tile Zophie’s head across the entire image.
# You can achieve this effect with just a couple for loops.
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('tiled.png')

# Resizing an Image
from PIL import Image
catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.png')

# Rotating and Flipping Images
from PIL import Image
catIm = Image.open('zophie.png')
catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')

# The rotate() method has an optional expand keyword argument that can be set to 
# True to enlarge the dimensions of the image to fit the entire rotated new image.

catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

# You can also get a “mirror flip” of an image with the transpose() method.
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

# Changing Individual Pixels
from PIL import Image
im = Image.new('RGBA', (100, 100))
im.getpixel((0, 0))

for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

from PIL import ImageColor
for x in range(100):
    for y in range(50, 100):
        im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
im.getpixel((0, 0))

im.getpixel((0, 50))

im.save('putPixel.png')