# Museum-SQL-Project
### THIS PROJECT IS NOT COMPLETE AND CAN STILL BE FURTHER IMPROVED UPON. THIS IS A WORK IN PROGRESS.

**Group Members**

Aryan Karadia

Aditya Prasad

Rohil Singh Dhillon

Akshpreet Singh

## Project Description

The objective of this project is to design and implement a real-world database application using database design and SQL queries. This application allows for a museum to manage their art objects and events, as well as user access and management. The application addressed three main areas: managing art objects, managing users, and providing access control. The database design considered the requirements and functionality of different types of users, including admins, data entry users, and end users. Admins had the ability to add and edit users, block users, and make changes to the database, while data entry users were able to add and modify information in the database within the constraints of the database. End users were able to look up information in the database. All users needed to log in to the application. The application was implemented using Python and SQL. 

## My Contribution

I designed the enhanced-entity-relation diagram along with a short description of the design and any assumptions I had made. From the EER diagram, I mapped the relational model into a relational schema. Furthermore, I along with a fellow group member, created and implemented the python application of the project. This includes creating multiple functions and using pair programming to create the other functions. This also includes debugging the python application and checking every function for functionality.

### Challenges

What I found the most challenging to be was to implement the access control in MySQL using python. Having to send MySQL commands in a python application from user inputs was particularly challenging as the user needed permissions they did not have. This was solved through extensive debugging and research, and the solution was to give the admin user specific grant permissions to the database.


## Notes
To initially start this application, you have two credentials:
### Username: Administrator
### Password: password

or

### Username: employee
### Password: 12345

Signing in as guest requires no username or password inputs.

To open the museumEER.drawio file, you will need to download the VSCode Draw.io extension. This file is the enhanced entity relationship diagram of the database.

**VSCode Draw.io Extension**

Name: Draw.io Integration

Id: hediet.vscode-drawio

Description: This unofficial extension integrates Draw.io into VS Code.

Version: 1.6.4

Publisher: Henning Dieterichs

VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio

## Future Improvements
* Add a website or GUI to the application
* Add more tables to the database
* Add more data to the database

