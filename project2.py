from login import User
import MySQLdb
import MySQLdb.cursors
import json
#import matplotlib.pyplot as plt

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

sql = "select * from STOCK_HISTORY order by rand() limit 50;"
cursor.execute(sql)

stock_history = cursor.fetchall()
price = []
for stock in stock_history:
	price.append(float(stock['OPEN_PRICE']))
#print(price)

############## Selecting Stocks to form ETFs ###############################
# Selected Sectors for ETFs --> Banking, Coputers, Medical, Software.


######################## ETF 1 ############################################

sql = "SELECT DISTINCT(TRADING_SYMBOL) FROM INSTRUMENT WHERE SCND_IDST_CLS_ID = 1 LIMIT 50;"
cursor.execute(sql)

stocksNames = cursor.fetchall()

Etf1Stocks = []

for stock in stocksNames:
	Etf1Stocks.append(str(stock['TRADING_SYMBOL']))

#print(Etf1Stocks)

#print(stocksNames)

######################## ETF 2 ############################################

sql = "SELECT DISTINCT(TRADING_SYMBOL) FROM INSTRUMENT WHERE SCND_IDST_CLS_ID = 3 LIMIT 50;"
cursor.execute(sql)

stocksNames = cursor.fetchall()

Etf2Stocks = []

for stock in stocksNames:
        Etf2Stocks.append(str(stock['TRADING_SYMBOL']))

#print(Etf2Stocks)

#print(stocksNames)


######################## ETF 3 ############################################

sql = "SELECT DISTINCT(TRADING_SYMBOL) FROM INSTRUMENT WHERE SCND_IDST_CLS_ID = 8 LIMIT 50;"
cursor.execute(sql)

stocksNames = cursor.fetchall()

Etf3Stocks = []

for stock in stocksNames:
        Etf3Stocks.append(str(stock['TRADING_SYMBOL']))

#print(Etf3Stocks)

#print(stocksNames)


######################## ETF 4 ############################################

sql = "SELECT DISTINCT(TRADING_SYMBOL) FROM INSTRUMENT WHERE SCND_IDST_CLS_ID = 10 LIMIT 50;"
cursor.execute(sql)

stocksNames = cursor.fetchall()

Etf4Stocks = []

for stock in stocksNames:
        Etf4Stocks.append(str(stock['TRADING_SYMBOL']))

#print(Etf4Stocks)

#print(stocksNames)

#plt.plot(price)
#plt.ylabel('Stock')
#plt.show()
