import cv2
import numpy as np

large = cv2.imread('out.jpg')

rgb = cv2.pyrDown(large)

#rgb = (large)
cv2.imshow('image', cv2.resize(rgb,(1000,700)))
cv2.waitKey(0)

small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 15))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
# using RETR_EXTERNAL instead of RETR_CCOMP
_,contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

mask = np.zeros(bw.shape, dtype=np.uint8)
i = 1

height = rgb.shape[0]
width = rgb.shape[1]
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
    
    if r > 0.45 and w > 8 and h > 8 and y<(width/1.3) and x<(height/1.3) and w*h > (width/6)*(height/6):
    
        cv2.rectangle(rgb, (x-5, y-5), (x+w+5, y+h+5), (0, 255, 0), 1)
        cropped = rgb[y - 5:y +  h + 5 , x - 5 : x + w + 5]
        #print("box "+str(i) + " w ="+str(w) + " h="+str(h))

        s = 'img_'+str(i)+'.jpg'
        i=i+1
        cv2.imwrite(s , cropped)


cv2.imshow('rects', cv2.resize(rgb,(1000,700)))
cv2.waitKey(0)
cv2.destroyAllWindows()
