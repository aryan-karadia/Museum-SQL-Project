CREATE DATABASE MUSEUM;
USE MUSEUM;
CREATE TABLE ART_OBJECT( id_no double,
						 Origin char(50),
						 Title char(50),
						 Epoch char(50),
                         Description char(50),
                         Year double,
                         PRIMARY KEY (id_no)
                         );
CREATE TABLE ARTIST  ( id_no double,
					   Name char(50),
					   Description char(50),
					   Date_born double,
                       Date_died double,
                       Country_of_origin char(50),
                       Epoch char(50),
                       Main_style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
CREATE TABLE PAINTING( id_no double,
					   paint_type char(50),
					   drawn_on char(50),
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
CREATE TABLE SCULPTURE( id_no double,
					   Material char(50),
					   Height double,
                       Weight double,
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
CREATE TABLE STATUE  ( id_no double,
					   Material char(50),
					   Height double,
                       Weight double,
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
CREATE TABLE OTHER   ( id_no double,
					   Type char(50),
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
CREATE TABLE COLLECTIONS ( Name char(50),
					   Phone double,
					   Contact_person char(50),
					   Street_address char(50),
                       City char(50),
                       Country char(50),
                       Postal_code char(50),
                       Type char(50),
                       Description char(50),
					   PRIMARY KEY (Name)
					   );
CREATE TABLE PERMANENT_COLLECTION   ( id_no double,
					   Status char(50),
					   Cost double,
                       Date_acquired char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no)
					   );
CREATE TABLE BORROWED   ( id_no double,
					   Collection_origin char(50),
                       Date_borrowed char(50),
                       Date_returned char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no)
					   );
CREATE TABLE EXHIBITIONS ( Name char(50),
                       Start_date char(50),
                       End_date char(50),
					   PRIMARY KEY (Name)
					   );
CREATE TABLE IN_COLLECTION ( id_no double,
					   Name char(50),
                       FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no),
                       FOREIGN KEY (Name) REFERENCES COLLECTIONS(Name)
                       );
CREATE TABLE ON_DISPLAY ( id_no double,
					   Name char(50),
                       FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no),
                       FOREIGN KEY (Name) REFERENCES EXHIBITIONS(Name)
                       );