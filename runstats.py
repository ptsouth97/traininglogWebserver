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

	#df = data_manipulations.convert_pace(df)
	#print(df)
	#run_type = "Recovery"
	#df = data_manipulations.select_run_type(df, [run_type])

	hr(df)

	return


def hr(df):
	''' Plot heart rate data'''

	variable = 'GARMIN Average HR (bpm)'

	df[variable].dropna().plot(marker='.', linewidth=1, color='r')

	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)
 
	os.chdir('./static')
	plt.savefig('hr.png')
	plt.close()
	os.chdir('..')


	return


def pace(df):
	''' Plot pace data'''

	variable = 'Average Pace (min/mile)'

	df = df[variable].dropna()
	print(df)
	df[variable].plot(marker='.', linewidth=1, color='r')

	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)
 
	os.chdir('../static')
	plt.savefig('pace.png')
	plt.close()
	os.chdir('..')

	'''metric = "Average Pace (min/mile)"
	pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values=metric)	
	#print(pv)
	pv.plot(marker='.', linewidth=1)
	plt.title('Year-Over-Year Comparison')
	plt.xlabel('Month')
	plt.ylabel(metric)
	#plt.show()

	os.chdir('./static')
	plt.savefig('pace.png')
	plt.close()
	os.chdir('..')'''

	return


if __name__ == '__main__':
	main()
