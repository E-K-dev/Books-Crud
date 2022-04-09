import sqlite3 as sql;
import os 

def clean(): # Clean function it's the same than cls in windows.
    if os.name == 'nt' or os.name == 'msdos':
        os.system('cls'); # Cls for windows.
        pass
    else:
        os.system('clear'); # And clear for the rest.
        pass
    pass # Next function or code.

name_table = str('books'); # This is the name of the table

def sqlite_main(): # Create table and configurations
    # Sqlite part.
    conexion = sql.connect('database.db');
    conexion.commit();
    cursor = conexion.cursor();
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {name_table}(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(15000000) NOT NULL,
            Description VARCHAR(15000000) NOT NULL 
        );
    ''');
    conexion.commit();
    conexion.close();
    # End Sqlite part.
    pass

def main(): # This is the menu funtion.
    sqlite_main(); # We execute the sqlite_main function
    clean(); # Execute the clean function.
    version = str('1.1'); # Version
    autor = str('Axel Ezequiel Kampmann.');
    first = str(f'''# Main Menu [Books Api]

 [/] Version : {version} 

 [/] Using Sqlite as database.

 [/] Author : {autor}

 [/] Opciones / Options :

 [1] - Create a book.

 [2] - Show all the books.

 [3] - Delete one book.

 [4] - Delete all books.
 
 [xx] - Close the application.
''')
    print(first); # Print first variable.
    options = str(input(' Select one option >> ')).lower();

    if options == '1':
        create_book();
    elif options == '2':
        show_all();
    elif options == '3':
        delete_one();
    elif options == '4':
        delete_all();
    elif options == 'xx':
        exit();
    else:
        print(f'\n[!] Option "{options}" was invalid\n\n');
        exit();
    pass

def create_book(): # 1 Function about books
    clean(); # Execute the clean function.
    name = str(input('! Insert a name for the new book >> '));
    content = str(input('\n\n! Insert a description for the new book >> '));

    if name.lower() == ' ' or name.lower() == '' or content.lower() == ' ' or content.lower() == '': # Error or null if.
        clean(); # Execute the clean function.
        print('<!> Null , You have complete all the inputs\n'.upper());
        exit();

    else:
        # Sqlite part.
        conexion = sql.connect('database.db');
        conexion.commit(); # We connect to the database.
        cursor = conexion.cursor();
        cursor.execute(f'''INSERT INTO {name_table}(Name,Description) VALUES ('{name}' , '{content}');''');
        conexion.commit();
        conexion.close();
        # End Sqlite part.

        clean(); # Execute the clean function.
        print(f'[/] Book ["{name}"] has been created!\n\n');
        exit();

def show_all(): # 2 function about books
    clean(); # Execute the clean function.
    # Sqlite connection
    conexion = sql.connect('database.db');
    cursor = conexion.cursor();
    conexion.commit(); # We connect to the database.
    cursor.execute(f'''SELECT * FROM {name_table}''');
    data = cursor.fetchall(); # Fetch all information of cursor object.
    conexion.close(); # We close the connection to the database.
    # End sqlite connection


    if data == []: # Check the information recived
        clean();
        print('''<!> There ain't noathing in the database.\n\n''');
        exit();

    else: # If we have some information , we print it 
        print('|Bookid| , |Title| , |Description|'); # The information will arrive using these format (BookId , Title and Description)
        for information in data: # We extract all the information about data , for then print it.
            print('|' + str(information[-3]) + '     | , ' + '|' + str(information[-2]) + '| , ' + ' |' + str(information[-1]) + '| , ');

        pass
    pass

def delete_one(): # 3 Function about books.
    clean(); # Execute the clean function.
    bookid = str(input('Ok , send me the id of the book >> ').lower())

    # Sqlite connection
    conexion = sql.connect('database.db');
    cursor = conexion.cursor();
    conexion.commit(); # We connect to the database.
    cursor.execute(f'''SELECT * FROM {name_table} WHERE ID = {bookid}''');
    data = cursor.fetchall(); # Fetch all information of cursor object.
    conexion.close(); # We close the connection to the database.
    # End sqlite connection


    if data == []: # Check the information recived
        clean();
        print('''<!> There ain't noathing in the database.\n\n''');
        exit();

    else: # Else if we have information , we delete all the information charged in an id.
        clean();
        # Sqlite connection
        conexion = sql.connect('database.db');
        cursor = conexion.cursor();
        conexion.commit(); # We connect to the database.
        cursor.execute(f'''DELETE FROM {name_table} WHERE ID = {bookid}''');
        conexion.commit(); # We execute the script.
        conexion.close(); # We close the connection to the database.
        # End sqlite connection

        print(f"[/] Book has been deleted '[{bookid}]' , from database\n\n");
        exit();
        pass

def delete_all(): # 4 Function about books.
    clean(); # Execute the clean function.

     # Sqlite connection
    conexion = sql.connect('database.db');
    cursor = conexion.cursor();
    conexion.commit(); # We connect to the database.
    cursor.execute(f'''SELECT * FROM {name_table}''');
    data = cursor.fetchall(); # Fetch all information of cursor object.
    conexion.close(); # We close the connection to the database.
    # End sqlite connection


    if data == []: # Check the information recived
        clean();
        print('''<!> There ain't noathing in the database.\n\n''');
        exit();

    else: # Else if have information , we delete all the table.
        #Sql part and script
        conexion = sql.connect('database.db');
        cursor = conexion.cursor();
        cursor.execute(f'DROP TABLE IF EXISTS {name_table};'); # Execute the script.
        conexion.commit();
        conexion.close();
        #End sql part and script

        print(f'[/] Table "books" has been deleted.\n\n'); # Print delete message.
        exit();

main(); # Execute the main function.