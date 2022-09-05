import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate


df=pd.read_csv("Cristae Thickness.csv").astype('float64')

for ttype in ['Intact', 'Permeabilised']:
	x=df['Temperature'].to_numpy()
	y=df[ttype].to_numpy()



	tck = interpolate.splrep(x, y, k=2, s=0)
	xnew = np.linspace(x.min(), x.max())

	fig, axes = plt.subplots(3)

	axes[0].plot(x, y, 'x', label = 'data')
	#axes[0].plot(xnew, interpolate.splev(xnew, tck, der=0), label = 'Fit')
	axes[1].plot(x, interpolate.splev(x, tck, der=1), label = '1st dev')
	dev_2 = interpolate.splev(x, tck, der=2)
	axes[2].plot(x, dev_2, label = '2st dev')

	turning_point_mask = dev_2 == np.amax(dev_2)
	print(f"{ttype} break point: {x[turning_point_mask]}")
	axes[2].plot(x[turning_point_mask], dev_2[turning_point_mask],'rx',
	             label = 'Turning point')
	for ax in axes:
	    ax.legend(loc = 'best')


	plt.show()
