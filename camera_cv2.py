import cv2
import time
import os
from db import db_util
def get_img(file_name=''):
    os.chdir('C:/Users/luuux/Desktop/tasks/w1')
    cap = cv2.VideoCapture(0)
    ret,frame=cap.read()
    # cv2.imshow('capture',frame)
    # cv2.waitKey(0)
    if file_name =='':
        file_name=str(time.time())
    path=os.path.join('tesla_giga_ga_pt000','data','collector',file_name+'.jpg')
    db=db_util()
    db.insert(file_name,path)
    return cv2.imwrite(path,frame)
    
if __name__ == '__main__':
    get_img()