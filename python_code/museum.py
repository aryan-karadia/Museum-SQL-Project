import mysql.connector

def format(cur, cnx):
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

def admin_consol(cur, cnx):
    print("\nWelcome to the Admin Consol:")
    print("1 - Add New User")
    print("2 - Edit User")
    print("3 - Block User")
    print("4 - Change Database") #data_entry, put into data entry; reduce redundancy
    print("5 - Exit")

    selection = input("\nplease select 1, 2, 3, 4, 5: ")

    if selection == '1':
        add_user(cur, cnx)
    if selection == '4':
        print("\nWelcome to the Database Consol:")
        print("1 - Edit database through command line")
        print("2 - Edit database using a source file")
        sub_selection = input("please select 1 or 2: ")
        if sub_selection == '1':
            print("\nWould you like to manipulate the database or view the database?")
            print("1 - Manipulate")
            print("2 - View")
            sub_select = input("please select 1 or 2: ")
            if sub_select == '1':
                data_manipulate(cur, cnx, 'admin')
            if sub_select == '2':
                data_view(cur, cnx, 'admin')
        if sub_selection == '2':
            filename = input("Please enter the name of the file you want to use: ")
            with open(filename, 'r') as f:
                for line in f:
                    cur.execute(line)
                cur.commit()
                print("Database updated successfully!")
    if selection == '5':
        exit()

def data_manipulate(cur, cnx, usr):
    command = input("Please enter the command you want to execute, enter q to quit: ")
    while (command != 'q'):
        cur.execute(command)
        cnx.commit()
        print("\nCommand executed successfully!\n")
        command = input("Please enter the command you want to execute, enter q to quit: ")
    if usr == 'admin':
        admin_consol(cur, cnx)
    if usr == 'data_entry':
        data_entry_consol(cur, cnx)
    
def add_user(cur, cnx):
    print("\nWelcome to the Add User Consol:")
    print("1 - Add New Admin")
    print("2 - Add New Data Entry User")
    sub_selection = input("\nplease select 1 or 2: ")

    while sub_selection != '1' and sub_selection != '2':
        print("Invalid selection, please try again")
        sub_selection = input("please select 1 or 2: ")

    if sub_selection == '1':
        add_admin(cur, cnx)
    
    if sub_selection == '2':
        add_data_entry(cur, cnx)

    

def add_admin(cur, cnx):
    print("\nWelcome to the Add Admin Consol:")
    print("Please enter the following information:")
    # Prompt the user for their desired username and password
    
    username = input("Enter your desired username: ")
    password = input("Enter your desired password: ")

    # Delete the user if it already exists
    sqlDropUser = "DROP USER IF EXISTS %s@'localhost'"
    try:
        cur.execute(sqlDropUser, (username,))
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error deleting user: Access denied. You may need to grant the CREATE USER privilege to the current user.")
        else:
            print("Error deleting user: ", err)

    # Create a new user with the given username and password
    sqlCreateUser = "CREATE USER %s@'localhost' IDENTIFIED WITH 'mysql_native_password' BY %s"
    try:
        cur.execute(sqlCreateUser, (username, password,), multi=True)
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error creating user: Access denied. You may need to grant the CREATE USER privilege to the current user.")
        else:
            print("Error creating user: ", err)

    # Grant the user the db_admin role
    sqlGrantUser = "GRANT db_admin@localhost TO %s@'localhost'"
    try:
        cur.execute(sqlGrantUser, (username,))
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error granting user role: Access denied. You may need to grant the WITH ADMIN, ROLE_ADMIN, SUPER privileges to the current user.")
        else:
            print("Error granting user role: ", err)

    # Set the db_admin role as the default role for the user
    sqlDefaultUser = "SET DEFAULT ROLE ALL TO %s@'localhost'" 
    try:
        cur.execute(sqlDefaultUser, (username,))
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error setting default role: Access denied. You may need to grant the CREATE USER privilege to the current user.")
        else:
            print("Error setting default role: ", err)

    # Flush the privileges to make the changes take effect
    sqlFlush = "FLUSH PRIVILEGES"
    cur.execute(sqlFlush)

    print("\nAdmin added successfully!\n")
	
    # Check to see if the user was added successfully
    instr = "select * from information_schema.USER_PRIVILEGES"
    cur.execute(instr)
    format(cur,cnx)
    admin_consol(cur, cnx)



