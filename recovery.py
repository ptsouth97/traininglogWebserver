#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import plot


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)

	hrv(df)
	rhr(df)	

	return


def hrv(df):
	''' Plot HRV data'''

	metric = "HRV"

	plot.year_over_year(df, metric, 'r')

	return


def rhr(df):
	''' Plot RHR data'''

	metric = "RHR"

	plot.year_over_year(df, metric, 'g')

	return


if __name__ == '__main__':
	main()
