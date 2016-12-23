from login import User
import MySQLdb
import MySQLdb.cursors
import json
#import matplotlib.pyplot as plt

# Create the user object which has all of the credentials
user = User()

db = MySQLdb.connect(
	host="134.74.126.107",
	user=user.username,
	passwd=user.password,
	db="stockmarket",
	cursorclass=MySQLdb.cursors.DictCursor
)

cursor = db.cursor()

def compute_etf_index(cursor, industry):
	"""
	:param cursor: mysqldb object
	:param industry: int
	Computes the geometric average of 50 stocks to make the ETF index of a particular
	sector of an industry.
	"""
	# Take 50 trading symbols, this represent the trading symbol
	sql_statement = "select TRADING_SYMBOL from STOCK_HISTORY where INSTRUMENT_ID in (select INSTRUMENT_ID from INSTRUMENT where SCND_IDST_CLS_ID=%s) order by rand() limit 50;" % (industry)
	cursor.execute(sql_statement)
	trading_symbols = cursor.fetchall()


if __name__ == "__main__":
	compute_etf_index(cursor, 7)
