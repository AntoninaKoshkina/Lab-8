import cv2

img = cv2.imread('variant-8.jpg')

height, width, _ = img.shape

center_x = width // 2
center_y = height // 2

crop_x = center_x - 200
crop_y = center_y - 200
crop_width = 400
crop_height = 400

cropped_img = img[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]

# Save the cropped image to a new file
cv2.imwrite('cropped_variant-8.jpg', cropped_img)
