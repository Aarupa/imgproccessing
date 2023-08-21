#image processing
#importing computer vision
import cv2
#load photo on to the Ram
photo=cv2.imread("C:\\Users\\admin\\Pictures\\pic1.jpeg")
#showing image in windows ,windows name as (my image)
cv2.imshow("my image",photo)
#it wait for 10 sec and open new shell
cv2.waitKey(10000)
#it distroy the image windows 
cv2.destroyAllWindows()