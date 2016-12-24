from login import User
from etf_index import ETFIndex
from etf_table import etf_tbl
import MySQLdb
import MySQLdb.cursors
import json
#import matplotlib.pyplot as plt


def run(do_debug=False):
	"""
	Main function to run the program.
	"""
	# Create the user object which has all of the credentials
	user = User()

	db = MySQLdb.connect(
		host="134.74.126.107",
		user=user.username,
		passwd=user.password,
		db="F16336team7",
		cursorclass=MySQLdb.cursors.DictCursor
	)

	cursor = db.cursor()
	# Create the object which computes the ETFIndex object
	etf_name = "IND"
	idst_id = 7
	ind_etf = ETFIndex(cursor,etf_name,idst_id)
	ind_etf.debug = do_debug

	# Create the object which computes the ETFIndex object
        etf_name = "COM"
	idst_id = 3
        com_etf = ETFIndex(cursor,etf_name,idst_id)
        com_etf.debug = do_debug

	# Create the object which computes the ETFIndex object
        etf_name = "MED"
	idst_id = 8
        med_etf = ETFIndex(cursor,etf_name,idst_id)
        med_etf.debug = do_debug

	# Create the object which computes the ETFIndex object
        etf_name = "FIN"
	idst_id = 6
        fin_etf = ETFIndex(cursor,etf_name,idst_id)
        fin_etf.debug = do_debug

	# etf_object.trading_symbols
	#trading_symbols = etf_object.get_trading_symbols()
	#etf_object.compute_etf_index(etf_object.initial_date, debug_list=True)
	#etf_object.compute_monthly_etf(2, 2005)
	# etf_object.compute_yearly_etf()
	ind_etf.compute_time_span_etf(2005, 2006)
	com_etf.compute_time_span_etf(2005, 2006)
	med_etf.compute_time_span_etf(2005, 2006)
	fin_etf.compute_time_span_etf(2005, 2006)
	
	# Create etf-table objects for all etfs
	ind_tbl = etf_tbl(ind_etf,cursor,db)
	com_tbl = etf_tbl(com_etf,cursor,db)
	med_tbl = etf_tbl(med_etf,cursor,db)
	fin_tbl = etf_tbl(fin_etf,cursor,db)

	# Delete Previous Data(if there) from ETF_RECORDS & EXCH_TRD_FUND
	delete_records(cursor,db)
	delete_etf_table_data(cursor,db)	

	# Insert new Etf data into Records for all etfs
	ind_tbl.insert_into_records()
	com_tbl.insert_into_records()
	med_tbl.insert_into_records()
	fin_tbl.insert_into_records()

	#For renaming a stock from STOCK_HISTORY for each ETF 
	random_stocks = (ind_tbl.random_stock, com_tbl.random_stock, med_tbl.random_stock, fin_tbl.random_stock)
	# Insert Data into EXCH_TRD_FUND for all etfs
	insert_into_etf_table(cursor,db,random_stocks)
	print(random_stocks)	

def delete_records(cursor,db):
	sql_statement = "DELETE FROM ETF_RECORDS;"
	cursor.execute(sql_statement)
	db.commit()

def delete_etf_table_data(cursor,db):
	sql_statement = "DELETE FROM EXCH_TRD_FUND;"
	cursor.execute(sql_statement)
	db.commit()	

def insert_into_etf_table(cursor,db,random_stocks):
	sql = "INSERT INTO EXCH_TRD_FUND select SH.INSTRUMENT_ID,SH.TRADE_DATE,ER.TRADING_SYMBOL,SH.OPEN_PRICE,SH.CLOSE_PRICE,ER.ULYING_INDEX,SH.VOLUME from STOCK_HISTORY AS SH INNER JOIN ETF_RECORDS AS ER on SH.TRADE_DATE = ER.TRADE_DATE where SH.TRADING_SYMBOL in (%s,%s,%s,%s)"
	cursor.execute(sql,random_stocks)
	db.commit()


if __name__ == "__main__":
	run(True)
