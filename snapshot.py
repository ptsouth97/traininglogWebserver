#!/usr/bin/python3

import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np
import load


def main():
	''' main function for testing'''

	df = load.to_df('trainingLog.csv')

	df = filter_dates(df, pd.Timestamp.today() - timedelta(7), pd.Timestamp.today())
	print(df)
	return


def filter_dates(df, start, end):
	''' Selects a range of dates based on user input'''

	df = df.loc[start:end]

	return df


def select_run_type(df, run_type):
	''' select specific type of run only from dataframe'''

	df = df.loc[df['Run type'].isin(run_type)]

	return(df)


def convert_pace(df):
	''' converts 0:8:30 min/mile to 8.5 min/mile'''

	df['datetime'] = pd.to_datetime(df['Average Pace (min/mile)'])
	df['minutes'] = df['datetime'].dt.minute
	df['seconds'] = (df['datetime'].dt.second)/60
	df['Pace (min per mile)'] = round(df['minutes'] + df['seconds'], 2)

	return df


def convert_time(df):
	''' converts time of 1:30:00 to 1.5'''
	
	df['datetime'] = pd.to_datetime(df['Time'], errors='ignore')
	df['hours'] = df['datetime'].dt.hour
	df['minutes'] = (df['datetime'].dt.minute)/60
	df['seconds'] = (df['datetime'].dt.second)/60/60
	df['Duration (hrs)'] = round(df['hours'] + df['minutes'] + df['seconds'], 2)

	
def convert_sleep(df):
	''' converts 8:30:00 hours of sleep to 8.5 hours of sleep'''

	df['datetime'] = pd.to_datetime(df['WHOOP Total Hours of Sleep'])
	df['hours'] = df['datetime'].dt.hour
	df['minutes'] = (df['datetime'].dt.minute)/60
	df['seconds'] = (df['datetime'].dt.second)/60/60
	df['Total Hours of Sleep'] = round(df['hours'] + df['minutes'] + df['seconds'], 2)

	return df


def two_variable_correlation(df, variable1, variable2):
	''' Plots one variable versus another to test correlation'''

	# Exclude outliers in the 1% range
	q1 = df[variable1].quantile(0.9)
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
	plt.savefig("/home/ocros03/Website/static/regression.png")
	plt.close()
	
	return


if __name__ == '__main__':
	main()
