import MySQLdb
import MySQLdb.cursors
import json
import matplotlib.pyplot as plt
db = MySQLdb.connect(host="134.74.126.107",user="F16336sgupta",passwd="16025184",db="stockmarket",cursorclass=MySQLdb.cursors.DictCursor) #Be sure to change username and password

cursor = db.cursor()

sql = "select * from STOCK_HISTORY order by rand() limit 50;"
cursor.execute(sql)

stock_history = cursor.fetchall()
price = []
for stock in stock_history:
	price.append(float(stock['OPEN_PRICE']))

print price

plt.plot(price)
plt.ylabel('Stock')
plt.show()
