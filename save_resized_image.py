import cv2

#image = cv2.imread('Images/colours-transparent.png', flags=1)

#save in grascale
image = cv2.imread('Images/colours-transparent.png', flags=0)
print(image.shape)

reduced_image=cv2.resize(image, (0,0), fx=0.2, fy=0.2)

print(reduced_image.shape)

cv2.imshow('image', reduced_image)

#writing image to file
cv2.imwrite('Images/reduced_image_grayscale.png', reduced_image)

cv2.waitKey(0)
cv2.destroyAllWindows()