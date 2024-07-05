

#---------------------------------------------------------------------------
from PIL import Image
import os

os.makedirs('watermarked_images')
logo_image = Image.open('watermark_logo.png')
logo_image = logo_image.resize((50, 50))
logo_width, logo_height = logo_image.size
for image in os.listdir('./images'):

    # Separting the filepath from the image's name
       path, filename = os.path.split(image)
       filename = os.path.splitext(filename)[0]
       with  Image.open('./images/' + image) as image:
           # Resizing the image to a set size.
           edited_image = image.resize((300, 300))
           # Setting the position for the placement
           width = edited_image.width
           height = edited_image.height
           edited_image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)
           edited_image.save('./watermarked_Images/' + filename + ".jpg")



