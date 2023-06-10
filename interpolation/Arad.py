import numpy
from PIL import Image

img = Image.open('InputImage.bmp')
newImg = Image.new(img.mode, (512, 512), 'white')
w, h = img.size
sw = 512 / w
sh = 512 / h
for x in range(512 - 1):
    for y in range(512 - 1):
        newImg.putpixel((x, y), img.getpixel((numpy.round(x / sw), numpy.round(y / sh))))
newImg.save('./Im_NNI.bmp')

############################

img = Image.open('InputImage.bmp')
newImg = Image.new(img.mode, (512, 512), 'white')
w, h = img.size
sw = w / 512
sh = h / 512
for i in range(512):
    for j in range(512):
        x = i * sw
        y = j * sh
        x1 = int(numpy.floor(x))
        x2 = min(w - 1, numpy.ceil(x))
        y1 = int(numpy.floor(y))
        y2 = min(h - 1, numpy.ceil(y))

        if x1 == x2 and y1 == y2:
            p = img.getpixel((int(x), int(y)))
        elif x1 == x2:
            tmp1 = img.getpixel((int(x), int(y1)))
            tmp2 = img.getpixel((int(x), int(y2)))
            p = tmp1 * (y2 - y) + tmp2 * (y - y1)
        elif y1 == y2:
            tmp1 = img.getpixel((int(x1), int(y)))
            tmp2 = img.getpixel((int(x2), int(y)))
            p = tmp1 * (x2 - x) + tmp2 * (x - x1)
        else:
            q00 = img.getpixel((int(x1), int(y1)))
            q01 = img.getpixel((int(x2), int(y1)))
            q10 = img.getpixel((int(x1), int(y2)))
            q11 = img.getpixel((int(x2), int(y2)))

            q1 = q00 * (x2 - x) + q01 * (x - x1)
            q2 = q10 * (x2 - x) + q11 * (x - x1)
            p = q1 * (y2 - y) + q2 * (y - y1)
        newImg.putpixel((i, j), int(p))
newImg.save('./Im_BLI.bmp')


##################
img1 = Image.open('OriginalImage.bmp')
img2 = Image.open('Im_NNI.bmp')
w,h  = img1.size
s=0
for i in range(w):
    for j in range(h):
        s += (img1.getpixel((i, j)) * img2.getpixel((i, j))) ** 2
print(s / (w * h))

##################
img1 = Image.open('OriginalImage.bmp')
img2 = Image.open('Im_BLI.bmp')
w,h  = img1.size
s=0
for i in range(w):
    for j in range(h):
        s += (img1.getpixel((i, j)) * img2.getpixel((i, j))) ** 2
print(s / (w * h))