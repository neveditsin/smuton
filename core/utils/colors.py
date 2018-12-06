from PIL import Image
import numpy as np
from scipy.misc import imsave

img = Image.open("C:\\temp\\scan\\0001.jpg")

#Pixels higher than this will be 1. Otherwise 0.
THRESHOLD_VALUE = 128
img = img.convert("L")

imgData = np.asarray(img)
img = (imgData > THRESHOLD_VALUE) * 1.0


imsave("C:\\temp\\scan\\0002.jpg", img)

