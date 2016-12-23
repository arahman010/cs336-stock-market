class ETFIndex:
	def __init__(self, cursor):
		self.cursor = cursor
		self.trading_symbols = self.get_trading_symbols()

	@classmethod
	def get_trading_symbols(self, cursor, industry=7):
		"""
		Gets 50 trading symbols from a sql query, these will be used to compute
		the ETF index
		"""
		sql_statement = "select TRADING_SYMBOL from STOCK_HISTORY where \
						INSTRUMENT_ID in (select INSTRUMENT_ID from INSTRUMENT \
						where SCND_IDST_CLS_ID=%s) order by rand() limit 50;" % (industry)
		cursor.execute(sql_statement)
		query = cursor.fetchall()
		trade_symbols = []
		for item in query:
			trade_symbols.append(item["TRADING_SYMBOL"])
		return trade_symbols

	@classmethod
	def compute_etf_index(self, cursor, industry):
		"""
		:param cursor: mysqldb object
		:param industry: int
		Computes the geometric average of 50 stocks to make the ETF index of a particular
		sector of an industry.
		"""
		pass
