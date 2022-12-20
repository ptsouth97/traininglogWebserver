#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData, Table, Column, String, select
import pandas as pd

# Download Google sheet
# curl -L "https://docs.google.com/spreadsheets/d/e/2PACX-1vQXXuvN0QK1QYnHdCKAXd11jaUO3WJ_Yc7_6PrZ6TFhJMENGFURk-Yz7AqTarYmeGaz50Xbj5ef-_7Q/pub?gid=1105825653&single=true&output=csv" > ./trainingLog.csv


def main():
	''' main function'''

	file_name = "trainingLog.csv"

	df = to_df(file_name)
	#print(df)

	#to_db(file_name)


def to_df(fileName):
	''' Loads the Training Log .csv file as a Pandas dataframe'''

	# Read the Training Log .csv file, make the column the index, use headers in row 1
	df = pd.read_csv(fileName, index_col=0, parse_dates=True, header=1)

	# Drop the first row of data because it contains averages in the .csv file
	df = df.drop(df.index[0])

	return(df)


def to_db(fileName):
	''' Loads the csv file into the database'''

	engine = create_engine('sqlite:///database.db')
	csv_file = pd.read_csv(fileName)
	csv_file.to_sql(name='trainingLog', if_exists='append', con=engine, index=False)


if __name__ == '__main__':
	main()
