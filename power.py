#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
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

	print("Calculating Average Power...")

	variable = 'Average Power (W)'

	plot.single_variable_time_series(df, variable, 'r', 'No')

	return


def efficiencyIndex(df):
	''' EI = Avg Speed / Avg Power, i.e., what is your speed per watt?'''

	print("Calculating Efficiency Index...")

	variable = 'Efficiency Index'

	df = data_manipulations.convert_pace(df)

	df[variable] = df['Pace (min per mile)'] / df['Average Power (W)']

	plot.single_variable_time_series(df, variable, 'b', 'No')

	return


def efficiencyFactor(df):
	''' EF = Average Power divided by Average Heart Rate, i.e., how aerobically efficient is your running?'''

	print("Calculating Efficiency Factor...")

	variable = 'Efficiency Factor'

	df[variable] = df['Average Power (W)'] / df['GARMIN Average HR (bpm)']

	plot.single_variable_time_series(df, variable, 'g', 'No')

	return


def intensityFactor(df):
	''' Critical Power divided by Average Power, i.e., how hard are you running?'''

	print("Calculating Intensity Factor...")

	variable = 'Intensity Factor'

	df[variable] =  df['Average Power (W)'] / df['Functional Threshold Power (rFTPw)']

	plot.single_variable_time_series(df, variable, 'b', 'No')

	return


def powerVariableByRunType(df):
	''' Power metrics sorted by run type'''

	print("Calculating power metrics by run type")

	metrics = ["Average Power (W)", "Efficiency Index", "Efficiency Factor", "Intensity Factor"]	

	df = data_manipulations.convert_pace(df)	

	df['Efficiency Index'] = df['Pace (min per mile)'] / df['Average Power (W)']
	df['Efficiency Factor'] = df['Average Power (W)'] / df['GARMIN Average HR (bpm)']
	df['Intensity Factor'] =  df['Average Power (W)'] / df['Functional Threshold Power (rFTPw)']

	runtype1 = ["Recovery"]
	df1 = data_manipulations.select_run_type(df, runtype1)

	runtype2 = ["Long run","Medium long"]
	df2 = data_manipulations.select_run_type(df, runtype2)

	runtype3 = ["General aerobic"]
	df3 = data_manipulations.select_run_type(df, runtype3)
	
	runtype4 = ["Threshold"]
	df4 = data_manipulations.select_run_type(df, runtype4)

	for metric in metrics:

		plt.style.use("ggplot")

		fig = plt.figure()

		ax1 = df1[metric].dropna().plot(marker='.', linewidth=1, color='m', legend=True, label="Recovery runs")
		ax1 = df2[metric].dropna().plot(marker='.', linewidth=1, color='c', legend=True, label="Long runs")
		ax1 = df3[metric].dropna().plot(marker='.', linewidth=1, color='g', legend=True, label="General aerobic runs")
		ax1 = df4[metric].dropna().plot(marker='.', linewidth=1, color='coral', legend=True, label="Threshold runs")

		plt.suptitle(metric + ' by run type', fontsize=14, fontweight="bold")
		title = getTitle(metric)

		plt.title(title, fontsize=10, loc="left")
		#plt.title('What is the difference in power between different types of runs?', fontsize=10, loc="left")
		plt.xlabel('Date')
		plt.ylabel(metric)

		#os.chdir('./static')
		path = '/home/ocros03/Website/static/'
		plt.savefig(path + metric + ' by run type.png')
		plt.close()
		#os.chdir('..')

	return


def getTitle(variable):
	''' Returns the correct chart title based on the variable'''

	if variable =='Average Power (W)':
		title = 'What is the difference in power between different types of runs?'
	elif variable == 'Efficiency Index':
		title = 'What is your speed per watt? (Avg Speed/Avg Pwr)'
	elif variable == 'Efficiency Factor':
		title = 'How aerobically efficient is your running? (EF=AvgPwr/AvgHR)'
	elif variable == 'Intensity Factor':
		title = 'How hard are your running? (Avg Pwr/Critical Pwr)'
	
	return title


if __name__ == '__main__':
	main()
