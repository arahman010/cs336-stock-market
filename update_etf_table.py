from etf_index import ETFIndex
from etf_table import etf_tbl

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

	sql = "INSERT INTO EXCH_TRD_FUND (INSTRUMENT_ID,TRADE_DATE,TRADING_SYMBOL,OPEN_PRICE,CLOSE_PRICE,ULYING_INDEX,VOLUME) select SH.INSTRUMENT_ID,SH.TRADE_DATE,ER.TRADING_SYMBOL,SH.OPEN_PRICE,SH.CLOSE_PRICE,ER.ULYING_INDEX,SH.VOLUME from STOCK_HISTORY AS SH INNER JOIN ETF_RECORDS AS ER on SH.TRADE_DATE = ER.TRADE_DATE where SH.TRADING_SYMBOL in (%s,%s,%s,%s)"
	cursor.execute(sql,random_stocks)
	db.commit()

def insert_main(cursor, db, do_debug):
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
