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
	pace(df)
	plot.distribution(df, "Average Pace (min/mile)")
	
	return


def temp(df):
	''' Plot temperature data'''

	variable = "Temperature (F)"

	plot.single_variable_time_series(df, variable, 'r')

	return


def hr(df):
	''' Plot heart rate data'''

	variable = "GARMIN Average HR (bpm)"

	plot.single_variable_time_series(df, variable, 'r')
	plot.multi_variable_time_series(df, variable)

	return


def pace(df):
	''' Plot pace data'''

	df = data_manipulations.convert_pace(df)

	variable = "Pace (min per mile)"

	plot.single_variable_time_series(df, variable, 'g')
	plot.multi_variable_time_series(df, variable)

	runtypes = ["Recovery", "General aerobic", "Threshold", "Medium long", "Long run"]

	for runtype in runtypes:
		df1 = data_manipulations.select_run_type(df, [runtype])
		plot.year_over_year(df1, variable, runtype)

	return


if __name__ == '__main__':
	main()
