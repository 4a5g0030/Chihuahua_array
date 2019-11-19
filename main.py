import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == '__main__':

    gyy = cv2.imread("gyy.jfif")
    out_img = None

    for i in np.arange(3):
        image = None
        for j in np.arange(3):
            if j == 0:
                image = cv2.flip(gyy, 1)
            elif j % 2 == 0:
                image = np.concatenate((image, cv2.flip(gyy, 1)), axis=1)
            else:
                image = np.concatenate((image, gyy), axis=1)
        if i == 0:
            out_img = image
        else:
            out_img = np.concatenate((out_img, image))

    cv2.imwrite("./gyyarray.jpg", out_img)