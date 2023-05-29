#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import plot
import data_manipulations


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)

	hrv(df)
	rhr(df)	
	sleep(df)

	return


def hrv(df):
	''' Plot HRV data'''

	metric = "HRV"

	plot.year_over_year(df, metric)

	return


def rhr(df):
	''' Plot RHR data'''

	metric = "RHR"

	plot.year_over_year(df, metric)

	return


def sleep(df):
	''' Plot WHOOP total sleep data'''

	old_metric = "WHOOP Total Hours of Sleep"
	new_metric = "WHOOP Total Sleep (hrs)"

	df = data_manipulations.convert_sleep(df, old_metric, new_metric )

	plot.year_over_year(df, new_metric)

	return


if __name__ == '__main__':
	main()
