import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
  
image = cv2.imread("opencv.goruntuisleme/4.hafta/odev3/pirinc.jpg") 
kucult = cv2.resize(image,(400,400))

gray = cv2.cvtColor(kucult, cv2.COLOR_BGR2GRAY) 
cv2.imshow("pencere",gray)

dondur,binary = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY) 
cv2.imshow("esikleme",binary)

kernel = np.ones((3, 3), np.uint8) 

erozyon = cv2.erode(binary, kernel, iterations=1) 
cv2.imshow("erozyon",erozyon)

blur = cv2.GaussianBlur(erozyon,(9,9),0) 
cv2.imshow("blur",blur)
  
say, bul = cv2.findContours(blur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
rgb = cv2.cvtColor(kucult, cv2.COLOR_BGR2RGB) 
cv2.drawContours(rgb, say, -1, (255, 165, 0), 2) 
cv2.imshow("cercevele",rgb)

print("ekrandaki pirinç sayısı: ", len(say))
  

cv2.waitKey(0)
