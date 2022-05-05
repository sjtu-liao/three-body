

from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import layers
from sklearn.preprocessing import MinMaxScaler,StandardScaler,MaxAbsScaler
import numpy as np

#input the data path and load the mass data #
data=np.loadtxt(r'',delimiter=' ',dtype='float')


#do the data normalization
scaler=StandardScaler()
data0=np.loadtxt(r'case1_periodic_orbit.dat',delimiter=' ',dtype='float')
data1=data0[:,0:7]
mdata=data1[:,0:2]
status = data1[:,3:7]
dataSet_size=len(status)

x_train=scaler.fit_transform(mdata)
x_test=scaler.transform(data[:,0:2])
status_train=scaler.fit_transform(status)

#load the trained model
trained_model=load_model('case1_model.h5')

#predict the initial conditions and period for the periodic orbits
prediction=scaler.inverse_transform(trained_model.predict(x_test))






