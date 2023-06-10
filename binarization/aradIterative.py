from PIL import Image
img = Image.open('image1.png').convert('L').copy()
width, height = img.size
windowLength = (25,25)
for i in range(0, width, windowLength[0]):
    print(i)
    for j in range(0, height, windowLength[1]):

        histogram = [0 for x in range(256)]

        lenw = windowLength[0] if i + windowLength[0] <= width else width - i
        lenh = windowLength[1] if j + windowLength[1] <= height else height - j

        for x in range(i,i+lenw):
            for y in range(j,j+lenh):
                for p in range(256):
                    if p == img.getpixel((x,y)):
                        histogram[p] += 1

        histogram = [p / (windowLength[0] * windowLength[1]) for p in histogram]

        T = 128
        for ii in range(1000):
            e1 = []
            for iii in range(T):
                e1.append((iii+1) * histogram[iii])
            e1 = sum(e1)

            e2 = []
            for iii in range(T,256):
                e2.append((iii + 1) * histogram[iii])
            e2 = sum(e2)

            Ttmp = int((e1 + e2) / 2)
            if abs(Ttmp - T) < 0.0000001 :
                break
            T = Ttmp

        for x in range(i, i + lenw):
            for y in range(j, j + lenh):
                if img.getpixel((x,y)) > T :
                    img.putpixel((x,y),255)
                else:
                    img.putpixel((x, y), 0)


img.save('arad.png')
