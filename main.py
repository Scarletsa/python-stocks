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
from urllib.request import urlopen
from modules import database
import sqlite3

def main():
    stocks = []
    flag = True

    #Loop that runs until user enters 'Q' or 'q'.
    while flag == True:
        choice = input("(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ").lower()

        #Condtional for choice 'A' or 'a'.
        #Adds a stock to portfolio.dat
        if choice == 'a':
            print('Add a stock to your portfolio!\n')
            symbol = input('Ticker: ')
            company = input('Company name: ')
            shares = int(input('Number of shares: '))
            pPrice = int((input('Purchase price per share: ')/100))

            name = company + " (" + symbol + ")"

            url = ("http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv ".format(symbol))
            content = urlopen(url).read().decode().split('\n')
            for k in content:
                stockData = k.split(',')
                print(stockData)
                if len(stockData) == 9:
                    cPrice = int(stockData[1]/100)

            iValue = shares*(pPrice*100)
            cValue = shares*(cPrice*100)

            gl = (-1 + ( (cValue) / (iValue) ))*100
            totalValue += (cValue)
            totalGL += ((cValue)/(iValue))

            temp = [symbol, company, shares, pPrice, cPrice, cValue, gl]
            stocks.append(temp)

        #Conditional for choice 'D' or 'd'
        #Removes a stock from portfolio.dat
        if choice == 'd':
            remove = input('Enter the ticker symbol of the stock to remove: ')
            delete(database, remove)

        #Conditional for choice 'L' or 'l'
        #Loads the intialized portfolio.dat
        if choice == 'l':
            inFile = input('Load file: ')
            tempFile = inFile
            db = sqlite3.connect(inFile)
            db.execute('drop table if exists portfolio')
            db.execute('create table portfolio (ticker TEXT PRIMARY KEY, company TEXT, shares NEAR, initial NEAR, current NEAR, value REAL, gl REAL)')

        #Conditional for choice 'U' or 'u'
        #Updates the current values of the stocks in portfolio.dat
        if choice == 'u':
            print('Update stock prices (<Return> to keep current values)...')

        #Conditional for choice 'R' or 'r'
        #Prints out the portfolio.dat in required format based on
        #another set of conditionals for 'Name' or 'Value'
        if choice == 'r':
            sort = input('Sort output by (N)ame, or (V)alue? ').lower()

            print('{0: <27}'.format(name) + '{0: >4}'.format(shares) + '{:8.2f}'.format(price) + '{:8.2f}'.format(cPrice) + '{0: >8}'.format(int(cValue)) + '{:8.1f}%'.format(gl))

            #Sub-Conditional for choice 'V' or 'v'
            #Prints out portfolio.dat in value-order
            if sort == 'v':
                cmd = 'select * from portfolio order by current'
                disp_rows(database, cmd)

            #Sub-Conditional for choice 'N' or 'n'
            #Prints out portfolio.dat in name-order
            if sort == 'n':
                cmd = 'select * from portfolio order by company'
                disp_rows(database, cmd)

        #Conditioanl for choice 'Q' or 'q'
        #Allows the user to quit
        if choice == 'q':
            save = input('Save {} (y/n)? '.format(file))

            #Conditional for choice 'Y' or 'y'
            #For saving the datatbase
            if save.lower() == 'y':
                pass

            #Conditional for choice 'N' or 'n'
            #For not saving the datatbase
            if save.lower() == 'n':
                pass

            print('Bye!')
            flag = false

if __name__== '__main__': main()
