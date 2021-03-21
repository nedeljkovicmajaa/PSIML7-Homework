from PIL import Image
image_path = input()
image = Image.open(image_path)
pixel = image.load()
red, green, blue = pixel[0,0]
print("Red: {0}".format(red))
print("Green: {0}".format(green))
print("Blue: {0}".format(blue))