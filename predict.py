from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2
import numpy as np
import os

def predict():
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("tesla_giga_ga_pt000/model/model.h5", compile=False)

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    dir=os.listdir('tesla_giga_ga_pt000/data/collector')
    images=[]
    img_shape = (224, 224)
    results=[]
    # 打开图片
    for img_name in dir:
        image = cv2.imread(os.path.join('tesla_giga_ga_pt000/data/collector', img_name))
        if image is None:
            print(img_name)
        else:
            # resizing the image to be at least 224x224 and then cropping from the center
            image = cv2.resize(image, img_shape)
            # turn the image into a numpy array
            image_array = np.asarray(image)
            data[0]=image_array
            images.append(image)

            # Predicts the model
            prediction = model.predict(data)
            results.append(prediction)
    for index in range(len(results)):
        if results[index]==1:
            cv2.imwrite('tesla_giga_ga_pt000/data/predict/car/'+dir[index],images[index])
        else:
            cv2.imwrite('tesla_giga_ga_pt000/data/predict/non_car/'+dir[index],images[index])
        # os.remove('tesla_giga_ga_pt000/data/collector/'+dir[index])
