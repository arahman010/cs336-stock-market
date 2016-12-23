from pprint import PrettyPrinter

class ETFIndex:
	def __init__(self, dbcursor):
		self.initial_date = "2005-08-02"
		self.cursor = dbcursor
		self.trading_symbols = self.get_trading_symbols()

	def get_trading_symbols(self, industry=7):
		"""
		Gets 50 trading symbols from a sql query, these will be used to compute
		the ETF index. By default the sector is INDUSTRIAL from the db.
		"""
		sql_statement = "select TRADING_SYMBOL from STOCK_HISTORY where \
						INSTRUMENT_ID in (select INSTRUMENT_ID from INSTRUMENT \
						where SCND_IDST_CLS_ID=%s) order by rand() limit 50;" % (industry)
		self.cursor.execute(sql_statement)
		query = self.cursor.fetchall()
		trade_symbols = []
		for item in query:
			trade_symbols.append(item["TRADING_SYMBOL"])
		return trade_symbols

	def compute_etf_index(self, date, debug=False):
		"""
		:param cursor: mysqldb object
		:param industry: int
		Computes the geometric average of 50 stocks to make the ETF index of a particular
		sector of an industry on a specific date.
		"""
		values = []
		print date
		for trade_symbol in self.trading_symbols:
			sql_statement = "select CLOSE_PRICE from STOCK_HISTORY where \
							TRADING_SYMBOL='%s' and TRADE_DATE='%s';" % (trade_symbol, date)
			self.cursor.execute(sql_statement)
			query = self.cursor.fetchone()
			if query is not None:
				values.append(float(query["CLOSE_PRICE"]))

		if (debug):
			pretty_printer = PrettyPrinter(indent=2)
			pretty_printer.pprint(values)
			print "----------------------\nSum: %s\nAvg: %s" % (sum(values), sum(values) / len(values))
		
		if (len(values) > 0):
			return sum(values) / len(values)
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
			print geometric_mean

	def compute_yearly_etf(self):
		"""
		Computes the etf on a daily basis for an entire year.
		"""
		pass

