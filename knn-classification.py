#!/usr/bin/python3

import pandas as pd
from pandas.plotting._misc import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import load
import data_manipulations
from matplotlib.patches import Patch



def main():
	''' main function for testing'''
	
	filename = "trainingLog.csv"
	df = load.to_df(filename)

	variables = ['Run type', 'GARMIN Average HR (bpm)', 'Average Pace (min/mile)', 'Average Cadence (spm)', 'Average Power (W)']
	

	data = df[variables].dropna()
	data = data_manipulations.convert_pace(data)

	target_variable = 'Run type'
	predictor_variables = ['GARMIN Average HR (bpm)', 'Pace (min per mile)', 'Average Cadence (spm)', 'Average Power (W)']

	y = data[target_variable]

	df = data[predictor_variables] 
	
	fig = plt.figure()
	fig.set_figheight(12)
	fig.set_figwidth(8)

	ax1 = plt.subplot(1, 1, 1) #, frameon=True)

	#fig, ax = plt.subplots()
	plt.style.use('ggplot')

	colors = {'Recovery':'red', 'Threshold':'orange', 'Medium long':'green', 'Long run':'blue', 'VO2 max':'yellow', 'General aerobic':'black', 'Progression':'cyan', 'Race':'magenta', 'Intervals':'0.8'}

	color_map = data['Run type'].map(colors)

	ax1 = scatter_matrix(df, c=color_map, figsize = [8,8], s=150, marker='D')

	#ax2 = plt.subplot(2, 1, 2)

	red = Patch(facecolor='red', edgecolor='r', label='Recovery')
	#orange = mpatches.Patch(color='orange', label='Threshold')

	#ax2.legend(handles=[red], loc='center')
	#_ = ax.add_artist(legend)
	
	#plt.tight_layout()
	plt.show()

	plt.savefig("/home/ocros03/Website/static/scatter_matrix.png")
	plt.close()
	

	#print(df)
	#print(df.shape)
	#print(df.keys())
	#print(type(df.HRV))
	'''
	X = np.array(data[predictor_variables])
	#print(predictor)
	#print(type(predictor)

	
	y = np.array(data[target_variable])

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)
	
	knn = KNeighborsClassifier(n_neighbors=5)

	knn.fit(X_train, y_train)

	y_pred = knn.predict(X_test)

	print("Test set predictions: \n {}".format(y_pred))

	print(X_test)

	print(knn.score(X_test, y_test))
	'''
	return


if __name__ == '__main__':
	main()
