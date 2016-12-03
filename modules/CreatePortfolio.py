@@ -0,0 +1,33 @@
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

    url = 'http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv'.format('MMM' + 'MDT')
    response = urlopen(url)
    df = open(response, "rt", encoding="utf8")

    cr = csv.reader(df)

    for row in cr:
        print(row)

    database.disp_rows(db)

if __name__ == "__main__": main()
