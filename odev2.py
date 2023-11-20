import cv2
import numpy as np

video = cv2.VideoCapture(0)


while True:
    true, matriks = video.read()

    hsv_donustur = cv2.cvtColor(matriks,cv2.COLOR_BGR2HSV)

    kirmizi1 = np.array([0,100,100])
    kirmizi2 = np.array([10,255,255])

    maskele = cv2.inRange(hsv_donustur,kirmizi1,kirmizi2)

    ortak = cv2.bitwise_and(matriks,matriks,mask=maskele)

    bgr_donustur = cv2.cvtColor(ortak,cv2.COLOR_HSV2BGR)

    cv2.imshow("renkli",matriks)

    cv2.imshow("kirmizi goruntu yakalama",ortak)

    cv2.imshow("beyaz goruntu",bgr_donustur)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()

cv2.destroyAllWindows()