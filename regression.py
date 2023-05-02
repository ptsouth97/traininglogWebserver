#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations
import plot
import numpy as np
from sklearn.linear_model import LinearRegression
import csv


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)
	
	variables = ['Elevation (ft)', 'Temperature (F)', 'Humidity (%)',
				 'Feels like', 'Distance (miles)', 'Time', 
				 'Average Pace (min/mile)', 'GARMIN Average HR (bpm)',
				 'Average Cadence (spm)', 'Average Power (W)',
				 'Average Vertical Oscillation (cm)', 
				 'Average Ground Contact Time (ms)', 'Max HR',
				 'Average Stride Length (m)']

	counter = 0

	results = pd.DataFrame(columns=variables, index=variables)

	for variable1 in variables:
		for variable2 in variables:
			if variables.index(variable2) > counter:
				print("Calculating regression for " + variable1 + " and " + variable2)
				r2 = round(two_variable_correlation(df, variable1, variable2), 5)
				print(variable1 + ", " + variable2 + " -> r2 = " + str(r2))
				results[variable1][variable2] = r2
				results.to_csv('regression_results.csv')
		counter += 1

	return


def two_variable_correlation(df, variable1, variable2):
	''' Plots one variable versus another to test correlation'''

	# Exclude outliers in the 1% range
	'''
	q1 = df[variable1].quantile(0.1)
	df = df[df[variable1] > q1]

	q2 = df[variable2].quantile(0.9)
	df = df[df[variable2] < q2]
	'''
	df = df.dropna(subset=[variable1, variable2])
	print(df['Time'])
	if variable1 == 'Time':
		data_manipulations.convert_time(df)
		variable1 = 'Duration (hrs)'

	if variable2 == 'Time':
		data_manipulations.convert_time(df)
		variable2 = 'Duration (hrs)'

	if variable1 == 'Average Pace (min/mile)':
		data_manipulations.convert_pace(df)
		variable1 = 'Pace (min per mile)'

	if variable2 == 'Average Pace (min/mile)':
		data_manipulations.convert_pace(df)
		variable2 = 'Pace (min per mile)'

	print(df[variable2])
	df.plot(x=variable1, y=variable2, kind='scatter')

	#df = df.dropna(subset=[variable1, variable2])

	column = pd.to_numeric(df[variable1])
	upper_end = column.max()
	lower_end = column.min()

	reg = LinearRegression()
	prediction_space = np.linspace(lower_end, upper_end).reshape(-1,1)
	X = pd.to_numeric(df[variable1]).values.reshape(-1,1)
	y = pd.to_numeric(df[variable2]).values.reshape(-1,1)
	
	
	reg.fit(X,y)
	y_pred = reg.predict(prediction_space)

	r2 = reg.score(X, y)

	#plt.style.use("ggplot")	
	plt.plot(prediction_space, y_pred, color='red', linewidth=1)
	plt.title(variable2 + ' versus ' + variable1 + ', r^2=' + str(round(r2,2)))
	plt.savefig("/home/ocros03/Website/static/" + variable2 + " versus " + variable1 + ".png")
	plt.close()
	
	return r2

if __name__ == '__main__':
	main()
