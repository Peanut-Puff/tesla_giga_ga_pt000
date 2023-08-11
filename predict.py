from keras.models import load_model
import cv2
import numpy as np
import os

def get_images(dir:str):
    images=[]
    data=np.ndarray(shape=(len(dir), 224, 224, 3), dtype=np.float32)
    img_shape = (224, 224)
    i = 0
    for img_name in dir:
        image = cv2.imread(os.path.join(
            'tesla_giga_ga_pt000/data/collector', img_name))
        if image is None:
            print(img_name)
        else:
            images.append(image)
            # resizing the image to 224x224 and normalize it
            image = cv2.resize(image, img_shape)
            image=image.astype(np.float32) / 255.0
            # turn the image into a numpy array
            image_array = np.asarray(image)
            data[i] = image_array
            i = i+1
    return data,images

def save_images(results,dir,images):
    for index in range(len(results)):
        if results[index] == 1:
            cv2.imwrite('tesla_giga_ga_pt000/data/predict/car/' + dir[index], images[index])
        else:
            cv2.imwrite('tesla_giga_ga_pt000/data/predict/non_car/' + dir[index], images[index])
        os.remove('tesla_giga_ga_pt000/data/collector/'+dir[index])

def predict(model_name="model.h5"):
    os.chdir('C:/Users/luuux/Desktop/tasks/w1')
    dir = os.listdir('tesla_giga_ga_pt000/data/collector')
    
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model('tesla_giga_ga_pt000/model/'+model_name, compile=False)

    # get images
    data,images=get_images(dir)

    # Predicts the model
    results = []
    results = model.predict(data)

    # save images
    save_images(results,dir,images)

if __name__ == '__main__':
    predict()

