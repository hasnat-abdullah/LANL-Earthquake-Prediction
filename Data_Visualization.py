import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#==========Read data from train.csv file==========
data = pd.read_csv('train.csv', dtype={'acoustic_data': np.float32, 'time_to_failure': np.float64})
step = 1000

#==========Plot building===========
figure, axis1 = plt.subplots()
x_axis = np.arange(0, len(data), step)

#=========Plot axis initializing & labaling===========
axis1.plot(x_axis, data.iloc[:, 0][0::step], '-g')
axis1.set_ylabel('sequence')
axis1.set_ylabel('Seismic Activity', color='g')

#=========Plot axis initializing & labaling==========
axis2 = axis1.twinx()
axis2.plot(x_axis, data.iloc[:, 1][0::step], '-r')
axis2.set_ylabel('Time To Failure', color='r')

#==========plot showing=========
plt.show()

#==========Run complition dialog==========
print ("Complited")