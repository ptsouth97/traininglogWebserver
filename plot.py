#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)
	#print(df)
	#power(df)

	overlay_time_series(df, 'HRV', 'Training Load')

	return


def year_over_year(df, variable, runtype):
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

	os.chdir('./static')
	plt.savefig('Mean ' + runtype + ' ' + variable + ' Year-Over-Year Comparison.png')
	plt.close()
	os.chdir('..')

	return


def single_variable_time_series(df, variable, color):
	''' Plot single variable time series'''

	df[variable].dropna().plot(marker='.', linewidth=1, color=color)

	df['SMA_30'] = df[variable].rolling(30, min_periods=15).mean()
	df['SMA_30'].plot(legend=True)

	#plt.style.use('ggplot')
	#plt.figure(facecolor="yellow")

	#ax = plt.axes()
	#ax.set_facecolor("violet")
	
	plt.style.use('ggplot')

	plt.title(variable + ' changes over time', fontsize=14, pad=10, loc="left")
	plt.xlabel('Date')
	plt.ylabel(variable)

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
