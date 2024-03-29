#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
import load
import os
import data_manipulations
import numpy as np


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)
	#print(df)
	#power(df)

	overlay_time_series(df, 'HRV', 'Training Load')

	return


def distribution(df, variable):
	''' Plot histogram of average pace'''

	print("Creating distribution...")

	df = df.dropna(subset=variable)	

	if variable == 'Average Pace (min/mile)':
		data_manipulations.convert_pace(df)
		variable = 'Pace (min per mile)'

	q2 = df[variable].quantile(0.95)
	df = df[df[variable] < q2]

	plt.style.use('ggplot')
	binwidth = 0.25
	df.hist(column=variable, bins=np.arange(min(df[variable]), max(df[variable]) + binwidth, binwidth))

	plt.title('Histogram of ' + variable)
	
	#os.chdir('./static')
	path = "/home/ocros03/Website/static/"
	plt.savefig(path + 'Histogram of ' + variable + '.png')
	plt.close()
	#os.chdir('..')

	return


def year_over_year(df, variable, runtype=''):
	''' Plot single variable year-over-year data'''

	pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values=variable)	
	
	plt.style.use('ggplot')
	pv.plot(marker='.', linewidth=1)
	plt.title('Mean ' + runtype + ' ' + variable + ' Year-Over-Year Comparison',
		fontsize=12,
		pad=0,
		loc="left")
	plt.xlabel('Month')
	plt.ylabel(variable)

	#os.chdir('./static')
	path = "/home/ocros03/Website/static/"
	plt.savefig(path + 'Mean ' + runtype + ' ' + variable + ' Year-Over-Year Comparison.png')
	plt.close()
	#os.chdir('..')

	return


def single_variable_time_series(df, variable, color, vlines):
	''' Plot single variable time series'''

	df[variable].dropna().plot(marker='.', linewidth=1, color=color)

	plt.style.use('ggplot')

	df['SMA_30'] = df[variable].rolling(30, min_periods=15).mean()
	df['SMA_30'].plot(legend=True)

	#plt.figure(facecolor="yellow")

	#ax = plt.axes()
	#ax.set_facecolor("violet")
	
	plt.title(variable + ' changes over time', fontsize=14, pad=10, loc="left")
	plt.xlabel('Date')
	plt.ylabel(variable)

	if vlines == 'Yes':
		plt.axvline(x='2021-12-11', label='Kiawah marathon 2021', color='blue')
		plt.axvline(x='2022-12-10', label='Kiawah marathon 2022', color='green')

	plt.legend()
	plt.tight_layout()

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + variable + " changes over time.png")
	plt.close()
	#os.chdir("/home/ocros03/Website/")

	return


def multi_variable_time_series(df, variable):
	''' Plot data by the type of run'''
	
	# Turn off SettingWithCopyWarning (dataquest.io)
	pd.set_option('mode.chained_assignment', None)
	
	if variable == "Pace (min per mile)":
		df = data_manipulations.convert_pace(df)
	
	runtype1 = "Recovery"
	df1 = data_manipulations.select_run_type(df, [runtype1])
	
	runtype2 = "Threshold"
	df2 = data_manipulations.select_run_type(df, [runtype2])

	runtype3 = "Long run"
	df3 = data_manipulations.select_run_type(df, [runtype3])

	runtype4 = "General aerobic"
	df4 = data_manipulations.select_run_type(df, [runtype4])
	
	plt.style.use('ggplot')

	fig = plt.figure()
 
	#ax1 = df1[variable].dropna().plot(marker='.', linewidth=1, color='m', legend=True, label=runtype1)
	#ax1 = df2[variable].dropna().plot(marker='.', linewidth=1, color='c', legend=True, label=runtype2)

	df1[runtype1] = df1[variable].rolling(30, min_periods=15).mean()
	ax1 = df1[runtype1].plot(legend=True)

	df2[runtype2] = df2[variable].rolling(30, min_periods=15).mean()
	ax1 = df2[runtype2].plot(legend=True)

	df3[runtype3] = df3[variable].rolling(30, min_periods=15).mean()
	ax1 = df3[runtype3].plot(legend=True)

	df4[runtype4] = df4[variable].rolling(30, min_periods=15).mean()
	ax1 = df4[runtype4].plot(legend=True)

	plt.title(variable + ' SMA-30 Comparison by run type')
	plt.xlabel('Date')
	plt.ylabel(variable)

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + variable + " Comparison by run type.png")
	plt.close()

	return


def overlay_time_series(df, variable1, variable2):
	''' Plot two variables on the same y-axis scale'''

	fig, ax1 = plt.subplots()

	ax1.plot(df.index, df['HRV'], marker='.', linewidth=1, color='blue')
	ax1.set_ylabel(variable1, color='blue')
	ax1.tick_params(axis='y', labelcolor='blue')
	
	plt.xticks(rotation=70)

	# Instantiate a second axis that shares the same x-axis
	ax2 = ax1.twinx()
	ax2.plot(df.index, df['Training Load'], marker='.', linewidth=1, color='red')
	ax2.set_ylabel(variable2, color='red')
	ax2.tick_params(axis='y', labelcolor='red')

	plt.title(variable1 + "-" + variable2 + " Overlay")
	plt.xlabel('Date')

	fig.tight_layout()

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + variable1 + "-" + variable2 + " overlay.png")
	plt.close() 
	
	return

'''
def by_run_type(df, variable):
	 Plot data by the type of run
	
	if variable == "Pace (min per mile)":
		df = data_manipulations.convert_pace(df)
	
	runtype1 = "Recovery"
	df1 = data_manipulations.select_run_type(df, [runtype1])
	
	runtype2 = "Threshold"
	df2 = data_manipulations.select_run_type(df, [runtype2])

	runtype3 = "Long run"
	df3 = data_manipulations.select_run_type(df, [runtype3])

	runtype4 = "General aerobic"
	df4 = data_manipulations.select_run_type(df, [runtype4])
	
	fig = plt.figure()
 
	ax1 = df1[variable].dropna().plot(marker='.', linewidth=1, color='m', legend=True, label=runtype1)
	ax1 = df2[variable].dropna().plot(marker='.', linewidth=1, color='c', legend=True, label=runtype2)
	ax1 = df3[variable].dropna().plot(marker='.', linewidth=1, color='purple', legend=True, label=runtype3)
	ax1 = df4[variable].dropna().plot(marker='.', linewidth=1, color='olive', legend=True, label=runtype4)

	plt.title(variable + ' Comparison by run type')
	plt.xlabel('Date')
	plt.ylabel(variable)

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + variable + " Comparison by run type.png")
	plt.close()

	return
'''

if __name__ == '__main__':
	main()
