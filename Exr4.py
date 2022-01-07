import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(650,650))
    row ,col = frame.shape[:2]
    frame_blur = cv2.blur(frame,(40,40))
    Dominant = frame[row//2-50:row//2+50,col//2-50:col//2+50]
    cv2.rectangle(frame_blur,(row//2-50,col//2-50),(row//2+50,col//2+50),(0,255,0),4)
    frame_blur[row//2-50:row//2+50,col//2-50:col//2+50] = Dominant
    ColorA = int(np.mean(Dominant[:,:,2]))
    ColorB = int(np.mean(Dominant[:,:,1]))
    ColorC = int(np.mean(Dominant[:,:,0]))
    
    if ColorC>170 and ColorB>170 and ColorA>170:
        color = 'White'
    elif ColorC<=50 and ColorB<=50 and ColorA<=50:
        color='Black'
    elif 50<ColorC<=170 and 50<ColorB<=170 and 50<ColorA<=170:
        color = 'Gray'
    elif ColorA>150 and ColorB<40 and ColorC<40:
        color='Red'
    elif ColorA<70 and ColorB>160 and ColorC<70:
        color='Green'
    elif ColorA<50 and ColorB<50 and ColorC>180:
        color = 'Blue'
    elif ColorA<50 and ColorB>150 and ColorC>170:
        color ='Cyan'
    elif ColorA>170 and ColorB<50 and ColorC>170:
        color='Purple'
    elif ColorA>170 and ColorB>150 and ColorC<50:
        color='Yellow'
    

    cv2.putText(frame_blur,f"Color: {color}",(10,70),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,0,0),2)  
    cv2.imshow("frame",frame_blur)
    if cv2.waitKey(1) & 0xFF==ord("0"):
        break

cap.release()
cv2.destroyAllWindows()
