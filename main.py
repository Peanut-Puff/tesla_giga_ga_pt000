import os
from predict import predict
from db import db_util
from image import save_image,get_image
def main():
    os.chdir('C:/Users/luuux/Desktop/tasks/w1')
    save_dir='C:/Users/luuux/Desktop/tasks/w1/predict/'
    db=db_util()
    files=db.select_by_predict_result_null()
    for (id,file) in files:
        image=get_image(file)
        result=predict(file)
        if result==True:
            new_file_name=save_dir+'car/'+file.split('/')[-1]
        else:
            new_file_name=save_dir+'non_car/'+file.split('/')[-1]
        save_image(new_file_name,image)
        db.update_predict_result(id,result)


if __name__ == '__main__':
    main()
