from PIL import Image
import glob
import numpy as np

class ImageProcessing:          #defining a class that takes an image
    def __init__(self, image):                  #initializing by opening the image
        self.img = Image.open(image)

    def show(self):                             #defining a function to show the image from pilow package
        self.img.show()

    def size(self):                             #defining a function to find the image size from pilow package
        self.img.size

    def grey(self):                             #defining a function to convert the image color to grey
        grey_img = self.img.convert("L")
        return grey_img

    def histogram(self):                         #defining a function to find 10 bin histogram for the image
        grey_img = self.grey()                   #converting to grey using the predefined grey function
        grey_img_n = grey_img.point(lambda i: int(i / 28))        #coverting from 0-255 range to 0-10 range
        size = grey_img_n.size
        length = size[0]
        width = size[1]
        pixel = np.zeros((length, width))        #defining an array to store pixels of the image
        for i in range(length):
            for j in range(width):
                pixel[i][j] = grey_img_n.getpixel((i, j))
        histo = {}
        for i in range(length):                  #calculating the count of each grey level
            for j in range(width):
                if pixel[i][j] not in histo.keys():
                    histo[pixel[i][j]] = 1
                else:
                    histo[pixel[i][j]] = histo[pixel[i][j]] + 1
        return histo

def thumbnails(directory):                              #defining a function that converts each image in a directory to thumbnail image
    img_format = ['jpg', 'png', 'gif']
    img_format_O = ['JPEG', 'PNG', 'GIF']
    directory_ = directory + '\\'
    if directory == 'current':                          #if the directory is the current directory where the code exists
        for frmt in img_format:
            for img_name in glob.glob('*.' + frmt):      #using glob package to go to directory path
                img = Image.open(img_name)
                img.thumbnail((100, 100), Image.ANTIALIAS)  #using thumbnail function to convert image to thumbnail with maximum size 100*100
                if img_name[0:2] != 'T_':                #ensuring that the image is not coverted yet
                    for i in range(3):
                        if frmt == img_format[i]:
                            img.save('T_' + img_name, img_format_O[i])   #saving thumbnail image with T_ prefix
    else:
        for frmt in img_format:
            for img_address in glob.glob(directory_+'*.'+frmt):
                img = Image.open(img_address)
                img.thumbnail((100, 100), Image.ANTIALIAS)
                img_name = img_address.replace(directory_, '')

                if img_name[0:2] != 'T_':
                    img_address_new = img_address.replace(directory_, directory_ + 'T_')
                    for i in range(3):
                        if frmt == img_format[i]:
                            img.save(img_address_new, img_format_O[i])
    print('Thumbnails for all images in your directory are created, Check your directory!')
