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
            shares = input('Number of shares: ')
            price = input('Purchase price per share: ')

            insert(db, (symbol, company, shares, price))

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

        #Conditional for choice 'U' or 'u'
        #Updates the current values of the stocks in portfolio.dat
        if choice == 'u':
            print('Update stock prices (<Return> to keep current values)...')

        #Conditional for choice 'R' or 'r'
        #Prints out the portfolio.dat in required format based on
        #another set of conditionals for 'Name' or 'Value'
        if choice == 'r':
            sort = input('Sort output by (N)ame, or (V)alue? ').lower()

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
