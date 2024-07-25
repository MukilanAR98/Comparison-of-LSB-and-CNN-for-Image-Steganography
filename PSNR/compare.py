# USAGE
# python compare.py

# import the necessary packages
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import math

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	'''First we convert the images from unsigned 8-bit integers to floating point, that way we don’t run into any problems with modulus operations “wrapping around”.
	We then take the difference between the images by subtracting the pixel intensities.
	Next up, we square these difference (hence mean squared error, and finally sum them up.'''
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	#print (m)
	if m==0:
		psnr = 100
	else :
		psnr =  20 * math.log10(255 / math.sqrt(m))
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f , PSNR: %.2f " % (m, psnr))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()

# load the images -- the original, the original + extracted,
# and the original + photoshop
original = cv2.imread("images/secret.jpg")
extracted = cv2.imread("images/extracted.png")
#cipher = cv2.imread("images/ciphercnn.png")
#cover = cv2.imread("images/covercnn.png")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
extracted = cv2.cvtColor(extracted, cv2.COLOR_BGR2GRAY)
#cipher = cv2.cvtColor(cipher, cv2.COLOR_BGR2GRAY)
#cover = cv2.cvtColor(cover, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Original", original),("Extracted", extracted)

# loop over the images to plot them
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 2, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

# compare the images
#compare_images(cover, cipher, "Cover vs Cipher")
compare_images(original, extracted, "Original vs. Extracted")
#compare_images(original, original, "Original vs. Original")