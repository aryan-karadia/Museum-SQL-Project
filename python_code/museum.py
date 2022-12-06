import mysql.connector

def admin_consol(cur):
    print("\nWelcome to the Admin Consol:")
    print("1 - Add New User")
    print("2 - Edit User")
    print("3 - Block User")
    print("4 - Change Database") #data_entry, put into data entry; reduce redundancy

    selection = input("please select 1, 2, 3, or 4: ")

    if selection == '1':
        add_user(cur)



    pass

def add_user(cur):
    print("\nWelcome to the Add User Consol:")
    print("1 - Add New Admin")
    print("2 - Add New Data Entry")
    sub_selection = input("please select 1 or 2: ")

    if sub_selection == '1':
        add_admin(cur)

    pass

def add_admin(cur):
    print("Welcome to the Add Admin Consol:")
    print("Please enter the following information:")
    username = input("User Name: ")
    password = input("Password: ")
    cur.execute('DROP USER IF EXISTS %s@localhost', (username,))
    cur.execute('CREATE USER %s@localhost IDENTIFIED WITH mysql_native_password BY %s', (username, password))
    cur.execute('GRANT ALL PRIVILEGES ON museum.* TO %s@localhost', (username,))
    cur.execute('FLUSH PRIVILEGES')
    cur.commit()
    print("Admin added successfully!")
    pass


def data_entry():
    pass

def guest_view():
    print("Waht are you looking for:")
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
        join = 'from athlete naturaljoin PARTICIPANT'
    

    #instr="select * from athlete where olympicid = %(oid)s"
    instr="select * from athlete"
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
        username= input("user name:")
        passcode= input("password:")

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
        admin_consol(cur)
    elif selection == '2':
        data_entry()
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