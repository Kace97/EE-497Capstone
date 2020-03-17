#!/usr/bin/env python
import cv2
import numpy as np
import keras
from keras.models import Model, load_model
from keras.layers import GlobalAveragePooling2D
import time
import Cartesian2Polar
from PIL import Image


model_name = 'models/borg_keras.h5'
t0 = time.time()
autoencoder = load_model(model_name)
encoder = Model(inputs=autoencoder.input, outputs=autoencoder.get_layer('encoder').output)
t1 = time.time()
print("Model loaded in: ", t1-t0)

enc_model = Model(autoencoder.input, autoencoder.get_layer('encoder').output)

x1 = enc_model.get_layer('encoder').output
x1 = GlobalAveragePooling2D(name='flat')(x1)
encoder = Model(enc_model.input, x1)


def expand_for_encoding(img):
	single = cv2.resize(img, (128,64))
	single = np.expand_dims(single, axis=2)
	single_scaled = single * 1. / 255
	single_scaled = np.expand_dims(single_scaled, axis=0)
	return single_scaled

im = Image.open('test_images/1.jpg')
pim = Cartesian2Polar.project_cartesian_image_into_polar_image(im, origin=None)

crop_height = min(150, pim.height)
crop_width = min(10000, pim.width)
cropped_polar_im = pim.crop(box=(0,0,crop_width,crop_height))

open_cv_image = np.array(cropped_polar_im)
open_cv_image = open_cv_image[:,:,::-1].copy()
img = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

img = expand_for_encoding(img)
encodings = encoder.predict(img, batch_size=1)
print(encodings)


