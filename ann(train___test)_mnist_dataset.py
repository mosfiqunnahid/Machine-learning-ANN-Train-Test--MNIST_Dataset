# -*- coding: utf-8 -*-
"""ANN(Train | Test)-MNIST_Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RRwWMyXzgow9tbpIngACdXvUPhyFOlus
"""

import keras
import numpy as np
import pandas as pd
from keras.layers import Dense
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.utils import to_categorical
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

mnist = pd.read_csv('/content/sample_data/mnist_train_small.csv').iloc[:,:].values
mnist

y = mnist[:,0]
x = mnist[:,1:]
y

y_ = to_categorical(y)
print(y_)

y_.shape

temp = x[0]
temp.shape

temp = temp.reshape(28,28)
temp.shape

plt.imshow(temp)

model = Sequential()
model.add(Dense(250, input_dim=784, activation = 'relu'))
model.add(Dense(200, activation = 'relu'))
model.add(Dense(100, activation = 'relu'))
model.add(Dense(50, activation = 'relu'))
model.add(Dense(10,  activation = 'softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

model.summary()

X_train,X_test,y_train,y_test = train_test_split(x,y_,shuffle = True, test_size = 0.1)

history = model.fit(X_train,y_train, validation_data=(X_test,y_test),epochs=80,batch_size =150)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model acc')
plt.ylabel('acc')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

test_data = pd.read_csv('/content/sample_data/mnist_test.csv').iloc[:,:].values
test_y = test_data[:,0]
test_x = test_data[:,1:]
test_y

pred = model.predict(test_x)

pred[0]

temp = []
for i in pred:
  temp.append(np.argmax(i))
temp = np.array(temp)

temp

acc = accuracy_score(temp, test_y)
print(acc)

wrong = []
for i in range (len(test_y)):
  if test_y[i] != temp[i]:
     wrong.append(i)
print(wrong)

for i in range(1,10):
  pos = wrong[i-1]
  plt.subplot(3,3,i)
  plt.imshow(test_x[pos].reshape(28,28))
  plt.title(temp[pos])