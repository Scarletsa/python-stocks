import csv
import urllib2
import database.py

def main():
    flag == true

    while flag == true:
        choice = input("(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ").lower()

        if choice == a:
            print('Add a stock to your portfolio!\n')
            symbol = input(Ticker: )
            company = input(Company name: )
            shares = input(Number of shares: )
            price = input(Purchase price per share: )
            insert(database, (symbol, company, shares, price))

        if choice == d:
            remove = input('Enter the ticker symbol of the stock to remove: ')
            delete(database, remove)

        if choice == l:
            file = input('Load file: ')
            database = sqlite3.connect('portfolio.dat')
            database.execute('drop table if exists students')
            database.execute('create table students (ticker TEXT PRIMARY KEY, company TEXT, shares NEAR, initial REAL, current REAL)')

        if choice == u:
            print('Update stock prices (<Return> to keep current values)...')

        if choice == r:
            sort = input('Sort output by (N)ame, or (V)alue? ').lower()

            if sort == v:
                retrieve(database, currentValue)

            if sort == n:
                retrieve(database, tickerName)

        if choice == q:
            save = input('Save {} (y/n)? '.format(file))

            if save.lower() == y:

            if save.lower() == n:

            print('Bye!')
            flag = false

    
    url = 'http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv'.format()
    response = urllib2.urlopen(url)
    cr = csv.reader(response)

    for row in cr:
        print row

if __name__== '__main__': main()
