#Photo Manipulation

# import opencv
import cv2

# Read the original image
image = cv2.imread('Scenery.jpg')

# Define the desired height and width
desired_height = 500
desired_width = 300

# Resize the original image
resized_original = cv2.resize(image, (desired_width, desired_height))

# Convert the original image to grayscale
gray_image = cv2.cvtColor(resized_original, cv2.COLOR_BGR2GRAY)

# Resize the grayscale image
resized_gray = cv2.resize(gray_image, (desired_width, desired_height))

# Display the original and resized images
cv2.imshow('Original Image', resized_original)
cv2.imshow('Resized Grayscale Image', resized_gray)
cv2.waitKey(0)

cv2.destroyAllWindows()
