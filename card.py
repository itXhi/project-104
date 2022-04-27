from unittest import TextTestResult
import cv2

img = cv2.imread("solar-system.jpg")


Text_to_show="sun"
cv2.putText(img,Text_to_show,(5,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=2,color=(225,225,225))

Text_to_show="mercury"
cv2.putText(img,Text_to_show,(110,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.6,color=(220,220,0))

Text_to_show="venus"
cv2.putText(img,Text_to_show,(200,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.6,color=(220,220,0))

Text_to_show="earth"
cv2.putText(img,Text_to_show,(280,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(220,220,0))

Text_to_show="mars"
cv2.putText(img,Text_to_show,(380,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(220,220,0))

Text_to_show="jupiter"
cv2.putText(img,Text_to_show,(580,400),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(220,220,0))

Text_to_show="saturn"
cv2.putText(img,Text_to_show,(777,320),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(220,220,0))

Text_to_show="neptune"
cv2.putText(img,Text_to_show,(950,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(220,220,0))


Text_to_show="uranus"
cv2.putText(img,Text_to_show,(1111,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(220,220,0))






cv2.imshow("output",img)

cv2.waitKey(0)



cv2.imwrite("solar-system.jpg",img)
