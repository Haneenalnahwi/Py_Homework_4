import IP_Model as ip

img = 'SierraSunset.Over.Deluxe.JPG'
im = ip.ImageProcessing(img)
grey_img = im.grey()
grey_img.show()
print('\n')
print('The Histogram of the image is: ', '\n', im.histogram())
print('\n')
dir = 'current'
ip.thumbnails(dir)

