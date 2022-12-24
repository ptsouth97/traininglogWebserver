#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations
import plot
import numpy as np
from sklearn.linear_model import LinearRegression


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)

	variable1 = 'Average Power (W)'
	variable2 = 'GARMIN Average HR (bpm)'

	two_variable_correlation(df, variable1, variable2)

	return


def two_variable_correlation(df, variable1, variable2):
	''' Plots one variable versus another to test correlation'''

	# Exclude outliers in the 1% range
	q1 = df[variable1].quantile(0.99)
	df = df[df[variable1] < q1]

	q2 = df[variable2].quantile(0.99)
	df = df[df[variable2] < q2]

	df.plot(x=variable1, y=variable2, kind='scatter')

	df = df.dropna(subset=[variable1, variable2])

	column = df[variable1]
	upper_end = column.max()
	lower_end = column.min()

	reg = LinearRegression()
	prediction_space = np.linspace(lower_end, upper_end).reshape(-1,1)
	X = df[variable1].values.reshape(-1,1)
	y = df[variable2].values.reshape(-1,1)
	reg.fit(X,y)
	y_pred = reg.predict(prediction_space)

	r2 = reg.score(X, y)
	
	plt.plot(prediction_space, y_pred, color='red', linewidth=1)
	plt.title(variable2 + ' versus ' + variable1 + ', r^2=' + str(round(r2,2)))
	plt.savefig("/home/ocros03/Website/static/" + variable2 + " versus " + variable1 + ".png")
	plt.close()
	
	return

if __name__ == '__main__':
	main()
