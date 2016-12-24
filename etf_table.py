from pprint import PrettyPrinter
import MySQLdb
import warnings
import random

class etf_tbl:
        def __init__(self,etf_object,dbcursor,dbconnect):
		self.etf = etf
		self.cursor = dbcursor
		self.db = dbconnect
		self.random_stock = (random.choice(etf_object.trading_symbols))[1]

	def delete_records(self):
		sql_statement = "DELETE FROM ETF_RECORDS;"
        	self.cursor.execute(sql_statement)
       		self.db.commit()
	
	def insert_into_records(self):
		for item in self.etf.date_name_index:
                	sql = "INSERT INTO ETF_RECORDS(TRADE_DATE,TRADING_SYMBOL,ULYING_INDEX) values(%s,%s,%s)"
                	self.cursor.execute(sql,item)
                	db.commit()
	'''
	def choose_random_stock(self):
		random_stock = (random.choice(self.etf.trading_symbols))[1]
        	#print(random_stock)
        	return random_stock
'''
	def insert_into_etf_table(self):
		sql = "INSERT INTO EXCH_TRD_FUND select SH.INSTRUMENT_ID,SH.TRADE_DATE,ER.TRADING_SYMBOL,SH.OPEN_PRICE,SH.CLOSE_PRICE,ER.ULYING_INDEX,SH.VOLUME from STOCK_HISTORY AS SH INNER JOIN ETF_RECORDS AS ER on SH.TRADE_DATE = ER.TRADE_DATE where SH.TRADING_SYMBOL = %s"
        	self.cursor.execute(sql,self.random_stock)
        	self.db.commit()
