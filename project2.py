from login import User
from etf_plot import plot
from update_etf_table import insert_main
import MySQLdb
import MySQLdb.cursors
import json


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
	#insert_main(cursor,db,do_debug)		
	plot(cursor)


if __name__ == "__main__":
	run(False)
