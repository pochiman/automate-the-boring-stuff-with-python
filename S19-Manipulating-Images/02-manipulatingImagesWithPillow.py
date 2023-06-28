from PIL import Image
catIm = Image.open('zophie.png')

# If the image file isn’t in the current working directory, change the
# working directory to the folder that contains the image file by calling
# the os.chdir() function.
import os
os.chdir('C:\\folder_with_image_file')