import MySQLdb
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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

		plt.figure().suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
		ax = plt.figure().add_subplot(111)
		plt.figure().subplots_adjust(top=0.85)
		ax.set_title('axes title')

		ax.set_xlabel('xlabel')
		ax.set_ylabel('ylabel')

		plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
		plt.plot(date, value)
		plt.plot(date, index)
		plt.show()
