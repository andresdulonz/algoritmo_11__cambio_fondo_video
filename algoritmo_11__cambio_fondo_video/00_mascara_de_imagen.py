import cv2

img = cv2.imread('Captura.PNG')

im_fondo = cv2.imread('desierto.jpg')
h,w,_ = img.shape
im_fondo= cv2.resize(im_fondo, (w,h))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask_i = cv2.inRange(hsv,(50,45,160),(65,255,255))
mask = cv2.bitwise_not(mask_i)
img_2 = cv2.bitwise_and(img, img, mask=mask)

im3= cv2.bitwise_and(im_fondo, im_fondo, mask=mask_i)
img_4= cv2.bitwise_or(im3, img_2)

cv2.imshow('Imagen nuevo fondo',img_4)
cv2.waitKey(0)