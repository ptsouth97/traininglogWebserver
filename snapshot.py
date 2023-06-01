#!/usr/bin/python3

import pandas as pd
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np
import load
import data_manipulations


def main():
	''' main function for testing'''

	df = load.to_df('trainingLog.csv')

	df = data_manipulations.convert_sleep(df, 'WHOOP Total Hours of Sleep', 'WHOOP Total Sleep (hrs)')

	df_7 = filter_dates(df, pd.Timestamp.today() - timedelta(7), pd.Timestamp.today())
	df_28 = filter_dates(df, pd.Timestamp.today() - timedelta(28), pd.Timestamp.today())

	metrics = ['HRV', 'RHR', 'Training Load', 'Calories consumed', 'WHOOP Total Sleep (hrs)']

	for metric in metrics:
		basic_plot(df_7, metric, 'red', ' this week')

	basic_plot(df_28, 'HRV', 'red', ' this month')

	return


def filter_dates(df, start, end):
	''' Selects a range of dates based on user input'''

	df = df.loc[start:end]

	return df


def basic_plot(df, variable, color, period):
	''' Plot single variable time series'''

	mean = df[variable].mean()

	plt.style.use('ggplot')

	df[variable].dropna().plot(marker='.', linewidth=1, color=color)

	plt.axhline(y=mean, color='b', linestyle='dashed')
	#plt.annotate('Mean = ' + str(mean),xy=(i)

	plt.title(variable + period, fontsize=14, pad=10, loc="left")
	plt.xlabel('Date')
	plt.ylabel(variable)

	plt.legend()
	plt.tight_layout()

	path = "/home/ocros03/Website/static/"
	plt.savefig(path + variable + period + ".png")
	plt.close()
	#os.chdir("/home/ocros03/Website/")

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


def convert_time(df):
	''' converts time of 1:30:00 to 1.5'''
	
	df['datetime'] = pd.to_datetime(df['Time'], errors='ignore')
	df['hours'] = df['datetime'].dt.hour
	df['minutes'] = (df['datetime'].dt.minute)/60
	df['seconds'] = (df['datetime'].dt.second)/60/60
	df['Duration (hrs)'] = round(df['hours'] + df['minutes'] + df['seconds'], 2)

	
def convert_sleep(df):
	''' converts 8:30:00 hours of sleep to 8.5 hours of sleep'''

	df['datetime'] = pd.to_datetime(df['WHOOP Total Hours of Sleep'])
	df['hours'] = df['datetime'].dt.hour
	df['minutes'] = (df['datetime'].dt.minute)/60
	df['seconds'] = (df['datetime'].dt.second)/60/60
	df['Total Hours of Sleep'] = round(df['hours'] + df['minutes'] + df['seconds'], 2)

	return df


if __name__ == '__main__':
	main()
