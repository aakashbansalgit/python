from PIL import Image

from sys import argv
from qrcode import make as QR

if __name__ == '__main__':
    QRCODE = QR("SECRETMESSAGE")
    qwidth, qheight = QRCODE.size

    image = Image.open("test.jpg")
    width, height = image.size

    if qwidth > width:
        QRCODE = QRCODE.resize((width, width))
    elif qheight > height:
        QRCODE = QRCODE.resize((height, height))
    qwidth, qheight = QRCODE.size

    imaged = image.load()
    for m in range(width):
        for n in range(height):
            d = imaged[m,n]
            imaged[m,n] = d[:-1] + ((d[-1] | 1) if QRCODE.getpixel((m % qwidth, n % qheight)) else (d[-1] & ~1),)


    from os.path import splitext

    basefile, extension = splitext("image.jpg")
    image.save(basefile + '_withWatermark.png')
    QRCODE.save(basefile +'_theQRCodeUsed'+'.png')

