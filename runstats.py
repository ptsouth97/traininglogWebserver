#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations
import plot

def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)

	#df = data_manipulations.convert_pace(df)
	#print(df)
	#run_type = "Recovery"
	#df = data_manipulations.select_run_type(df, [run_type])

	hr(df)
	#pace(df)
	#pace_by_run_type(df)
	
	return


def hr(df):
	''' Plot heart rate data'''

	variable = "GARMIN Average HR (bpm)"

	plot.single_variable_time_series(df, variable, 'r')

	return


def pace(df):
	''' Plot pace data'''

	df = data_manipulations.convert_pace(df)

	variable = "Pace (min per mile)"

	plot.single_variable_time_series(df, variable, 'g')

	return


def pace_by_run_type(df):
	''' Plot pace data by the type of run'''

	df = data_manipulations.convert_pace(df)

	variable = "Pace (min per mile)"

	runtype1 = ["Recovery"]
	df1 = data_manipulations.select_run_type(df, runtype1)

	runtype2 = ["Threshold"]
	df2 = data_manipulations.select_run_type(df, runtype2)

	fig = plt.figure()
 
	ax1 = df1[variable].dropna().plot(marker='.', linewidth=1, color='m', legend=True, label="Recovery runs")
	ax1 = df2[variable].dropna().plot(marker='.', linewidth=1, color='c', legend=True, label="Long runs")

	plt.title(variable + ' Comparison by run type')
	plt.xlabel('Date')
	plt.ylabel(variable)

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + variable + " Comparison by run type.png")
	plt.close()

	return


if __name__ == '__main__':
	main()
