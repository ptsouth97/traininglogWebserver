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
	hrv(df)

	return


def hrv(df):
	''' Plot HRV data'''

	metric = "HRV"
	pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values=metric)	
	#print(pv)
	pv.plot(marker='.', linewidth=1)
	plt.title('Year-Over-Year Comparison')
	plt.xlabel('Month')
	plt.ylabel(metric)
	#plt.show()

	os.chdir('./static')
	plt.savefig('hrv.png')
	plt.close()
	os.chdir('..')

	return


if __name__ == '__main__':
	main()
