from PIL import Image, ImageGrab
import time
# from numpy import asarray

def takeScreenshot():
	image = ImageGrab.grab().convert('L') #converted to grayscale
	# image.show()
	return image

if __name__ == "__main__":
	time.sleep(2)
	image = takeScreenshot()
	data = image.load()
	print(data)

	# print(asarray(image))
 
    # Box for cactus
    for i in range(275, 325):
        for j in range(563, 650):
            data[i, j] = 0
    
    # Box for birds
    for i in range(250, 300):
        for j in range(410, 563):
            data[i, j] = 171

    image.show()