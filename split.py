<<<<<<< HEAD
import cv2

def splitting(Video): 
    vidcap = cv2.VideoCapture(Video)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite('input/frames%d.jpg' %count, image)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count +=1 
=======
import cv2

def splitting(Video): 
    vidcap = cv2.VideoCapture(Video)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite('input/frames%d.jpg' %count, image)
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count +=1 
>>>>>>> 7fa3809cbe502936a4fc97d7ecdcce953ae3c237
