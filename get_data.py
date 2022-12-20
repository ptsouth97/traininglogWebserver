#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData, Table, Column, String, select
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def main():

	test()
	
	return


def test():
	''' testing getting data and plotting on webpage'''

	time = datetime.now()
	engine = create_engine('sqlite:///database.db')
	metadata = MetaData(engine)
	trainingLog = Table('trainingLog', metadata, autoload=True, autoload_with=engine)

	connection = engine.connect()

	return

if __name__ == '__main__':
	main()
