import cv2
import time
import os
def get_img(file_name=''):
    os.chdir('C:/Users/luuux/Desktop/tasks/w1')
    cap = cv2.VideoCapture(0)
    ret,frame=cap.read()
    # cv2.imshow('capture',frame)
    # cv2.waitKey(0)
    if file_name =='':
        path=os.path.join('tesla_giga_ga_pt000','data','collector',str(time.time())+'.jpg')
        return cv2.imwrite(path,frame)
    else:
        path=os.path.join('tesla_giga_ga_pt000','data','collector',file_name+'.jpg')
        return cv2.imwrite(path,frame)
    
if __name__ == '__main__':
    get_img()