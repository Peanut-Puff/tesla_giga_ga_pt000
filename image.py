import cv2
import os

def get_image(file_name):
    return cv2.imread(file_name)

def save_image(file_name,image):
    return cv2.imwrite(file_name,image)
