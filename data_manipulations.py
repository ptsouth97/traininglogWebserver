#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import load


def main():
	''' main function for testing'''

	df = load.to_df('trainingLog.csv')

	df = convert_pace(df)
	
	return


def select_run_type(df, run_type):
	''' select specific type of run only from dataframe'''

	df = df.loc[df['Run type'].isin(run_type)]

	return(df)


def convert_pace(df):
	''' converts 0:8:30 min/mile to 8.5 min/mile'''

	df['datetime'] = pd.to_datetime(df['Average Pace (min/mile)'])
	df['minutes'] = df['datetime'].dt.minute
	df['seconds'] = (df['datetime'].dt.second)/60
	df['Pace (min per mile)'] = round(df['minutes'] + df['seconds'], 2)

	return df


if __name__ == '__main__':
	main()
