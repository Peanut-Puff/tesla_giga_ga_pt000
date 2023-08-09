from keras.models import load_model
import cv2
import numpy as np
import os


def predict(model_name="tesla_giga_ga_pt000/model/model.h5"):
    os.chdir('C:/Users/luuux/Desktop/tasks/w1')
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(model_name, compile=False)

    dir = os.listdir('tesla_giga_ga_pt000/data/collector')
    data = np.ndarray(shape=(len(dir), 224, 224, 3), dtype=np.float32)
    images = []
    img_shape = (224, 224)
    results = []
    i = 0

    # 打开图片
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

    # Predicts the model
    results = model.predict(data)

    for index in range(len(results)):
        if results[index] == 1:
            cv2.imwrite('tesla_giga_ga_pt000/data/predict/car/' + dir[index], images[index])
        else:
            cv2.imwrite('tesla_giga_ga_pt000/data/predict/non_car/' + dir[index], images[index])
        os.remove('tesla_giga_ga_pt000/data/collector/'+dir[index])

if __name__ == '__main__':
    predict()

