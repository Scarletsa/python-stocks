#CRUD FUNCTIONAILITY MODULE
import sqlite3

# Function for adding new stocks into databse
def insert(database, row):
    database.execute('insert into portfolio (ticker, company, shares, initial, current) values (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], row[4]))
    database.commit()

# Function for finding stocks in the database.
def retrieve(database, ticker):
    cursor = database.execute('select * from portfolio where ticker = ?', (ticker,))
    print(cursor.fetchone())

# Function for deleting stocks from the database.
def delete(database, ticker):
    database.execute('delete from portfolio where ticker = ?', (ticker,))
    database.commit()

# Function for displaying all of the stocks in the database.
def disp_rows(database):
    cursor = database.execute('select * from portfolio order by company')
    totalValue = 0
    totalGL = 0
    for row in cursor:
        comp = row[1] + " (" + row[0] + ")"
        gl = (-1 + ( (row[2]*row[4]) / (row[2]*row[3]) ))*100
        print('{0: <27}'.format(comp) + '{0: >4}'.format(row[2]) + '{:8.2f}'.format(row[3]) + '{:8.2f}'.format(row[4]) + '{0: >8}'.format(int((row[2]*row[4]))) + '{:8.1f}%'.format(gl))
        totalValue += (row[2]*row[4])
        totalGL += ((row[2]*row[4])/(row[2]*row[3]))

def main():
    pass

if __name__ == "__main__": main()
