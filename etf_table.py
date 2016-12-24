# -*- coding: utf-8 -*-
from pprint import PrettyPrinter
import MySQLdb
import warnings
import random


class etf_tbl:
        def __init__(self,etf_object,dbcursor,dbconnect):
		self.etf = etf_object
		self.cursor = dbcursor
		self.db = dbconnect
		self.random_stock = (random.choice(etf_object.trading_symbols))[1]

		
	def insert_into_records(self):
		for item in self.etf.date_name_index:
			sql = "INSERT INTO ETF_RECORDS(TRADE_DATE,TRADING_SYMBOL,ULYING_INDEX) values(%s,%s,%s)"
			self.cursor.execute(sql,item)
			self.db.commit()

