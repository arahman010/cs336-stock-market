import MySQLdb

def delete_records(cursor,db):
	''' Funtion to delete old Records from ETF_RECORDS '''
	
	sql_statement = "DELETE FROM ETF_RECORDS;"
	cursor.execute(sql_statement)
	db.commit()

def delete_etf_table_data(cursor,db):
	''' Function to delete old data from EXCH_TRD_FUND '''
	
	sql_statement = "DELETE FROM EXCH_TRD_FUND;"
	cursor.execute(sql_statement)
	db.commit()	

def insert_into_etf_table(cursor,db,random_stocks):
	''' Function to insert ETF history with ULYING_INDEX corresponding to each date of STOCK_HISTORY '''

	sql = "INSERT INTO EXCH_TRD_FUND select SH.INSTRUMENT_ID,SH.TRADE_DATE,ER.TRADING_SYMBOL,SH.OPEN_PRICE,SH.CLOSE_PRICE,ER.ULYING_INDEX,SH.VOLUME from STOCK_HISTORY AS SH INNER JOIN ETF_RECORDS AS ER on SH.TRADE_DATE = ER.TRADE_DATE where SH.TRADING_SYMBOL in (%s,%s,%s,%s)"
	cursor.execute(sql,random_stocks)
	db.commit()
