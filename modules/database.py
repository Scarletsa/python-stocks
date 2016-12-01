#CRUD FUNCTIONAILITY MODULE
import sqlite3

# Function for adding new stocks into databse
def insert(database, row):
    database.execute('insert into students (ticker, company, shares, initial, current) values (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], row[4]))
    database.commit()

# Function for finding stocks in the database.
def retrieve(database, ticker):
    cursor = database.execute('select * from portfolio where name = ?', (ticker,))
    print(cursor.fetchone())

# Function for deleting stocks from the database.
def delete(database, ticker):
    database.execute('delete from students where name = ?', (ticker,))
    database.commit()

# Function for displaying all of the stocks in the database.
def disp_rows(database):
    cursor = database.execute('select * from portfolio order by ticker')
    totalValue = 0
    totalGL = 0
    for row in cursor:
        print('({} ({}), {}, {}, {}, {}, {})'.format(row[1], row[0], row[2], row[3], row[4], (row[2]*row[4]), ((row[2]*row[4])/(row[2]*row[3]))))
        totalValue += (row[2]*row[4])
        totalGL += ((row[2]*row[4])/(row[2]*row[3]))

def main():
    
if __name__ == "__main__": main()