def add_data_entry(cur, cnx):


    print("\nWelcome to the Add Data Entry Consol:")
    print("Please enter the following information:")

    # Prompt the user for their desired username and password
    username = input("User Name: ") or None
    password = input("Password: ") or None

    # Delete the user if it already exists
    sqlDropUser = "DROP USER IF EXISTS %s@localhost"
    cur.execute(sqlDropUser, (username,))
    
    # Create a new user with the given username and password
    sqlCreateUser = "CREATE USER %s@localhost IDENTIFIED WITH mysql_native_password BY %s"
    cur.execute(sqlCreateUser, (username, password,), multi=True)

    # Grant the user the db_entry role
    sqlGrantUser = "GRANT db_entry@localhost TO %s@'localhost'"
    cur.execute(sqlGrantUser, (username,))

    # Set the db_entry role as the default role for the user
    sqlDefaultUser = "SET DEFAULT ROLE ALL TO %s@localhost"
    cur.execute(sqlDefaultUser, (username,))

    cnx.commit()

    print("\Data Entry User added successfully!\n")

    # Check to see if the user was added successfully
    instr = "select * from information_schema.USER_PRIVILEGES"
    cur.execute(instr)
    format(cur,cnx)
    admin_consol(cur, cnx)    

def data_view(cur, cnx, usr):
    command = input("Please enter the command you want to execute, enter q to quit: ")
    print()
    while (command != 'q'):
        cur.execute(command)
        format(cur, cnx)
        command = input("Please enter the command you want to execute, enter q to quit: ")
    if usr == 'admin':
        admin_consol(cur, cnx)
    if usr == 'data_entry':
        data_entry_consol(cur, cnx)

def data_entry_consol(cur, cnx):
    pass

def guest_view():
    print("What Information are you looking for: ")
    print("1 - Event information")
    print("2 - Participant information")
    print("3 - Country information\n")
    selection = input()

    if selection == '2':
        subselection = input('Please type 1 for Athletes or 2 for Coaches:\n')
        if subselection == '1':
            athlete_info(cur)


def athlete_info(cur):

    instr=""
    join=""
    att_selection = input("Do you want to see the Athlete name ? Y or N: ")
    if att_selection == 'Y':
        join = 'from museum naturaljoin PARTICIPANT'
    

    #instr="select * from athlete where olympicid = %(oid)s"
    instr="select * from museum"
    searchkey=input("please insert the olympicid of the athlete you are looking for (press Enter to view all):") or None

    #cur.execute(instr,{'oid':searchkey})
    cur.execute(instr)
    col_names=cur.column_names
    search_result=cur.fetchall()
    print("Search found ",len(search_result)," Entries:\n")
    header_size=len(col_names)
    for i in range(header_size):
        print("{:<15s}".format(col_names[i]),end='')
    print()
    print(15*header_size*'-')
    for row in search_result:
        for val in row:
            print("{:<15s}".format(str(val)),end='')
        print()
        





if __name__ == "__main__":
    
    # Connect to server
    print("\nWelcome to the Museum Database:")
    print("In order to proceed please select your role from the list below:")
    print("1 - DB Admin")
    print("2 - Data Entry")
    print("3 - Browse as guest\n")

    selection = input("please type 1, 2, or 3 to select your role:")

    if selection in ['1','2']:
        username= input("User name: ")
        passcode= input("Password: ")

    else:
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
        admin_consol(cur, cnx)
    elif selection == '2':
        data_entry_consol(cur, cnx)
    else:
        guest_view()
    

    
    #insert example
    inst_country_template= "insert into country values (%s,%s,%s,%s)"

    countryname= input("Please insert name of country to add: ")
    gnum = input("How many gold medals do this country have (press enter and leave blank if unknown): ") or None
    snum = input("How many silver medals do this country have (press enter and leave blank if unknown): ") or None
    bnum = input("How many bronze medals do this country have (press enter and leave blank if unknown): ") or None

    print(type(gnum))
    print(type(snum))

    inst_country_data = (countryname,gnum,snum,bnum)
    cur.execute(inst_country_template,inst_country_data)
    cnx.commit()

    
    
    # Close connection
    cnx.close()