#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations
import plot
import body_metrics as bm
import runstats
import power as pwr
import recovery as rec
import regression as reg
from itertools import cycle
from time import sleep


def main():
	''' Load dataframe from csv file'''

	# Download latest Google Sheet data as a csv file
	load.get_url()

	# Load csv file to a pandas dataframe
	filename = 'trainingLog.csv'
	df = load.to_df(filename)

	'''	
	for frame in cycle(r'-\|/'):
		print('\r', frame, sep='', end='', flush=True)
		sleep(0.2)
	'''

	#power(df)
	body_metrics(df)
	#run_stats(df)
	#recovery(df)


def power(df):
	''' Creates all power charts'''

	print("Calculating power...")
	pwr.avgPower(df)
	pwr.efficiencyFactor(df)
	pwr.intensityFactor(df)
	pwr.powerVariableByRunType(df, "Average Power (W)")

	return


def body_metrics(df):
	''' Creates all body metric charts'''

	print("Calculating body metrics...")
	bm.weight(df)
	bm.calories(df)
	reg.two_variable_correlation(df, 'Weight (pounds)', 'Body Fat %')

	return


def run_stats(df):
	''' Creates all run stats charts'''

	print("Calculating run stats...")
	runstats.hr(df)
	runstats.pace(df)
	runstats.temp(df)
	plot.distribution(df, "Average Pace (min/mile)")
		
	return


def recovery(df):
	''' Creates all recovery charts'''

	print("Calculating recovery...")
	rec.hrv(df)
	rec.rhr(df)
	#recovery.sleep(df)

	return

if __name__ == '__main__':
	main()
