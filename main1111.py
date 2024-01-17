import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# 图像文件夹路径
folder_A = 'C:/Users/lch/Desktop/课题/yes or no/meiyou'
folder_B = 'C:/Users/lch/Desktop/课题/yes or no/you'

# 加载图像数据
train_images_A = [folder_A]
train_labels_A = [folder_A]
test_images_A = [folder_A]
test_labels_A = [folder_A]

train_images_B = [folder_B]
train_labels_B = [folder_B]
test_images_B = [folder_A]
test_labels_B = [folder_A]

# 文件夹 A 中的图像数据
for filename in os.listdir(folder_A):
    img = cv2.imread(os.path.join(folder_A, filename))
    img = cv2.resize(img, (32, 32))  # 调整图像大小为模型输入的尺寸
    img = img / 255.0  # 标准化图像数据
    if np.random.rand() < 0.8:  # 80% 的数据用于训练
        train_images_A.append(img)
        train_labels_A.append(0)  # 文件夹 A 对应的类别标签为 0
    else:
        test_images_A.append(img)
        test_labels_A.append(0)

# 文件夹 B 中的图像数据
for filename in os.listdir(folder_B):
    img = cv2.imread(os.path.join(folder_B, filename))
    img = cv2.resize(img, (32, 32))  # 调整图像大小为模型输入的尺寸
    img = img / 255.0  # 标准化图像数据
    if np.random.rand() < 0.8:  # 80% 的数据用于训练
        train_images_B.append(img)
        train_labels_B.append(1)  # 文件夹 B 对应的类别标签为 1
    else:
        test_images_B.append(img)
        test_labels_B.append(1)

# 转换为 NumPy 数组
train_images_A = np.array(train_images_A)
train_labels_A = np.array(train_labels_A)
test_images_A = np.array(test_images_A)
test_labels_A = np.array(test_labels_A)

train_images_B = np.array(train_images_B)
train_labels_B = np.array(train_labels_B)
test_images_B = np.array(test_images_B)
test_labels_B = np.array(test_labels_B)

# 创建并训练 CNN 模型
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images_A, train_labels_A, epochs=10, 
          validation_data=(test_images_A, test_labels_A))

# 评估模型性能
test_loss_A, test_acc_A = model.evaluate(test_images_A, test_labels_A, verbose=2)
print('\nTest accuracy for dataset A:', test_acc_A)

test_loss_B, test_acc_B = model.evaluate(test_images_B, test_labels_B, verbose=2)
print('\nTest accuracy for dataset B:', test_acc_B)