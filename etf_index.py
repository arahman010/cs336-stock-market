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

	def compute_etf_index(self, industry=7, debug=False):
		"""
		:param cursor: mysqldb object
		:param industry: int
		Computes the geometric average of 50 stocks to make the ETF index of a particular
		sector of an industry.
		"""
		date = self.initial_date
		values = []
		for trade_symbol in self.trading_symbols:
			sql_statement = "select CLOSE_PRICE from STOCK_HISTORY where \
							TRADING_SYMBOL='%s' and TRADE_DATE='%s';" % (trade_symbol, date)
			self.cursor.execute(sql_statement)
			values.append(float(self.cursor.fetchone()["CLOSE_PRICE"]))

		if (debug):
			pretty_printer = PrettyPrinter(indent=2)
			pretty_printer.pprint(values)
			print "----------------------\nSum: %s\nAvg: %s" % (sum(values), sum(values) / len(values))
		return sum(values) / len(values)


