import os
from predict import predict
from db import db_util
from image import save_image,get_image
import threading
import config

def main():
    global max
    save_dir=config.PREDICT_DIR
    db=db_util()
    mutex.acquire()
    files=db.select_by_predict_result_null(50,max)
    max=files[-1][0]
    print(max)
    mutex.release()
    for (id,file) in files:
        image=get_image(file)
        result=predict(image)
        if result==True:
            new_file_name=save_dir+'car/'+file.split('/')[-1]
        else:
            new_file_name=save_dir+'non_car/'+file.split('/')[-1]
        save_image(new_file_name,image)
        db.update_key_valaue(id,'predict_result',result)
        if id> max:
            print(id)

def init_data():
    db=db_util()
    dir=config.COLLECT_DIR
    for file in os.listdir(dir):
        db.insert(file.split('.')[0],dir+file)
    return

if __name__ == '__main__':
    # init_data()
    max=0
    mutex=threading.Lock()
    threads=[]
    for i in range(2):
        threads.append(threading.Thread(target=main))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
