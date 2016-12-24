from pprint import PrettyPrinter
import MySQLdb
import warnings

class ETFIndex:
	def __init__(self, dbcursor):
		self.initial_date = "2005-08-02"
		self.cursor = dbcursor
		self.trading_symbols = self.get_trading_symbols()
		self.debug = False

	def get_trading_symbols(self, industry=7):
		"""
		Gets 50 trading symbols from a sql query, these will be used to compute
		the ETF index. By default the sector is INDUSTRIAL from the db.
		"""
		sql_statement = "select INSTRUMENT_ID, TRADING_SYMBOL from STOCK_HISTORY where \
						INSTRUMENT_ID in (select INSTRUMENT_ID from INSTRUMENT \
						where SCND_IDST_CLS_ID=%s) order by rand() limit 50;" % (industry)
		self.cursor.execute(sql_statement)
		query = self.cursor.fetchall()
		trade_symbols = []
		for item in query:
			trade_symbols.append(item["INSTRUMENT_ID"], item["TRADING_SYMBOL"])
		return trade_symbols

	def compute_etf_index(self, date, debug_list=False):
		"""
		:param cursor: mysqldb object
		:param industry: int
		Computes the geometric average of 50 stocks to make the ETF index of a particular
		sector of an industry on a specific date.
		"""

		# Warning handling
		warnings.filterwarnings("error", category=MySQLdb.Warning)

		values = []
		for instrument_id, trade_symbol in self.trading_symbols:
			try:
				sql_statement = "select CLOSE_PRICE from STOCK_HISTORY where \
								TRADING_SYMBOL='%s' and TRADE_DATE='%s';" % (trade_symbol, date)
				self.cursor.execute(sql_statement)
				query = self.cursor.fetchone()
				if query is not None:
					values.append(float(query["CLOSE_PRICE"]))
			except Exception, e:
				# Break out of the exception when there is an invalid date, this is to
				# help speed up the process
				break

		if (len(values) > 0):
			geometric_avg = sum(values) ** (float(1) /  len(values))

			if (debug_list):
				pretty_printer = PrettyPrinter(indent=2)
				pretty_printer.pprint(values)
				print "----------------------\nSum: %s, No. of Stocks: %s\nAvg: %06.4f" % (
						sum(values),
						len(values),
						geometric_avg)

			if (self.debug):
				print "Date: %s, Geometric Avg: %06.4f" % (date, geometric_avg)
			return geometric_avg
		else:
			return None

	def compute_monthly_etf(self, month=8, year=2005):
		"""
		Computes the etf on a daily basis on a month to month basis. This iterates through
		all of the days.
		"""
		monthly_etf_index = []
		for day in xrange(1, 32):
			date = "%s-%02d-%02d" % (year, month, day)
			geometric_mean = self.compute_etf_index(date, False)

	def compute_yearly_etf(self, year=2005):
		"""
		Computes the etf on a daily basis for an entire year, from months 01-12 (January to December).
		"""
		# Start in February, since there is no data for January
		for month in xrange(2, 13):
			self.compute_monthly_etf(month, year)

	def compute_time_span_etf(self, start_year, end_year):
		"""
		Computes the etf along a time span reading the initial start year and end year.
		"""
		time_span = end_year - start_year
		for time in xrange(time_span):
			# Get the time span to pass as a string
			year = "%s" % (start_year + time)
			# After each year randomize the stocks to mimic something similar to the
			# QQQ etf
			self.trade_symbols = self.get_trading_symbols()
			# Compute the yearly etf for the time span
			self.compute_yearly_etf(year)
