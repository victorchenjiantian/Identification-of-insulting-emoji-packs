# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:08:10 2023

@author: Victor
"""


import keras
from keras import layers
import matplotlib.pyplot as plt
import numpy as np
import keras.datasets.mnist as mnist


(train_image,train_label),(test_image,test_label) = mnist.load_data()
print(train_image.shape)
print('efe')
plt.imshow(train_image[0])
plt.show()
print(train_label[0])
print('eee')
model = keras.Sequential()#初始化
model.add(layers.Flatten())
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(10,activation='softmax'))
model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics=['acc'])
model.fit(train_image,train_label,epochs=50,batch_size = 512)

model.evaluate(test_image,test_label)
y = np.argmax(model.predict(test_image[:10]),axis=1)
print('原始：',y)
print('结果：',test_label[:10])
