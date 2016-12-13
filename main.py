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
import sqlite3
from operator import itemgetter

def main():
    iFile = ""
    stocks = []
    flag = True

    #Loop that runs until user enters 'Q' or 'q'.
    while flag == True:
        choice = input("(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ").lower()

        #Condtional for choice 'A' or 'a'.
        #Adds a stock to portfolio.dat
        if choice == 'a':
            print('Add a stock to your portfolio!\n')
            symbol = input('Ticker: ').upper()
            company = input('Company name: ')
            shares = int(input('Number of shares: '))
            pPrice = float(input('Purchase price per share: '))
            pPrice = int(pPrice*100)
            print(pPrice)

            url = ("http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv ".format(symbol))
            content = urlopen(url).read().decode().split('\n')
            for k in content:
                stockData = k.split(',')
                print(stockData)
                if len(stockData) == 9:
                    try:
                        cPrice = float(stockData[1])*100
                    except:
                        cPrice = pPrice

            iValue = shares*(pPrice/100)
            cValue = shares*(cPrice/100)

            gl = (-1 + ( (cValue) / (iValue) ))*100

            temp = [symbol, company, shares, pPrice, cPrice, cValue, gl]
            stocks.append(temp)

        #Conditional for choice 'D' or 'd'
        #Removes a stock from portfolio.dat
        if choice == 'd':

            index=0
            remove = input('Enter the ticker symbol of the stock to remove: ')

            for each in stocks:

                if remove.upper() == each[0]:
                    stocks.pop(index)

                index += 1

        #Conditional for choice 'L' or 'l'
        #Loads the intialized portfolio.dat
        if choice == 'l':
            iFile = input('Load file: ')
            tempFile = iFile
            db = sqlite3.connect(iFile)
            cursor = db.cursor()
            cursor.execute("SELECT * FROM portfolio")
            result = cursor.fetchall()
            stocks = []
            for r in result:
                stocks.append(r)

        #Conditional for choice 'U' or 'u'
        #Updates the current values of the stocks in portfolio.dat
        if choice == 'u':
            print('Update stock prices (<Return> to keep current values)...')

        #Conditional for choice 'R' or 'r'
        #Prints out the portfolio.dat in required format based on
        #another set of conditionals for 'Name' or 'Value'
        if choice == 'r':
            sort = input('Sort output by (N)ame, or (V)alue? ').lower()
            totalValue = 0
            totalGL = 0

            #Sub-Conditional for choice 'V' or 'v'
            #Prints out portfolio.dat in value-order
            if sort == 'v':
                print('Company                   Shares   Pur.  Latest   Value     G/L')
                print('=================================================================')
                vSort = sorted(stocks, key=itemgetter(5))
                for i in vSort:
                    totalValue += (i[5])
                    totalGL += ((i[5])/(i[2]*i[3]/100))
                    name = i[1] + " (" + i[0] + ")"
                    print('{0: <27}'.format(name) + '{0: >4}'.format(i[2]) + '{:8.2f}'.format(i[3]/100) + '{:8.2f}'.format(i[4]/100) + '{0: >8}'.format(int(i[5])) + '{:8.1f}%'.format(i[6]))

            #Sub-Conditional for choice 'N' or 'n'
            #Prints out portfolio.dat in name-order
            if sort == 'n':
                print('Company                   Shares   Pur.  Latest   Value     G/L')
                print('=================================================================')
                nSort = sorted(stocks, key=itemgetter(1))
                for i in nSort:
                    totalValue += (i[5])
                    totalGL += ((i[5])/(i[2]*i[3]/100))
                    name = i[1] + " (" + i[0] + ")"
                    print('{0: <27}'.format(name) + '{0: >4}'.format(i[2]) + '{:8.2f}'.format(i[3]/100) + '{:8.2f}'.format(i[4]/100) + '{0: >8}'.format(int(i[5])) + '{:8.1f}%'.format(i[6]))

        #Conditioanl for choice 'Q' or 'q'
        #Allows the user to quit
        if choice == 'q':
            save = input('Save {} (y/n)? '.format(iFile))

            #Conditional for choice 'Y' or 'y'
            #For saving the datatbase
            if save.lower() == 'y':
                if iFile == "":
                    fName = input('Save file as: ')
                    db = sqlite3.connect(fName)
                    db.execute('drop table if exists portfolio')
                    db.execute('create table portfolio (ticker TEXT PRIMARY KEY, company TEXT, shares NEAR, initial NEAR, current NEAR, value REAL, gl REAL)')

                    for row in stocks:
                        db.execute('insert into portfolio (ticker, company, shares, initial, current, value, gl) values (?, ?, ?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

                    db.commit()
                else:
                    db.execute('drop table if exists portfolio')
                    db.execute('create table portfolio (ticker TEXT PRIMARY KEY, company TEXT, shares NEAR, initial NEAR, current NEAR, value REAL, gl REAL)')

                    for row in stocks:
                        db.execute('insert into portfolio (ticker, company, shares, initial, current, value, gl) values (?, ?, ?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

                    db.commit()

            #Conditional for choice 'N' or 'n'
            #For not saving the datatbase
            if save.lower() == 'n':
                pass

            print('Bye!')
            flag = False

if __name__== '__main__': main()
