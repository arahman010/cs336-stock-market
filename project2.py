from login import User
from etf_index import ETFIndex
from etf_table import etf_tbl
from update_etf_table import *
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
	# Create the object which computes the ETFIndex for ind_etf
	etf_name = "IND"
	idst_id = 7
	ind_etf = ETFIndex(cursor,etf_name,idst_id)
	ind_etf.debug = do_debug

	# Create the object which computes the ETFIndex for pha_etf
        etf_name = "PHA"
	idst_id = 9
        pha_etf = ETFIndex(cursor,etf_name,idst_id)
        pha_etf.debug = do_debug

	# Create the object which computes the ETFIndex med_etf
        etf_name = "MED"
	idst_id = 8
        med_etf = ETFIndex(cursor,etf_name,idst_id)
        med_etf.debug = do_debug

	# Create the object which computes the ETFIndex fin_etf
        etf_name = "FIN"
	idst_id = 6
        fin_etf = ETFIndex(cursor,etf_name,idst_id)
        fin_etf.debug = do_debug

	# etf_object.trading_symbols
	#trading_symbols = etf_object.get_trading_symbols()
	#etf_object.compute_etf_index(etf_object.initial_date, debug_list=True)
	#etf_object.compute_monthly_etf(2, 2005)
	# etf_object.compute_yearly_etf()
	''' Computing Yearly ETF Indexes '''
	ind_etf.compute_time_span_etf(2005, 2006)
	pha_etf.compute_time_span_etf(2005, 2006)
	med_etf.compute_time_span_etf(2005, 2006)
	fin_etf.compute_time_span_etf(2005, 2006)
	
	''' Create etf-table objects for all ETFS '''
	ind_tbl = etf_tbl(ind_etf,cursor,db)
	pha_tbl = etf_tbl(pha_etf,cursor,db)
	med_tbl = etf_tbl(med_etf,cursor,db)
	fin_tbl = etf_tbl(fin_etf,cursor,db)

	''' Delete Previous Data(if there) from ETF_RECORDS & EXCH_TRD_FUND '''
	delete_records(cursor,db)
	delete_etf_table_data(cursor,db)	

	''' Insert new Etf data into ETF_Records for all etfs '''
	ind_tbl.insert_into_records()
	pha_tbl.insert_into_records()
	med_tbl.insert_into_records()
	fin_tbl.insert_into_records()

	''' Chossing a random Stock from STOCK_HISTORY for each ETF to be renamed as each ETF '''
	random_stocks = (ind_tbl.random_stock, pha_tbl.random_stock, med_tbl.random_stock, fin_tbl.random_stock)
	
	''' Insert Data into EXCH_TRD_FUND for all etfs with renamed stock's history from STOCK_HISTORY '''
	insert_into_etf_table(cursor,db,random_stocks)	



if __name__ == "__main__":
	run(False)
