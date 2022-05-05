

import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import layers
from tensorflow.keras.callbacks import History 
from sklearn.preprocessing import MinMaxScaler,StandardScaler,MaxAbsScaler
import numpy as np


#load the data#
data=np.loadtxt(r'case1_classification.dat',delimiter=' ',dtype='float')
#This data has been shuffled#


#divide the data into training set, validation set and test set and do the data normalization
scaler=StandardScaler()
mdata=data[:,0:2]
status = data[:,2:5]
dataSet_size=len(status)
x_train0=mdata[0:np.int(dataSet_size*0.9),:]
x_train=scaler.fit_transform(x_train0)

x_val0=mdata[np.int(dataSet_size*0.9): np.int(dataSet_size*0.95),:]
x_val=scaler.transform(x_val0)
x_test0=mdata[np.int(dataSet_size*0.95): np.int(dataSet_size),:]
x_test=scaler.transform(x_test0)

status_train0=status[0:np.int(dataSet_size*0.9)]
status_val0=status[np.int(dataSet_size*0.9): np.int(dataSet_size*0.95)]
status_test0=status[np.int(dataSet_size*0.95): np.int(dataSet_size*1)]


#build uo the model

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(256,activation='relu',input_dim=2))
    
    model.add(layers.Dense(256,activation='relu'))
    model.add(layers.Dense(256,activation='relu'))
    model.add(layers.Dense(256,activation='relu'))
    model.add(layers.Dense(256,activation='relu'))
    model.add(layers.Dense(256,activation='relu')) 
    model.add(layers.Dense(3,activation='softmax'))
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3,amsgrad=True,decay=0.008),
                 loss= 'categorical_crossentropy',
               metrics = ['accuracy'])
    return model

model = build_model()


earlystop=tf.keras.callbacks.EarlyStopping(monitor='accuracy', patience=100, verbose=0, mode='max')

model_path=''# the path to save the model
checkpoint=tf.keras.callbacks.ModelCheckpoint(model_path,monitor='val_accuracy',save_best_only=True,mode='max')
#train the model#
history1 = model.fit(x_train,status_train0,callbacks=[earlystop,checkpoint],
                  epochs=5000,validation_data=(x_val,status_val0))


##Load the trained model and use the trained model to chassify the orbits of any masses#

model_path1='case1_classify_model.h5' 
trained_model=load_model(model_path1)
pred=trained_model.predict(x_test)
trained_model.evaluate(x_test,status_test0)


