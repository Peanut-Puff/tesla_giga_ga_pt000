import cv2
import time
from db import db_util
import config
def get_img(file_name=''):
    cap = cv2.VideoCapture(0)
    ret,frame=cap.read()
    if ret:
        if file_name =='':
            file_name=str(time.time())
        path=config.COLLECT_DIR+file_name+'.jpg'
        db=db_util()
        db.insert(file_name,path)
        return cv2.imwrite(path,frame)
    else:
        return False
    
if __name__ == '__main__':
    get_img()