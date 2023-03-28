import cv2

# Configurable parameters
source = "amit.jpg"
destination = "newImage.png"
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# percent by which the image is resized
scale_percent = 50

# cv2.imshow("Amitesh", src)
# cv2.waitKey(0)


# calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)
