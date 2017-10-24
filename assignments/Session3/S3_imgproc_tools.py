import cv2
import numpy as np 

img_gray = cv2.imread("cat.jpg",0)
img_bgr = cv2.imread("cat.jpg",1)

#display the matrix shapes
print("Gray levels image shape = "+ str(img_gray.shape))
print("BGR image shape = "+ str(img_bgr.shape))

#display the loaded images
cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)


def invert_colors_manual(input_image):
	"""
	Basic function able to inverse the color of an image manually
	"""
	img_inv = np.zeros(input_image.shape, dtype=np.uint8)

	if len(input_image.shape) == 3:
		for x in xrange(input_image.shape[0]):
			for y in xrange(input_image.shape[1]):
				for z in xrange(input_image.shape[2]):
					img_inv[x,y,z] = 255 - input_image[x,y,z]

	elif len(input_image.shape) == 2:
		for x in xrange(input_image.shape[0]):
				for y in xrange(input_image.shape[1]):
					img_inv[x,y] = 255 - input_image[x,y]

	return img_inv


def invert_colors_numpy(input_image):
	"""
	Basic function able to inverse the color of an image with numpy
	"""
	img_inv = (255 - input_image)
	return img_inv


def invert_colors_opencv(input_image):
	"""
	Basic function able to inverse the color of an image with opencv
	"""
	img_inv = cv2.bitwise_not(input_image)
	return img_inv

#inv_img = invert_colors_manual(img_bgr)
#inv_img = invert_colors_numpy(img_bgr)
#inv_img = invert_colors_opencv(img_bgr)

cv2.imshow("image", inv_img);

cv2.waitKey(0)
