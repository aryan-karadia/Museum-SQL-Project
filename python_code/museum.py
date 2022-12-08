import mysql.connector

def format(cur, cnx):
    #formatting the output of the query
    col_names = cur.column_names
    search_result = cur.fetchall()
    print("Search found ", len(search_result), " Entries:\n")
    header_size = len(col_names)
    for i in range(header_size):
        print("{:<35s}".format(col_names[i]), end='')
    print()
    print(30 * header_size * '-')
    for i in range(len(search_result)):
        for x in range(len(search_result[i])):
            print("{:<35s}".format(str(search_result[i][x])), end='')
        print()

def admin_console(cur, cnx):
    print("\nWelcome to the Admin console:")
    print("1 - Add New User")
    print("2 - Manage Users")
    print("3 - Edit Database") 
    print("4 - Exit")

    selection = input("please select 1, 2, 3, 4: ")

    if selection == '1':
        add_user(cur, cnx)
    if selection == '2':
        manage_users(cur, cnx)

    if selection == '3':
        print("\nWelcome to the Database console:")
        print("1 - Edit database through command line")
        print("2 - Edit database using a source file")
        sub_selection = input("please select 1 or 2: ")
        if sub_selection == '1':
            print("\nWould you like to manipulate the database or view the database?")
            print("1 - Manipulate")
            print("2 - View")
            sub_select = input("please select 1 or 2: ")
            if sub_select == '1':
                data_manipulate(cur, cnx)
            if sub_select == '2':
                data_view(cur, cnx)
        if sub_selection == '2':
            add_art_object_from_file(cur, cnx)
    if selection == '4':
        exit()
    else:
        print("Invalid selection, please try again")
        admin_console(cur, cnx)

def data_manipulate(cur, cnx):
    # This function allows the user to manipulate the database through the command line using exact sql commands
    command = input("Please enter the command you want to execute, enter q to quit: ")
    while (command != 'q'):
        cur.execute(command)
        cnx.commit()
        print("\nCommand executed successfully!\n")
        command = input("Please enter the command you want to execute, enter q to quit: ")
    
def add_user(cur, cnx):
    print("\nWelcome to the Add User console:")
    print("1 - Add New Admin")
    print("2 - Add New Data Entry User")
    sub_selection = input("please select 1 or 2: ")

    while sub_selection != '1' and sub_selection != '2':
        print("Invalid selection, please try again")
        sub_selection = input("please select 1 or 2: ")

    if sub_selection == '1':
        add_admin(cur, cnx)
    
    if sub_selection == '2':
        add_data_entry(cur, cnx)

    pass

def add_admin(cur, cnx):
    print("\nWelcome to the Add Admin console:")
    print("Please enter the following information:")
    username = input("User Name: ")
    password = input("Password: ")

    sqlDropUser = "DROP USER IF EXISTS %s@localhost"
    sqlCreateUser = "CREATE USER %s@localhost IDENTIFIED WITH mysql_native_password BY %s"
    sqlGrantUser = "GRANT db_admin@localhost TO %s@localhost"
    sqlGrantUser2 = "GRANT CREATE USER on *.* TO %s@localhost WITH GRANT OPTION"
    sqlDefaultUser = "SET DEFAULT ROLE ALL TO %s@localhost" 

    cur.execute(sqlDropUser, (username,), multi=True)
    cur.execute(sqlCreateUser, (username, password,), multi=True)
    cur.execute(sqlGrantUser, (username,), multi=True)
    cur.execute(sqlGrantUser2, (username,), multi=True)
    cur.execute(sqlDefaultUser, (username,), multi=True)
    cnx.commit()
    print("\nAdmin added successfully!\n")
    admin_console(cur, cnx)
    pass

def add_data_entry(cur, cnx):
    print("\nWelcome to the Add Data Entry console:")
    print("Please enter the following information:")
    username = input("User Name: ")
    password = input("Password: ")

    sqlDropUser = "DROP USER IF EXISTS %s@localhost"
    sqlCreateUser = "CREATE USER %s@localhost IDENTIFIED WITH mysql_native_password BY %s"
    sqlGrantUser = "GRANT db_entry@localhost TO %s@localhost"
    sqlDefaultUser = "SET DEFAULT ROLE ALL TO %s@localhost"

    cur.execute(sqlDropUser, (username,), multi=True)
    cur.execute(sqlCreateUser, (username, password,), multi=True)
    cur.execute(sqlGrantUser, (username,), multi=True)
    cur.execute(sqlDefaultUser, (username,), multi=True)
    cnx.commit()
    print("\nData Entry User added successfully!\n")
    admin_console(cur, cnx)
    pass

