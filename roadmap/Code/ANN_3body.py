

import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler,StandardScaler,MaxAbsScaler
import numpy as np

#input the datapath and load data
data0=np.loadtxt(r'',delimiter=' ',dtype='float')

data1=data0[:,0:7]
mdata=data1[:,0:2]
status = data1[:,3:7]
dataSet_size=len(status)

#do the data normalization
scaler=StandardScaler()
x_train=scaler.fit_transform(mdata)
status_train=scaler.fit_transform(status)

#build up the model
def build_model():
    model = models.Sequential()    
    model.add(layers.Dense(1024,activation='relu',input_dim=2))
    model.add(layers.Dense(1024,activation='relu'))
    model.add(layers.Dense(1024,activation='relu'))
    model.add(layers.Dense(1024,activation='relu'))
    model.add(layers.Dense(1024,activation='relu'))
    model.add(layers.Dense(1024,activation='relu'))
    model.add(layers.Dense(4))
    model.compile(optimizer=tf.keras.optimizers.Adam(amsgrad=True, learning_rate=0.001,decay=0.001),
                  loss= 'mse')
    return model
model = build_model()

# train the model#

history = model.fit(x_train,
                    status_train,
                    epochs=2000)


