import cv2

# Read image
image = cv2.imread('Images/jj-1.jpg')

# Show image
cv2.imshow('Image', image)

# Wait for key to be pressed
cv2.waitKey(0)

#distroy all windows
cv2.destroyAllWindows()

