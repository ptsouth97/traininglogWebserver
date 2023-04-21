#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)
	#print(df)
	#power(df)

	overlay_time_series(df, 'HRV', 'Training Load')

	return


def year_over_year(df, variable):
	''' Plot single variable year-over-year data'''

	pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values=variable)	

	plt.style.use('ggplot')
	pv.plot(marker='.', linewidth=1)
	plt.title('Mean ' + variable + ' Year-Over-Year Comparison')
	plt.xlabel('Month')
	plt.ylabel(variable)

	os.chdir('./static')
	plt.savefig('Mean ' + variable + ' Year-Over-Year Comparison.png')
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
	
	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + variable + " changes over time.png")
	plt.close()
	#os.chdir("/home/ocros03/Website/")

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


if __name__ == '__main__':
	main()
