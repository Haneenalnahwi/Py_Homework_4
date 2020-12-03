from PIL import Image
import glob
import numpy as np

class ImageProcessing:
    def __init__(self, image):
        self.img = Image.open(image)

    def show(self):
        self.img.show()

    def size(self):
        self.img.size

    def grey(self):
        grey_img = self.img.convert("L")
        return grey_img

    def histogram(self):
        grey_img = self.grey()
        grey_img_n = grey_img.point(lambda i: int(i / 28))
        size = grey_img_n.size
        length = size[0]
        width = size[1]
        pixel = np.zeros((length, width))
        for i in range(length):
            for j in range(width):
                pixel[i][j] = grey_img_n.getpixel((i, j))
        histo = {}
        for i in range(length):
            for j in range(width):
                if pixel[i][j] not in histo.keys():
                    histo[pixel[i][j]] = 1
                else:
                    histo[pixel[i][j]] = histo[pixel[i][j]] + 1
        return histo

def thumbnails(directory):
    img_format = ['jpg', 'png', 'gif']
    img_format_O = ['JPEG', 'PNG', 'GIF']
    for frmt in img_format:
        for img_address in glob.glob(directory+'\\*.'+frmt):
            img = Image.open(img_address)
            img.thumbnail((128, 128), Image.ANTIALIAS)
            img_name = img_address.replace(directory + '\\', '')

            if img_name[0:2] != 'T_':
                img_address_new = img_address.replace(directory + '\\', directory + '\\T_')
                for i in range(3):
                    if frmt == img_format[i]:
                        img.save(img_address_new, img_format_O[i])

