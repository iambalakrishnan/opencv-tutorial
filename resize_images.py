import cv2

image = cv2.imread('Images/colours-transparent.png', flags=1)

#original image size
print(image.shape)
# Resize the image
# 1st parameter is the source image
# 2nd parameter is the size of the image
#reduced_image=cv2.resize(image, (400,500))


#reduced_image=cv2.resize(image, (0,0), fx=0.3, fy=0.2) #fx and fy are the scaling factors

#fx = 0.3 - 30% of original width
#fy = 0.4 - 40% of original height

#reduced_image=cv2.resize(image, (0,0), fx=0.3, fy=1) # height as it is and reducing only width

# print(reduced_image.shape)
# cv2.imshow('image', reduced_image)


increased_image_2 = cv2.resize(image, (0,0), fx=3, fy=3) # increase width and height by 3 times
print(increased_image_2.shape)
cv2.imshow('image', increased_image_2)

cv2.waitKey(0)
cv2.destroyAllWindows()