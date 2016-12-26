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
		
		fig = plt.figure()
		fig.suptitle('Exchange-Traded Fund', fontsize=14, fontweight='bold')
		ax = fig.add_subplot(111)
		fig.subplots_adjust(top=0.85)
		ax.set_title(etf_name)
		ax.set_xlabel('Trade Date')
		ax.set_ylabel('Value/Index')
		plt.annotate('Value', 
             		xy=(date[5000], value[1000]), xytext=(date[5300], value[1000]+50),
			arrowprops=dict(facecolor='black', shrink=0.05))  
		plt.annotate('Index', 
	     		xy=(date[2000], index[1000]), xytext=(date[2300], value[1000]+50),
	     		arrowprops=dict(facecolor='black', shrink=0.05))
		plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
		plt.plot(date, value)
		plt.plot(date, index)
		plt.show()
