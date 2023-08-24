from keras.models import load_model
import cv2
import numpy as np
import config

def predict(image,model_name="model.h5"):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(config.MODEL_DIR+model_name, compile=False)

    # resize & normalize
    img_shape = (224, 224)
    image = cv2.resize(image, img_shape)
    image=image.astype(np.float32) / 255.0

    image_array = np.asarray(image)
    data=np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = image_array

    # Predicts the model
    results = []
    results = model.predict(data)

    if results[0] == 1:
        return True
    else:
        return False