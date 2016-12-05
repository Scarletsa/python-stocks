#Python 2061-70 FINAL PROJECT
#Michael Albrecht, Chris Payne, Taylor Jordan
#Written 11/29/16-12/5/16
#This program utilizes a loop initialized to true with
#a series of if statements to alter a pre-initialized
#database of stocks. The program allows you add stocks
#to the porfolio, remove stocks from the porfolio, update
#stock prices from the internet, print out the stocks
#in a print-out sorted by either name or value.
import csv
import urllib2
from modules import database

def main():
    flag == true

    #Loop that runs until user enters 'Q' or 'q'.
    while flag == true:
        choice = input("(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ").lower()

        #Condtional for choice 'A' or 'a'.
        #Adds a stock to portfolio.dat
        if choice == a:
            print('Add a stock to your portfolio!\n')
            symbol = input("Ticker: ")
            company = input("Company name: ")
            shares = input("Number of shares: ")
            price = input("Purchase price per share: $")

            insert(database, (symbol, company, shares, price))

        #Conditional for choice 'D' or 'd'
        #Removes a stock from portfolio.dat
        if choice == d:
            remove = input('Enter the ticker symbol of the stock to remove: ')
            delete(database, remove)

        #Conditional for choice 'L' or 'l'
        #Loads the intialized portfolio.dat
        if choice == l:
            f = input('Load file: ')
            database = sqlite3.connect(f)
            database.execute('drop table if exists portfolio')
            database.execute('create table portfolio (ticker TEXT PRIMARY KEY, company TEXT, shares NEAR, initial REAL, current REAL)')

        #Conditional for choice 'U' or 'u'
        #Updates the current values of the stocks in portfolio.dat
        if choice == u:
            print('Update stock prices (<Return> to keep current values)...')

        #Conditional for choice 'R' or 'r'
        #Prints out the portfolio.dat in required format based on
        #another set of conditionals for 'Name' or 'Value'
        if choice == r:
            sort = input('Sort output by (N)ame, or (V)alue? ').lower()

            #Sub-Conditional for choice 'V' or 'v'
            #Prints out portfolio.dat in value-order
            if sort == v:
                retrieve(database, currentValue)

            #Sub-Conditional for choice 'N' or 'n'
            #Prints out portfolio.dat in name-order
            if sort == n:
                retrieve(database, tickerName)

        #Conditioanl for choice 'Q' or 'q'
        #Allows the user to quit
        if choice == q:
            save = input('Save {} (y/n)? '.format(file))

            #Conditional for choice 'Y' or 'y'
            #For saving the datatbase
            if save.lower() == y:

            #Conditional for choice 'N' or 'n'
            #For not saving the datatbase
            if save.lower() == n:

            print('Bye!')
            flag = false

    url = 'http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv'.format()
    response = urllib2.urlopen(url)
    cr = csv.reader(response)

    for row in cr:
        print row

if __name__== '__main__': main()
