#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load

def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)
	#print(df)
	power(df)

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


def power(df):
	''' Plot power data'''

	variable = 'Average Power (W)'

	#df = df[variable].dropna()
	#print(df)
	df[variable].dropna().plot(marker='.', linewidth=1, color='r')

	plt.title(variable + ' changes over time')
	plt.xlabel('Date')
	plt.ylabel(variable)

	plt.savefig('power.png')
	plt.close()

	return

if __name__ == '__main__':
	main()
