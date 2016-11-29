# CSCI 2061, Assignment 11, program 02
# Michael Albrecht

import sqlite3

# Function for adding new students to the database.
def insert(db, row):
    db.execute('insert into students (name, age, class, gpa) values (?, ?, ?, ?)', (row[0], row[1], row[2], row[3]))
    db.commit()

# Function for finding students in the database.
def retrieve(db, name):
    cursor = db.execute('select * from students where name = ?', (name,))
    print(cursor.fetchone())

# Function for deleting students from the database.
def delete(db, name):
    db.execute('delete from students where name = ?', (name,))
    db.commit()

# Function for displaying all of the students in the database.
def disp_rows(db):
    cursor = db.execute('select * from students order by gpa')
    for row in cursor:
        print('(\'{}\', {}, \'{}\', {})'.format(row[0], float(row[1]), row[2], row[3]))

def main():
    # Initial stocks
    initialStocks = [['MMM', '3M', '100', '74.00', '118.30'],
                     ['MDT', 'Medtronic', '50', '56.10', '48.00'],
                     ['NWAC', 'Northwest Airlines', '100', '67.50', '18.04'],
                     ['SGI', 'Silicon Graphics', '100', '22.25', '2.25']]

    # Creating a database called students.
    db = sqlite3.connect('portfolio.dat')

    # Deleting the table students if it already exists, and then creating one.
    db.execute('drop table if exists students')
    db.execute('create table students (name TEXT PRIMARY KEY, age NEAR, class TEXT, gpa REAL)')   

    # Adding the students from the list into the database.
    for each in studentList:
        insert(db, each)

    # Display header.
    print('After creation database is: ')
    # Displaying the rows of the database.
    disp_rows(db)
    print()

    # Making sure we go through the loop once.
    again = 'y'
    while (again.lower() == 'y'):
        # Prompting the user fot the students name, age, year and gpa.
        name = input('Please enter student name: ')
        age = input('Please enter student age: ')
        year = input('Please enter student year: ')
        gpa = float(input('Please enter student gpa: '))
        # Adding that student to the database.
        insert(db, (name, age, year, gpa))
        # Prompting the user to go again.
        again = input('Go again? ')

    # Display header.
    print('\nAfter additions, database is: ')
    # Displaying the rows of the database.
    disp_rows(db)
    print()

    # Prompting the user to search for a student.
    search = input('Student to search for? ')
    # Looking in the database for that person.
    retrieve(db, search)
    print()

    # Prompting the user for a student to delete.
    bye = input('Student to delete? ')
    # Deleting that student from the database.
    delete(db, bye)

    # Display header.
    print('\nAfter deletion, database is:')
    # Displaying the rows of the database.
    disp_rows(db)

if __name__ == "__main__": main()
