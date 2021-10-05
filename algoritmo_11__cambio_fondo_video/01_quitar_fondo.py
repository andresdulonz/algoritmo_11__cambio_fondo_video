import cv2
from time import sleep

# Abrir archivos de imagen y video
cap = cv2.VideoCapture('video_1.mp4')
img_fondo = cv2.imread('desierto.jpg')

# Ancho y alto del video
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Code para archivo de video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Archivo de salida
# 30 --> fps
out = cv2.VideoWriter('new_video_5_seg.mp4', fourcc, 30, (w,h))

# Mostrar todo el video
for i in range(150): # revisar que el video esté abierto
    ret, img = cap.read()
    # revisar que haya más frames
    if ret == False:
        break
    
    # Quirtar fondo
    img_fondo= cv2.resize(img_fondo, (w,h))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask_i = cv2.inRange(hsv,(50,45,160),(65,255,255))

    mask = cv2.bitwise_not(mask_i)
    img_2 = cv2.bitwise_and(img, img, mask=mask)

    img_3= cv2.bitwise_and(img_fondo, img_fondo, mask=mask_i)
    img_4= cv2.bitwise_or(img_3, img_2)

    cv2.imshow('Video nuevo fondo',img_4)
    # gravación del video
    out.write(img_4)
    
    # Salida con tecla ESC
    if cv2.waitKey(1) == 27:
        break
    
    sleep(1/30)
