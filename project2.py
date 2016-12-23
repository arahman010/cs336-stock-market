from login import User
from etf_index import ETFIndex
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
		db="stockmarket",
		cursorclass=MySQLdb.cursors.DictCursor
	)

	cursor = db.cursor()
	# Create the object which computes the ETFIndex object
	etf_object = ETFIndex(cursor)
	etf_object.debug = do_debug

	# print etf_object.trading_symbols
	# etf_object.compute_etf_index(etf_object.initial_date, debug_list=True)
	etf_object.compute_monthly_etf(2, 2005)
	# etf_object.compute_yearly_etf()


if __name__ == "__main__":
	run(True)
