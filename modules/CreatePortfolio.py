import database
import sqlite3
import csv
from urllib.request import urlopen
import pickle

def main():
    # Initial stocks
    initialStocks = [['MMM', '3M', '100', '74.00', '118.30'],
                     ['MDT', 'Medtronic', '50', '56.10', '48.00'],
                     ['NWAC', 'Northwest Airlines', '100', '67.50', '18.04'],
                     ['SGI', 'Silicon Graphics', '100', '22.25', '2.25']]

    # Creating a database called students.
    db = sqlite3.connect('portfolio.dat')
    db.execute('drop table if exists portfolio')
    db.execute('create table portfolio (ticker TEXT PRIMARY KEY, company TEXT, shares NEAR, initial NEAR, current NEAR)')

    for row in initialStocks:
        database.insert(db, row)

    symbols = []
    for i in range(len(initialStocks)):
        symbols.append(initialStocks[i][0])

    print(symbols)

    url = ("http://finance.yahoo.com/d/quotes.csv?s={symbols}&f=sl1d1t1c1ohgv&e=.csv ".format(symbols="+".join(symbols)))
    content = urlopen(url).read().decode().split('\n')

    prices = []

    print(content)

    
    for k in content:
        stockData = k.split(',')
        print(stockData)
        if len(stockData) == 9:
            prices.append(stockData[1])

    print(prices)
    
    ask_quotes = {symbol: quote for symbol, quote in zip(symbols, prices)}

    print(ask_quotes)

    #cr = csv.reader(df)

    #for row in cr:
        #print(row)

    #database.disp_rows(db)

if __name__ == "__main__": main()
