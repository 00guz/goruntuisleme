import cv2
import numpy as np
from matplotlib import pyplot as plt

foto = cv2.imread("opencv.goruntuisleme/1.hafta/cicek.jpg")
cv2.imshow("papatya",foto)

gri_resim = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)  # gri seviye görüntüye dönüştürüyoruz

histogram = np.zeros(256)
uzunluk , genislik= gri_resim.shape
for i in range(uzunluk):
    for j in range(genislik):
        pixel = gri_resim[i, j]  
        histogram[pixel] += 1
        
plt.bar(range(256), histogram, color='yellow')
plt.title('Histogram tablosu',color = "blue")
plt.show()