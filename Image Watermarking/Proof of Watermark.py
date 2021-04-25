from PIL import Image

if __name__ == '__main__':
    image = Image.open("image_withWatermark.png")
    s = width, height = image.size
    imd = image.load()

    oldimage = Image.new('1', s)
    oldimaged = oldimage.load()

    for m in range(width):
        for n in range(height):
            d = imd[m, n]
            oldimaged[m, n] = 255 * (d[-1] & 1)

    from os.path import splitext

    basefile, extension = splitext("image_watermark.png")
    fileName = basefile + '_extractedQRCode' + extension
    oldimage.save(fileName)

