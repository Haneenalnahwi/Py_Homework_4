from PIL import Image

def grey(image):
    img = Image.open(image)
    grey_img = img.convert("L")
    return grey_img


