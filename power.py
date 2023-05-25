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
	
	avgPower(df)
	efficiencyIndex(df)
	efficiencyFactor(df)
	intensityFactor(df)
	powerVariableByRunType(df, "Average Power (W)")

	return


def avgPower(df):
	''' Plot average power data'''

	variable = 'Average Power (W)'

	plot.single_variable_time_series(df, variable, 'r', 'No')

	return


def efficiencyIndex(df):
	''' EI = Avg Speed / Avg Power, i.e., what is your speed per watt?'''

	variable = 'Efficiency Index'

	df = data_manipulations.convert_pace(df)

	df[variable] = df['Pace (min per mile)'] / df['Average Power (W)']

	plot.single_variable_time_series(df, variable, 'b', 'No')

	return


def efficiencyFactor(df):
	''' EF = Average Power divided by Average Heart Rate, i.e., how aerobically efficient is your running?'''

	variable = 'Efficiency Factor'

	df[variable] = df['Average Power (W)'] / df['GARMIN Average HR (bpm)']

	plot.single_variable_time_series(df, variable, 'g', 'No')

	return


def intensityFactor(df):
	''' Critical Power divided by Average Power, i.e., how hard are you running?'''

	variable = 'Intensity Factor'

	df[variable] =  df['Average Power (W)'] / df['Functional Threshold Power (rFTPw)']

	plot.single_variable_time_series(df, variable, 'b', 'No')

	return


def powerVariableByRunType(df, variable):
	''' Average Power divided by Average Heart Rate sorted by run type'''

	#variable = 'Efficiency Factor by run type'
	
	if variable == "Efficiency Factor by run type":
		df[variable] = df['Average Power (W)'] / df['GARMIN Average HR (bpm)']

	runtype1 = ["Recovery"]
	df1 = data_manipulations.select_run_type(df, runtype1)

	runtype2 = ["Long run","Medium long"]
	df2 = data_manipulations.select_run_type(df, runtype2)

	runtype3 = ["General aerobic"]
	df3 = data_manipulations.select_run_type(df, runtype3)
	
	runtype4 = ["Threshold"]
	df4 = data_manipulations.select_run_type(df, runtype4)

	plt.style.use("ggplot")

	fig = plt.figure()

	ax1 = df1[variable].dropna().plot(marker='.', linewidth=1, color='m', legend=True, label="Recovery runs")
	ax1 = df2[variable].dropna().plot(marker='.', linewidth=1, color='c', legend=True, label="Long runs")
	ax1 = df3[variable].dropna().plot(marker='.', linewidth=1, color='g', legend=True, label="General aerobic runs")
	ax1 = df4[variable].dropna().plot(marker='.', linewidth=1, color='r', legend=True, label="Threshold runs")

	plt.suptitle(variable + ' by run type', fontsize=14, fontweight="bold")
	title = getTitle(variable)

	plt.title(title, fontsize=10, loc="left")
	#plt.title('What is the difference in power between different types of runs?', fontsize=10, loc="left")
	plt.xlabel('Date')
	plt.ylabel(variable)

	os.chdir('./static')
	plt.savefig(variable + ' by run type.png')
	plt.close()
	os.chdir('..')

	return


def getTitle(variable):
	''' Returns the correct chart title based on the variable'''

	if variable =='Average Power (W)':
		title = 'What is the difference in power between different types of runs?'
	elif variable == 'Efficiency Factor by run type':
		title = 'How aerobically efficient is your running? (EF=AvgPwr/AvgHR)'
	

	return title


if __name__ == '__main__':
	main()
