#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import load
import os
import data_manipulations
import plot


def main():
	''' Load dataframe from csv file'''

	filename = 'trainingLog.csv'
	
	df = load.to_df(filename)
	
	weight(df)
	
	return


def weight(df):
	''' Plot weight data year-over-year'''

	variable = 'Weight (pounds)'

	plot.year_over_year(df, variable, 'r')

	return


if __name__ == '__main__':
	main()
