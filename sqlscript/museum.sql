DROP DATABASE IF EXISTS MUSEUM;
CREATE DATABASE MUSEUM;
USE MUSEUM;

DROP TABLE IF EXISTS ART_OBJECT;
CREATE TABLE ART_OBJECT( id_no double,
						 Origin char(50),
						 Title char(50),
						 Epoch char(50),
                         Description char(50),
                         Year double,
                         PRIMARY KEY (id_no)
                         );

DROP TABLE IF EXISTS ARTIST;                         
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
                       
DROP TABLE IF EXISTS PAINTING;                       
CREATE TABLE PAINTING( id_no double,
					   paint_type char(50),
					   drawn_on char(50),
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );

DROP TABLE IF EXISTS SCULPTURE;
CREATE TABLE SCULPTURE( id_no double,
					   Material char(50),
					   Height double,
                       Weight double,
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
					
DROP TABLE IF EXISTS STATUE;
CREATE TABLE STATUE  ( id_no double,
					   Material char(50),
					   Height double,
                       Weight double,
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
                       
DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER   ( id_no double,
					   Type char(50),
					   Style char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT (id_no)
					   );
                       
DROP TABLE IF EXISTS COLLECTIONS;
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
                       
DROP TABLE IF EXISTS PERMANENT_COLLECTION;
CREATE TABLE PERMANENT_COLLECTION   ( id_no double,
					   Status char(50),
					   Cost double,
                       Date_acquired char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no)
					   );
                       
DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED   ( id_no double,
					   Collection_origin char(50),
                       Date_borrowed char(50),
                       Date_returned char(50),
					   FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no)
					   );
                       
DROP TABLE IF EXISTS EXHIBITIONS;
CREATE TABLE EXHIBITIONS ( Name char(50),
                       Start_date char(50),
                       End_date char(50),
					   PRIMARY KEY (Name)
					   );
                       
DROP TABLE IF EXISTS IN_COLLECTION;
CREATE TABLE IN_COLLECTION ( id_no double,
					   Name char(50),
                       FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no),
                       FOREIGN KEY (Name) REFERENCES COLLECTIONS(Name)
                       );
                       
DROP TABLE IF EXISTS ON_DISPLAY;
CREATE TABLE ON_DISPLAY ( id_no double,
					   Name char(50),
                       FOREIGN KEY (id_no) REFERENCES ART_OBJECT(id_no),
                       FOREIGN KEY (Name) REFERENCES EXHIBITIONS(Name)
                       );

INSERT INTO ART_OBJECT (id_no, Origin, Title, Epoch, Description, Year)
VALUES (1, 'Italian', 'Mona Lisa', 'Renaissance', 'Portrait of a Florentine Merchants wife', 1503)
VALUES (2, 'Italian', 'The Last Supper', 'Renaissance', 'Jesus and his followers eating a meal', 1496)
VALUES (3, 'French', 'The Starry Night', 'Modern', 'Depicts a dreamy interpretation', 1889)
VALUES (4, 'Norweigan', 'The Scream', 'Modern', 'It depicts a paniced creature', 1893)
VALUES (5, 'Indian', 'Horses', 'Modern', 'Four horses are shown in tumultous gallop', 1960)

INSERT INTO ARTIST (id_no, Name, Description, Date_born, Date_died, Country_of_origin, Epoch, Main_style)

INSERT INTO PAINTING (id_no, paint_type, drawn_on, Style)

INSERT INTO SCULPTURE (id_no, Material, Height, Weight, Style)

INSERT INTO STATUE (id_no, Material, Height, Weight, Style)

INSERT INTO OTHER (id_no, Type, Style)

INSERT INTO COLLECTIONS (Name, Phone, Contact_person, Street_address, City, Country, Postal_code, Type, Description)

INSERT INTO PERMANENT_COLLECTION (id_no, Status, Cost, Date_acquired)

INSERT INTO BORROWED (id_no, Collection_origin, Date_borrowed, Date_returned)

INSERT INTO EXHIBITIONS (Name, Start_date, End_date)

INSERT INTO IN_COLLECTION (id_no, Name)

INSERT INTO ON_DISPLAY (id_no, Name)
