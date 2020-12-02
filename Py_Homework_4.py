from PIL import Image
import glob

def grey(image):
    img = Image.open(image)
    grey_img = img.convert("L")
    return grey_img

def thumbnails(directory):
    for img_address in glob.glob(directory + '\\*.jpg'):
        img = Image.open(img_address)
        img.thumbnail((128, 128), Image.ANTIALIAS)
        img_name = img_address.replace(directory + '\\', '')

        if img_name[0:2] != 'T_':
            img_address_new = img_address.replace(directory + '\\', directory + '\\T_')
            im.save(img_address_new, "JPEG")

