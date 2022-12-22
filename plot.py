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
	power(df)

	return


def year_over_year(df, variable, color):
	''' Plot single variable year-over-year data'''

	pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values=variable)	

	pv.plot(marker='.', linewidth=1)
	plt.title(variable + 'Year-Over-Year Comparison')
	plt.xlabel('Month')
	plt.ylabel(variable)

	os.chdir('./static')
	plt.savefig(variable + 'Year-Over_Year Comparison.png')
	plt.close()
	os.chdir('..')

	return


def single_variable_time_series(df, variable, color):
	''' Plot single variable time series'''

	df[variable].dropna().plot(marker='.', linewidth=1, color=color)

	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)

	os.chdir('./static')
	plt.savefig(variable + ' changes over time.png')
	plt.close()
	os.chdir('..')

	return



if __name__ == '__main__':
	main()
