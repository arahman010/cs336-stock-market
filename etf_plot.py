import MySQLdb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot(cursor):
	for etf_name in ["IND","PHA","MED","FIN"]:
		sql = "select TRADE_DATE, CLOSE_PRICE, ULYING_INDEX from EXCH_TRD_FUND where TRADING_SYMBOL like %s"
		cursor.execute(sql,etf_name)
		query = cursor.fetchall()
		value = []
		index = []
		date  = []
		for item in query:
			date.append(item['TRADE_DATE'])
			value.append(float(item['CLOSE_PRICE']))
			index.append(float(item['ULYING_INDEX']))
		#print(value,index,nav,date)
		plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
		#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
		plt.plot(date, value)
		plt.plot(date, index)
		plt.show()
