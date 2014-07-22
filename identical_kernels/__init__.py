'''
Created on Jul 14, 2014
this file load data from pickle file pkl_path
and displays final boundary boxes for image with image_number
image_number is number from 0 to number of different images in pkl_path
final boxes is result of nms and bbox_maker algorithms
@author: timmy
'''

import pprint, pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib 
import random
import time

def make_image(image, size_new_image = 50):
    size_old_image = image.shape[0]
    step = round(size_new_image / size_old_image)
    new_image = np.zeros(shape=(size_new_image, size_new_image))
    for i in range(size_old_image):
        for j in range(size_old_image):
            for x in range(step):
                for y in range(step):
                    new_image[i * step + x, j * step + y] = image[i,j]
    return new_image

weights = np.load('/home/timmy/weights2.npy')
print(weights.shape)
n_weights = weights.shape[0]
weights = np.reshape(weights, newshape=(n_weights,5,5,32)) 
n_channels = 10
stepx = 60
stepy = 60
n_columns = 2
n_row = 16
for col in range(n_columns):
    for row in range(n_row):
        for channel in range(n_channels):
            d  = make_image(weights[row * n_columns +  col, :, :, channel])
            plt.figimage(d,cmap=plt.gray(),
                         xo = stepx * (channel   +  col * n_channels) + col * 50+ 20,
                         yo = stepy * row + 20)
plt.suptitle("figimage")

plt.show()
# def get_true_label(image_path):
#     """
#     getting true label
#     """
#     true_label = image_path.split('_')
#     true_label = true_label[-2]
#     true_label = true_label.split('/')
#     true_label = true_label[-1]
#     return true_label
#     
# def make_dictionary(class_list_path):
#     """
#      make dictionary of class
#     """
#     f = open(class_list_path)
#     lines = f.readlines()
#     class_names_dict = {}
#     for i in range(len(lines)):
#         name_class = lines[i].split()[0]
#         class_names_dict[name_class] = i # lines[i]
#     f.close()
#     return class_names_dict






