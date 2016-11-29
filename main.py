import database.py

def main():
     # Initial stocks
    initialStocks = [['MMM', '3M', '100', '74.00', '118.30'],
                     ['MDT', 'Medtronic', '50', '56.10', '48.00'],
                     ['NWAC', 'Northwest Airlines', '100', '67.50', '18.04'],
                     ['SGI', 'Silicon Graphics', '100', '22.25', '2.25']]

    # Creating a database called students.
    db = sqlite3.connect('portfolio.dat')

    flag == true

    while flag == true:
        choice = input("(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? ").lower()

        if choice == a:
            print('Add a stock to your portfolio!\n')
            
        
        if choice == d:
            delete = input('Enter the ticker symbol of the stock to remove: ')

        if choice == l:
            file = input('Load file: ')
            db = sqlite3.connect(file)
            db.execute('drop table if exists students')
            db.execute('create table students (name TEXT PRIMARY KEY, age NEAR, class TEXT, gpa REAL)')  

        if choice == u:

        if choice == r:
            sort = input('Sort output by (N)ame, or (V)alue? ').lower()
            
            if sort == v:

            if sort == n:

        if choice == q:
            save = input('Save {} (y/n)? '.format(file))
            
            if save.lower() == y:

            if save.lower() == n:

            print('Bye!')
            flag = false

    
    url = 'http://finance.yahoo.com/d/quotes.csv?s={}&f=sl1d1t1c1ohgv&e=.csv'.format()

    shares = 100
    pp = 22.25
    latest = 2.25
    value = shares*latest
    G/L = float((shares*latest)/(shares*pp))
    
if __name__== '__main__': main()