def manage_users(cur, cnx):
    print("\nWelcome to the Manage Users console:")
    print("1 - Edit User")
    print("2 - Block User")
    print("3 - Unblock User")

    selection = input("please select 1, 2, or 3: ")

    if selection == '1':
        print("\nWelcome to the Edit User console:")
        print("1 - Edit User Permissions")
        print("2 - Edit User Password")
        sub_selection = input("please select 1 or 2: ")
        username = input("Please enter the username of the user you want to edit: ")

        if sub_selection == '1':
            new_role = input("Please enter the new role of the user(admin/employee): ")
            if new_role == 'admin':
                new_role = 'db_admin'
            if new_role == 'employee':
                new_role = 'db_entry'
            cur.execute("REVOKE ALL PRIVILEGES, GRANT OPTION FROM %s@localhost", (username,), multi=True)
            sql = "GRANT %s@localhost TO %s@localhost"
            cur.execute(sql, (new_role, username,), multi=True)
            cur.execute("FLUSH Privileges")
            cnx.commit()
            print("\nUser edited successfully!\n")
            admin_console(cur, cnx)

        if sub_selection == '2':
            new_password = input("Please enter the new password of the user: ")
            sql = "ALTER USER %s@localhost IDENTIFIED BY %s"
            cur.execute(sql, (username, new_password,), multi=True)
            cnx.commit()
            print("\nUser edited successfully!\n")
            admin_console(cur, cnx)

    if selection == '2':
        username = input("Please enter the username of the user you want to block: ")
        sql = "REVOKE ALL ON *.* FROM %s@localhost"
        cur.execute(sql, (username,), multi=True)
        cnx.commit()
        print("\nUser blocked successfully!\n")
        admin_console(cur, cnx)
    
    if selection == '3':
        username = input("Please enter the username of the user you want to unblock: ")
        usr_role = input("Please enter the role of the user you want to unblock(admin/employee): ")
        if usr_role == 'admin':
            sql = "GRANT ALL ON *.* TO %s@localhost"
        if usr_role == 'employee':
            sql = "GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO %s@localhost"
        cur.execute(sql, (username,), multi=True)
        cnx.commit()
        print("\nUser unblocked successfully!\n")
        admin_console(cur, cnx)

def data_view(cur, cnx):
    # This function allows the user to view the database through the command line using exact sql commands
    command = input("Please enter the command you want to execute, enter q to quit: ")
    print()
    while (command != 'q'):
        cur.execute(command)
        format(cur, cnx)
        command = input("Please enter the command you want to execute, enter q to quit: ")

def data_entry_console(cur, cnx):
    print("\nWelcome to the Data Entry console:")
    print("1 - Lookup Information")
    print("2 - Add Information")
    print("3 - Edit Information")
    print("4 - Quit Program")

    selection = input("please select 1, 2, 3, 4: ")

    if selection == '1':
        lookup(cur, cnx)
    if selection == '2':
        add(cur, cnx)
    if selection == '3':
        edit(cur, cnx)
    if selection == '4':
        exit()
    else:
        print("Invalid selection, please try again")
        data_entry_console(cur, cnx)

def lookup(cur, cnx):
    # This function allows the user to lookup information in the database not using exact sql commands
    print("\nWelcome to the lookup console:")
    print("1 - Lookup Artist")
    print("2 - Lookup Art object")
    print("3 - Lookup Painting")
    print("4 - Lookup Sculpture")
    print("5 - Lookup Statue")
    print("6 - Lookup Other")
    print("7 - Lookup Collection")
    print("8 - Lookup Exhibitions")
    print("9 - Lookup On Display")
    print("10 - Go Back")

    selection = input("please select 1, 2, 3, 4, 5, 6, 7, 8, 9, 10: ")

    # Looking up each specific type of art object using primary key
    if selection == '1':
        artist_name = input("Please enter the name of the artist: ")
        specific_lookup(cur, cnx, 'artist', artist_name)
    if selection == '2':
        art_object_name = input("Please enter the id_no of the art object: ")
        specific_lookup(cur, cnx, 'art_object', art_object_name)
    if selection == '3':
        painting_name = input("Please enter the id_no of the painting: ")
        specific_lookup(cur, cnx, 'painting', painting_name)
    if selection == '4':
        sculpture_name = input("Please enter the id_no of the sculpture: ")
        specific_lookup(cur, cnx, 'sculpture', sculpture_name)
    if selection == '5':
        statue_name = input("Please enter the id_no of the statue: ")
        specific_lookup(cur, cnx, 'statue', statue_name)
    if selection == '6':
        other_name = input("Please enter the id_no of the other: ")
        specific_lookup(cur, cnx, 'other', other_name)
    if selection == '7':
        collection_name = input("Please enter the Name of the collection: ")
        specific_lookup(cur, cnx, 'collection', collection_name)
    if selection == '8':
        exhibition_name = input("Please enter the Name of the exhibition: ")
        specific_lookup(cur, cnx, 'exhibition', exhibition_name)
    if selection == '9':
        on_display_name = input("Please enter the id_no of the art object to check if it is on display or not: ")
        specific_lookup(cur, cnx, 'on_display', on_display_name)
    if selection == '10':
        data_entry_console(cur, cnx)
    else:
        print("Invalid selection, please try again")
        lookup(cur, cnx)

