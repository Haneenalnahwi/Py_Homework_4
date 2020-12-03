from PIL import Image
import glob

def grey(image):
    img = Image.open(image)
    grey_img = img.convert("L")
    return grey_img

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
