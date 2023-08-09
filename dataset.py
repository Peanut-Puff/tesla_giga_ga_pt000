import os
from typing import Tuple

import cv2
import numpy as np


def load_set(data_path: str, img_shape: Tuple[int, int]):
    car_dirs = sorted(os.listdir(os.path.join(data_path, 'car')))
    non_car_dirs = sorted(os.listdir(os.path.join(data_path, 'non_car')))
    train_car_cnt=int(len(car_dirs)*0.8)
    test_car_cnt=len(car_dirs)-train_car_cnt
    train_non_car_cnt=int(len(non_car_dirs)*0.8)
    test_non_car_cnt=len(non_car_dirs)-train_non_car_cnt
    train_images = []
    test_images=[]
    for i, car_dir in enumerate(car_dirs):
        name = os.path.join(data_path, 'car', car_dir)
        car = cv2.imread(name)
        if car is None:
            print(name)
        if i >= train_car_cnt:
            test_images.append(car)
        else:
            train_images.append(car)

    for i, non_car_dir in enumerate(non_car_dirs):
        name = os.path.join(data_path, 'non_car', non_car_dir)
        non_car = cv2.imread(name)
        if non_car is None:
            print(name)
        if i >= train_non_car_cnt:
            test_images.append(non_car)
        else:
            train_images.append(non_car)

    for i in range(len(train_images)):
        train_images[i] = cv2.resize(train_images[i], img_shape)
        train_images[i] = train_images[i].astype(np.float32) / 255.0

    for i in range(len(test_images)):
        test_images[i] = cv2.resize(test_images[i], img_shape)
        test_images[i] = test_images[i].astype(np.float32) / 255.0
    return np.array(train_images),np.array(test_images),train_car_cnt,train_non_car_cnt,test_car_cnt,test_non_car_cnt


def get_car_set(
        data_root: str,
        img_shape: Tuple[int, int] = (224, 224),
        format='nhwc'
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:

    train_X,test_X,train_car_cnt,train_non_car_cnt,test_car_cnt,test_non_car_cnt = load_set(data_root, img_shape)

    train_Y = np.array([1] * train_car_cnt + [0] * train_non_car_cnt)
    test_Y = np.array([1] * test_car_cnt + [0] * test_non_car_cnt)

    if format == 'nhwc':
        return train_X, np.expand_dims(train_Y,
                                       1), test_X, np.expand_dims(test_Y, 1)
    elif format == 'nchw':
        train_X = np.reshape(train_X, (-1, 3, *img_shape))
        test_X = np.reshape(test_X, (-1, 3, *img_shape))
        return train_X, np.expand_dims(train_Y,
                                       1), test_X, np.expand_dims(test_Y, 1)
    else:
        raise NotImplementedError('Format must be "nhwc" or "nchw". ')