def add(cur, cnx):
    # This function allows the user to add information to the database not using exact sql commands
    print("\nWelcome to the Add console:")
    print("NOTE: You MUST add into art object before adding into any other table, other than creating a new collection or exhibition.")
    print("1 - Add Art Object")
    print("2 - Add Artist")
    print("3 - Add Collection")
    print("4 - Add piece into collection")
    print("5 - Add Exhibition")
    print("6 - Add On Display")
    print("7 - Adding from file")
    print("8 - Go Back")

    selection = input("please select 1, 2, 3, 4, 5, 6, 7: ")

    if selection == '1':
        #Figuring out which type of art object to add
        category = input(print("\nWhich category of art object would you like to add?\n Please make sure to enter the correctly spelled category name: "))
        location = input(print("Please enter if the art object is borrowed or part of the permanent_collection: "))
        values = input(print("Please enter the values for the art object in the following format: \n (id_no, origin, title, epoch, description, year) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))

        art_object_sqlcommand = "INSERT INTO art_object (id_no, origin, title, epoch, description, year) VALUES (%s)"
        cur.execute(art_object_sqlcommand, (values))
        cnx.commit()

        if category == 'painting':
            values = input(print("Please enter the values for the painting in the following format: \n (id_no, paint_type, drawn_on, style) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
            painting_sqlcommand = "INSERT INTO painting (id_no, paint_type, drawn_on, style) VALUES (%s)"
            cur.execute(painting_sqlcommand, (values))            
        if category == 'sculpture':
            values = input(print("Please enter the values for the sculpture in the following format: \n (id_no, material, height, weight, style) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
            sculpture_sqlcommand = "INSERT INTO sculpture (id_no, material, height, weight, style) VALUES (%s)"
            cur.execute(sculpture_sqlcommand, (values))           
        if category == 'statue':
            values = input(print("Please enter the values for the statue in the following format: \n (id_no, material, height, weight, style) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
            statue_sqlcommand = "INSERT INTO statue (id_no, material, height, weight, style) VALUES (%s)"
            cur.execute(statue_sqlcommand, (values))           
        if category == 'other':
            values = input(print("Please enter the values for the other in the following format: \n (id_no, type, style) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
            other_sqlcommand = "INSERT INTO other (id_no, material, type, style) VALUES (%s)"
            cur.execute(other_sqlcommand, (values))           
        if location == 'borrowed':
            values = input(print("Please enter the values for the borrowed art object in the following format: \n (id_no, collection_origin, date_borrowed, date_returned) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
            borrowed_sqlcommand = "INSERT INTO borrowed (id_no, collection_origin, date_borrowed, date_returned) VALUES (%s)"
            cur.execute(borrowed_sqlcommand, (values))            
        if location == 'permanent_collection':
            values = input(print("Please enter the values for the permanent_collection art object in the following format: \n (id_no, status, cost, date_acquired) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
            permanent_collection_sqlcommand = "INSERT INTO permanent_collection (id_no, status, cost, date_acquired) VALUES (%s)"
            cur.execute(permanent_collection_sqlcommand, (values))           
        cnx.commit()
        print("Database updated successfully!")

    if selection == '2':    
        values = input(print("Please enter the values for the artist in the following format:(id_no, name) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
        artist_sqlcommand = "INSERT INTO artist (id_no, name) VALUES (%s)"
        cur.execute(artist_sqlcommand, (values))
        cnx.commit()
        print("Database updated successfully!")
    
    if selection == '3':
        values = input(print("Please enter the values for the collection in the following format:(name, phone, contact_person, street_address, city, country, postal_code, type, description) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
        collection_sqlcommand = "INSERT INTO collection (name, phone, contact_person, street_address, city, country, postal_code, type, description) VALUES (%s)"
        cur.execute(collection_sqlcommand, (values))
        cnx.commit()
        print("Database updated successfully!")
    
    if selection == '4':
        values = input(print("Please enter the values for the piece entering a collection in the following format:(id_no, name) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
        exhibition_sqlcommand = "INSERT INTO in_collection (id_no, name) VALUES (%s)"
        cur.execute(exhibition_sqlcommand, (values))
        cnx.commit()
        print("Database updated successfully!")
    
    if selection == '5':
        values = input(print("Please enter the values for an exhibition in the following format:(name, start_date, end_date) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
        exhibition_sqlcommand = "INSERT INTO exhibitions (name, start_date, end_date) VALUES (%s)"
        cur.execute(exhibition_sqlcommand, (values))
        cnx.commit()
        print("Database updated successfully!")
    
    if selection == '6':
        values = input(print("Please enter the values for a piece being on_display or not in the following format:(id_no, name) \n Please make sure to enter the values in the correct order separated by commas. enter NULL for any unknown values: "))
        exhibition_sqlcommand = "INSERT INTO on_display (id_no, name) VALUES (%s)"
        cur.execute(exhibition_sqlcommand, (values))
        cnx.commit()
        print("Database updated successfully!")
    
    if selection == '7':
        from_file = input("Would you like to add the art object from a file? (y/n): ")
        if from_file == 'y':
            add_art_object_from_file(cur, cnx)

    if selection == '8':
        data_entry_console(cur, cnx)

    else:
        print("Invalid selection, please try again.")
        add(cur, cnx)

def edit(cur, cnx):
    print("What would you like to edit: ")
    print("1- Art Object")
    print("2- Artist")
    print("3- Collection")
    print("4- Piece entering a collection")
    print("5- Exhibition")
    print("6- Piece on display")
    print("7- Return to main menu")
    selection = input("Please enter the number of your selection: ")

    if selection == '1':
        old_value = input("Please enter the values of the art object you would like to edit, separated by spaces: ")
        old_value_list = old_value.split(' ')
        new_value = input("Please enter the new values for your selected values, separated by spaces. Make sure the order for both inputs are the same: ")
        new_value_list = new_value.split(' ')
        identifier = input("Please enter the id_no of the art objects you would like to edit, separated by commas if there are multiple: ")
        for i in range(len(old_value_list)):
            update(cur, cnx, 'art_object', old_value_list[i], new_value_list[i], identifier)
        print("Database updated successfully!")
        type = input("Are you editing a painting, sculpture, statue, or other? (enter full word): ")
        if type == 'painting':
            old_value = input("Please enter the values of the painting you would like to edit, separated by spaces: ")
            old_value_list = old_value.split(' ')
            new_value = input("Please enter the new values for your selected values, separated by spaces. Make sure the order for both inputs are the same: ")
            new_value_list = new_value.split(' ')
            identifier = input("Please enter the id_no of the painting you would like to edit, separated by commas if there are multiple: ")
        for i in range(len(old_value_list)):
            update(cur, cnx, type, old_value_list[i], new_value_list[i], identifier)
        print("Database updated successfully!")
    
def update(cur, cnx, table, old_value, new_value, identifier):
    sql = "UPDATE %s SET %s = %s WHERE id_no = %s"
    cur.execute(sql, (table, old_value, new_value, identifier,))
    cnx.commit()

def add_art_object_from_file(cur, cnx):
    filename = input("Please enter the name of the file you would like to add: ")
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cur.execute(command)
        except IOError as msg:
            print("Command skipped: ", msg)
    print("Database updated successfully!")
    
    
def specific_lookup(cur, cnx, lookup, identifier):
    sql = "SELECT * FROM %s WHERE id_no = %s"
    cur.execute(sql, (lookup, identifier,))
    format(cur, cnx)

def guest_view():
    pass

if __name__ == "__main__":
    
    # Connect to server
    print("Welcome to the Museum Database:")
    print("In order to proceed please select your role from the list below:")
    print("1 - DB Admin")
    print("2 - Data Entry")
    print("3 - Browse as guest")

    selection = input("please type 1, 2, or 3 to select your role:")

    if selection in ['1','2']:
        username= input("User name: ")
        passcode= input("Password: ")

    else:
        print("Enter username as 'guest' and no password\n")
        username="guest"
        passcode=None

    cnx = mysql.connector.connect(
        host="localhost",
        port=3306,
        user=username,
        password= passcode)  

    # Get a cursor
    cur = cnx.cursor()
    # Execute a query
    cur.execute("use museum")


    if selection == '1':
        admin_console(cur, cnx)
    elif selection == '2':
        data_entry_console(cur, cnx)
    else:
        guest_view()