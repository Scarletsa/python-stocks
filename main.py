#Python 2061-70 FINAL PROJECT
#Michael Albrecht, Chris Payne, Taylor Jordan
#Written 11/29/16-12/15/16
#This program is designed to let a user enter any number
#of stocks to a list. They can be removed, or updated.
#You can either start a new list or load a saved older
#version of a portfolio. By updating stocks, they are then
#issued their current value at that exact time from
#Yahoo finance. Once you're ready to finish you
#can quit with the option of saving or not saving.
import csv
from urllib.request import urlopen
import sqlite3
from operator import itemgetter

def main():
    iFile = ""
    stocks = []
    flag = True

    #Loop to process user input.
    while flag == True:
        choice = input("\n(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ").lower()

        #Condtional for choice 'A' or 'a'.
        #Adds a stock to stocks list
        if choice == 'a':
            #Getting variable from the user.
            print('Add a stock to your portfolio!\n')
            symbol = input('Ticker: ').upper()
            company = input('Company name: ')
            shares = int(input('Number of shares: '))
            pPrice = float(input('Purchase price per share: $'))
            pPrice = int(pPrice*100)

            #Converting internet data to a list
            url = ("http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv ".format(symbol))
            content = urlopen(url).read().decode().split('\n')

            #Loop for getting the current stock value. If the stock is a real NYSE Stock
            #it will pull the value. If stock is fictional it will set initial to current
            for k in content:
                stockData = k.split(',')
                try:
                    cPrice = float(stockData[1])*100
                except:
                    print('A current price for {} could not be found.'.format(symbol))
                    cPrice = pPrice

            iValue = shares*(pPrice/100)
            cValue = shares*(cPrice/100)

            gl = (-1 + ( (cValue) / (iValue) ))*100

            #Gathering all of the variables in a temp list
            #and storing it to the stocks list
            temp = [symbol, company, shares, pPrice, cPrice, cValue, gl]
            stocks.append(temp)

        #Conditional for choice 'D' or 'd'
        #Removes a stock from stocks list
        if choice == 'd':
            remove = input('Enter the ticker symbol of the stock to remove: ')

            #Searching the list for the ticker the user entered and removing it.
            for index, each in enumerate(stocks):
                if remove.upper() == each[0]:
                    stocks.pop(index)

        #Conditional for choice 'L' or 'l'
        #Loads the intialized stocks list
        if choice == 'l':
            #Prompting the user for the file name, connecting to that file,
            #getting all the data from the file and storing it to the stocks list
            iFile = input('Load file: ')
            db = sqlite3.connect(iFile)
            cursor = db.cursor()
            cursor.execute("SELECT * FROM portfolio")
            result = cursor.fetchall()
            stocks = []
            for r in result:
                stocks.append(r)

        #Conditional for choice 'U' or 'u'
        #Updates the current values of the stocks in stocks list
        if choice == 'u':
            temp = []
            print('\nUpdating stock prices...')
            #Iterating through the list to update the prices
            for o, p in enumerate(stocks):
                url = ("http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv ".format(stocks[o][0]))
                content = urlopen(url).read().decode().split('\n')
                for k in content:
                    stockData = k.split(',')
                    #Converting the content of the stocks list to a list to we can use the values
                    p = list(p)
                    #Try to get the price from the internet and store it to a temp list
                    try:
                        p[4] = float(stockData[1])*100
                        temp.append(p)
                        print('{}: {}'.format(p[0], (p[4]/100)))
                    #If that fails tell the user so and store the initial price to a temp list
                    except:
                        print('A current price for {} could not be found.'.format(stocks[o][0]))
                        p[4] = stocks[o][3]
                        temp.append(p)
            #Store the temp list to the stocks list and tell the user it's done
            stocks = temp
            print('Stock prices updated!')

        #Conditional for choice 'R' or 'r'
        #Prints out the stocks list in required format based on
        #another set of conditionals for 'Name' or 'Value'
        if choice == 'r':
            sort = input('Sort output by (N)ame, or (V)alue? ').lower()

            #Sub-Conditional for choice 'V' or 'v'
            #Prints out stocks list in value-order
            if sort == 'v':
                vSort = sorted(stocks, key=itemgetter(5))
                printTable(vSort)

            #Sub-Conditional for choice 'N' or 'n'
            #Prints out stocks list in name-order
            if sort == 'n':
                nSort = sorted(stocks, key=itemgetter(1))
                printTable(nSort)

        #Conditioanl for choice 'Q' or 'q'
        #Allows the user to quit
        if choice == 'q':
            save = input('Save {} (y/n)? '.format(iFile))

            #Conditional for choice 'Y' or 'y'
            #For saving the datatbase
            if save.lower() == 'y':

                #Conditional for when their is no such file.
                if iFile == "":
                    fName = input('Save file as: ')
                    db = sqlite3.connect(fName)
                    executeDatabase(db, stocks)

                #Conditional to overwrite the database with the new information
                else:
                    executeDatabase(db, stocks)

            #Conditional for choice 'N' or 'n'
            #For not saving the datatbase
            if save.lower() == 'n':
                pass

            print('Bye!')
            flag = False

#Method for printing the table
def printTable(stockSort):
    totalCurrentValue = 0
    totalInitialValue = 0
    totalGL = 0
    print('\nCompany                   Shares   Pur.  Latest   Value     G/L')
    print('=================================================================')
    for i in stockSort:
        totalCurrentValue += (i[5])
        totalInitialValue += ((i[2])*(i[3]/100))
        totalGL = (-1 + ( (totalCurrentValue) / (totalInitialValue)))*100
        name = i[1] + " (" + i[0] + ")"
        print('{0: <27}'.format(name) + '{0: >4}'.format(i[2]) + '{:8.2f}'.format(i[3]/100) + '{:8.2f}'.format(i[4]/100) + '{0: >8}'.format(int(i[5])) + '{:8.1f}%'.format(i[6]))
    print('{0: <50}'.format('') +'{:16}'.format('---------------'))
    print('{0: <47}'.format('') + '{0: >8}'.format(int(totalCurrentValue)) + '{:8.1f}%'.format(totalGL))
    print('{0: <50}'.format('') +'{:16}'.format('==============='))

#Metjod for creating and saving the table in the database
def executeDatabase(db, stockList):
    db.execute('drop table if exists portfolio')
    db.execute('create table portfolio (ticker TEXT PRIMARY KEY, company TEXT, shares NEAR, initial NEAR, current NEAR, value REAL, gl REAL)')
    for row in stockList:
        db.execute('insert into portfolio (ticker, company, shares, initial, current, value, gl) values (?, ?, ?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    db.commit()

if __name__== '__main__': main()
