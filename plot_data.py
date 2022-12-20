#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	df = pd.read_csv(filename, index_col=0, parse_dates=True, header=1)
	df = df.drop(df.index[0])

	weight(df)

	return


def weight(df):
	''' Plot weight data'''

	metric = "Weight (pounds)"
	pv = pd.pivot_table(df, index=df.index.month, columns=df.index.year, values=metric)	
	print(pv)
	pv.plot(marker='.', linewidth=1)
	plt.title('Year-Over-Year Comparison')
	plt.xlabel('Month')
	plt.ylabel(metric)
	#plt.show()

	plt.savefig('weight.png')
	plt.close()

	return


if __name__ == '__main__':
	main()
