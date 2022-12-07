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
    print("4 - Change Database") 
    print("5 - Exit")

    selection = input("please select 1, 2, 3, 4, 5: ")

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
                data_manipulate(cur, cnx)
            if sub_select == '2':
                data_view(cur, cnx)
        if sub_selection == '2':
            add_art_object_from_file(cur, cnx)
    if selection == '5':
        exit()
    else:
        print("Invalid selection, please try again")
        admin_consol(cur, cnx)

def data_manipulate(cur, cnx):
    command = input("Please enter the command you want to execute, enter q to quit: ")
    while (command != 'q'):
        cur.execute(command)
        cnx.commit()
        print("\nCommand executed successfully!\n")
        command = input("Please enter the command you want to execute, enter q to quit: ")
    
def add_user(cur, cnx):
    print("\nWelcome to the Add User Consol:")
    print("1 - Add New Admin")
    print("2 - Add New Data Entry User")
    sub_selection = input("please select 1 or 2: ")

    if sub_selection == '1':
        add_admin(cur, cnx)

    pass

def add_admin(cur, cnx):
    print("\nWelcome to the Add Admin Consol:")
    print("Please enter the following information:")
    username = input("User Name: ") or None
    password = input("Password: ") or None

    sqlDropUser = "DROP USER IF EXISTS %s@localhost"
    sqlCreateUser = "CREATE USER %s@localhost IDENTIFIED WITH mysql_native_password BY '%s'"
    sqlGrantUser = "GRANT db_admin@localhost TO %s@localhost"
    sqlDefaultUser = "SET DEFAULT ROLE ALL TO %s@localhost" 

    cur.execute(sqlDropUser, (username,), multi=True)
    cur.execute(sqlCreateUser, (username, password,), multi=True)
    cur.execute(sqlGrantUser, (username,), multi=True)
    cur.execute(sqlDefaultUser, (username,), multi=True)
    cnx.commit()
    print("\nAdmin added successfully!\n")
    admin_consol(cur, cnx)
    pass

def add_data_entry(cur, cnx):
    print("\nWelcome to the Add Data Entry Consol:")
    print("Please enter the following information:")
    username = input("User Name: ") or None
    password = input("Password: ") or None

    #sqlDropUser = "

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
    print("\nWelcome to the Data Entry Consol:")
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
        data_entry_consol(cur, cnx)

def lookup(cur, cnx):
    print("\nWelcome to the lookup Consol:")
    print("1 - Lookup Artist")
    print("2 - Lookup Painting")
    print("3 - Lookup Sculpture")
    print("4 - Lookup Statue")
    print("5 - Lookup Other")
    print("6 - Lookup Collection")
    print("7 - Lookup Exhibitions")
    print("8 - Lookup On Display")
    print("9 - Go Back")

    selection = input("please select 1, 2, 3, 4, 5, 6, 7, 8: ")

    if selection == '1':
        artist_name = input("Please enter the name of the artist: ")
        specific_lookup(cur, cnx, 'artist', artist_name)
    if selection == '2':
        painting_name = input("Please enter the id_no of the painting: ")
        specific_lookup(cur, cnx, 'painting', painting_name)
    if selection == '3':
        sculpture_name = input("Please enter the id_no of the sculpture: ")
        specific_lookup(cur, cnx, 'sculpture', sculpture_name)
    if selection == '4':
        statue_name = input("Please enter the id_no of the statue: ")
        specific_lookup(cur, cnx, 'statue', statue_name)
    if selection == '5':
        other_name = input("Please enter the id_no of the other: ")
        specific_lookup(cur, cnx, 'other', other_name)
    if selection == '6':
        collection_name = input("Please enter the Name of the collection: ")
        specific_lookup(cur, cnx, 'collection', collection_name)
    if selection == '7':
        exhibition_name = input("Please enter the Name of the exhibition: ")
        specific_lookup(cur, cnx, 'exhibition', exhibition_name)
    if selection == '8':
        on_display_name = input("Please enter the id_no of the art object to check if it is on display or not: ")
        specific_lookup(cur, cnx, 'on_display', on_display_name)
    if selection == '9':
        data_entry_consol(cur, cnx)
    else:
        print("Invalid selection, please try again")
        lookup(cur, cnx)

def add(cur, cnx):
    print("\nWelcome to the Add Consol:")
    print("1 - Add Art Object")
    print("2 - Add Artist")
    print("3 - Add Collection")
    print("4 - Add piece into collection")
    print("5 - Add Exhibition")
    print("6 - Add On Display")
    print("7 - Go Back")

    selection = input("please select 1, 2, 3, 4, 5, 6, 7: ")

    if selection == '1':
        from_file = input("Would you like to add the art object from a file? (y/n): ")
        if from_file == 'y':
            add_art_object_from_file(cur, cnx)
        category = input(print("\nWhich category of art object would you like to add?\n Please make sure to enter the correctly spelled category name: "))
        location = input(print("Please enter if the art object is borrowed or part of the permanent collection: "))
        values = input(print("Please enter the values for the art object in the following format: \n (id_no, origin, title, epoch, description, year) \n Please make sure to enter the values in the correct order seperated by commas: "))

        art_object_sqlcommand = "INSERT INTO art_object (id_no, origin, title, epoch, description, year) VALUES (%s)"
        cur.execute(art_object_sqlcommand, (values))
        cnx.commit()

        if category == 'painting':
            painting_sqlcommand = "INSERT INTO painting (id_no, paint_type, drawn_on, style) VALUES (%s)"
            cur.execute(painting_sqlcommand, (values, location))
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
    print("What Information are you looking for: ")
    print("1- ")
    print("1- Event information")
    print("2- Participant information")
    print("3- Country information")
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



'''
# Get a cursor
cur = cnx.cursor()


# Execute a query
cur.execute("use olympicarchery")



# Fetch results
col_names=cur.column_names
print("Attribute List:\n")
att_size=len(col_names)
for i in range(att_size):
    print(col_names[i],'\t',end='')
print()
print(120*'-')


rows = cur.fetchone()
print("number of entries in table\n",len(rows))
print("Current employee table content:\n ",rows)
rows = cur.fetchall()
print("number of entries in table\n",len(rows))
print("Current employee table content:\n ",rows)

# a slightly better way
cur.execute("select * from employee")
rows = cur.fetchall()
print("Current employee table content:\n ")
size=len(rows)
for i in range(size):
    for x in range(len(rows[i])):
        print(rows[i][x],end='\t')
    print()

insert_employee=("insert into employee "
                  "values (%(fname)s,%(minit)s,%(lname)s,%s,%s,%s,%s,%d,%s,%s)")
employee_data= ('m','e','k','010101010',None,None,None,55500,None,4)

emp_data={
    'fname':'Maan',
    'lname':'k',
    'ssn':'',

}
cur.execute(insert_employee,emp_data)
#cur.execute(insert_employee,employee_data)
cur.execute("insert into employee values ('m','e','k','101010101',null,null,null,55500,null,4)")
cnx.commit()

# Close connection
cnx.close()
'''