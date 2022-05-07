import cv2



# Read image color image =1 or CV2.IMREAD_COLOR - default,
# grayscale image = 0 or CV2.IMREAD_GRAYSCALE
# doesn't include alpha channel - transparancy parameter
#image = cv2.imread('Images/jj-1.jpg', flags=0)

#flags = -1 as it is including alphs channel
image = cv2.imread('Images/colours-transparent.png', flags=-1)

# Display image shape
print(image.shape)
# Show image
cv2.imshow('Image', image)

# Wait for key to be pressed
cv2.waitKey(0)

#distroy all windows
cv2.destroyAllWindows()

