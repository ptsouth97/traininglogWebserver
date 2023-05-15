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
	
	weight(df)
	calories(df)
	
	return


def weight(df):
	''' Plot weight data times series and year-over-year'''

	variable = 'Weight (pounds)'

	plot.year_over_year(df, variable)
	plot.single_variable_time_series(df, variable, "orange", 'No')

	return


def calories(df):
	''' Plot calorie data year-over-year'''

	variable = 'Calories consumed'

	plot.year_over_year(df, variable)
	plot.single_variable_time_series(df, variable, "purple", 'No')

	plt.style.use('ggplot')

	fig = plt.figure()
 
	#ax1 = df1[variable].dropna().plot(marker='.', linewidth=1, color='m', legend=True, label=runtype1)
	#ax1 = df2[variable].dropna().plot(marker='.', linewidth=1, color='c', legend=True, label=runtype2)
	
	calories1 = "WHOOP Activity Calories Burned"
	calories2 = "GARMIN Calories burned"
	calories3 = "Calories Burned (MET calculation)"

	df = df.dropna(subset=[calories1, calories2, calories3])

	df1 = df[calories1].rolling(30, min_periods=15).mean()
	ax1 = df1.plot(legend=True)

	df2 = df[calories2].rolling(30, min_periods=15).mean()
	ax1 = df2.plot(legend=True)

	df3 = df[calories3].rolling(30, min_periods=15).mean()
	ax1 = df3.plot(legend=True)

	plt.title('Calories Burned SMA-30 Comparison by method')
	plt.xlabel('Date')
	plt.ylabel('Calories Burned')

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + "Calories Burned Comparison by method.png")
	plt.close()

	return


if __name__ == '__main__':
	main()
