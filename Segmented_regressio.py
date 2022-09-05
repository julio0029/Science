#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
-------------------------------------------------------------------------------
Copyright© 2021 Jules Devaux / Cody Williams. All Rights Reserved
Open Source script under Apache License 2.0
-------------------------------------------------------------------------------
'''

PLOTTING=False

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate

# Read the data
df=pd.read_csv("Cristae Thickness.csv").astype('float64')

for tissue_prep in ['Intact', 'Permeabilised']:
	x=df['Temperature'].to_numpy()
	y=df[tissue_prep].to_numpy()

	tck = interpolate.splrep(x, y, k=2, s=0)
	xnew = np.linspace(x.min(), x.max())

	# Plot the data
	if PLOTTING is True:
		fig, axes = plt.subplots(3)

		axes[0].plot(x, y, 'x', label = 'data')
		axes[1].plot(x, interpolate.splev(x, tck, der=1), label = '1st dev')
		dev_2 = interpolate.splev(x, tck, der=2)
		axes[2].plot(x, dev_2, label = '2st dev')

		turning_point_mask = dev_2 == np.amax(dev_2)
		axes[2].plot(x[turning_point_mask], dev_2[turning_point_mask],'rx',
	             label = 'Turning point')
		for ax in axes:
		    ax.legend(loc = 'best')

		plt.show()
		
	print(f"{tissue_prep} break point: {x[turning_point_mask]}")

