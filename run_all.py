#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
import load
import os
import data_manipulations
import plot
import body_metrics as bm
import runstats
import snapshot as ss
import power as pwr
import recovery as rec
import regression as reg
from itertools import cycle
from datetime import timedelta
from time import sleep


def main():
	''' Load dataframe from csv file'''

	# Download latest Google Sheet data as a csv file (using script.sh instead)
	# load.get_url()

	# Load csv file to a pandas dataframe
	filename = 'trainingLog.csv'

	try:
		df = load.to_df(filename)
	except:
		print("An error occurred loading the dataframe")


	#power(df)
	#body_metrics(df)
	#run_stats(df)
	#recovery(df)
	snap_shot(df)


def snap_shot(df):
	''' Creates all snap shot charts'''

	print("Calculating snapshot")
	df = data_manipulations.convert_sleep(df, 'WHOOP Total Hours of Sleep', 'WHOOP Total Sleep (hrs)')

	df_7 = ss.filter_dates(df, pd.Timestamp.today() - timedelta(7), pd.Timestamp.today())
	df_28 = ss.filter_dates(df, pd.Timestamp.today() - timedelta(28), pd.Timestamp.today())

	metrics = ['HRV', 'RHR', 'Training Load', 'Calories consumed', 'WHOOP Total Sleep (hrs)']

	for metric in metrics:
		ss.basic_plot(df_7, metric, 'red', ' this week')

	ss.basic_plot(df_28, 'HRV', 'red', ' this month')

	print("Success!")

	return


def power(df):
	''' Creates all power charts'''

	print("Calculating power...")
	pwr.avgPower(df)
	pwr.efficiencyFactor(df)
	pwr.intensityFactor(df)
	pwr.powerVariableByRunType(df)
	print("Success!")

	return


def body_metrics(df):
	''' Creates all body metric charts'''

	print("Calculating body metrics...")
	bm.weight(df)
	bm.calories(df)
	#reg.two_variable_correlation(df, 'Weight (pounds)', 'Body Fat %')
	print("Success!")

	return


def run_stats(df):
	''' Creates all run stats charts'''

	print("Calculating run stats...")
	runstats.hr(df)
	runstats.pace(df)
	runstats.temp(df)
	plot.distribution(df, "Average Pace (min/mile)")
	print("Success!")
		
	return


def recovery(df):
	''' Creates all recovery charts'''

	print("Calculating recovery...")
	rec.hrv(df)
	rec.rhr(df)
	#recovery.sleep(df)
	print("Success!")

	return

if __name__ == '__main__':
	main()
