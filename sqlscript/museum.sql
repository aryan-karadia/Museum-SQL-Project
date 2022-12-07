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
VALUES (6, 'Brazillian', 'Christ the Redeemer',	'Modern' ,'Jesus with open arms', 1931)
VALUES (7, 'French', 'Statue of Liberty', 'Modern', 'Torch in her raised right hand', 1886)
VALUES (8, 'Russian', 'Mother Russia Statue', 'Modern', 'High statue of a winged female', 1967)
VALUES (9,'Chinese','Spring Temple Buddha','Modern','Statue showing Vairocana Buddha',2007)
VALUES (10,'Indian','Statue of Unity','Modern','Statue of Indian statesman',2013)
VALUES (11,'Italian', 'The Statue David', 'Renaissance', 'Marble sculpture of naked man',1504)
VALUES (12,'Italian', 'Ecstasy of Saint Teresa', 'Renaissance','Nun in religious ecstasy',1652)
VALUES (13, 'French', 'The Thinker', 'Renaissance', 'A man sitting and thinking',1904)
VALUES (14,'Italian', 'Manekken Pis', 'Renaissance', 'A naked infant',1619)
VALUES (15, 'Italian', 'Pieta', 'Renaissance', 'Mary thinking of her dead son',1499)
VALUES (16, 'French', 'Puddle', 'Modern', 'Man jumping over puddle',1932)
VALUES (17, 'American', 'Lunch atop a skyscraper', 'Modern', 'Workers eating lunch on a singular beam',1932)
VALUES (18, 'American','V-J Day in Times Square', 'Modern', 'uniformed man kissing a woman', 1945)
VALUES (19, 'Vietnamese','The Burning Monk', 'Modern','Protesting buddhist monk ablaze',1963)
VALUES (20, 'Vietnamese', 'Napalm Girl', 'Modern', 'An unclothed girl sobbing',1972)

INSERT INTO ARTIST (id_no, Name, Description, Date_born, Date_died, Country_of_origin, Epoch, Main_style)
VALUES (1, 'Leonardo Da Vinci', 'Mona Lisa',1452,1519,Italy,'Renaissance','Renaissance')
VALUES (2,'Leonardo Da Vinci', 'The Last Supper', 1452, 1519, 'Italy', 'Renaissance', 'Renaissance')
VALUES (3,'Vincent Van Gogh','The Starry Night',1853,1890, 'Netherlands','Modern', 'Post-Impressionism')
VALUES (4, 'Edvard Munch', 'Ecstasy of Saint Teresa', 1863, 1944, 'Norway', 'Modern', 'Post-Impressionism')
VALUES (5, 'Maqbool Fida Hussain', 'Horses', '1915', '2011', 'India', 'Modern', 'Cubism')
VALUES (6, 'Paul Landowski', 'Christ the Redeemer', 1875, 1961, 'France','Modern', 'Art Nouveau')
VALUES (7, 'Auguste Bartholdi', 'Statue of Liberty', 1834, 1904, 'France', 'Modern', 'Modern')
VALUES (8, 'Yevgeny Vuchetich', 'Mother Russia Statue' , 1908, 1974, 'Ukraine', 'Modern', 'Modern')
VALUES (9, 'Hai Tong', 'Spring Temple Buddha', 720, 760, 'China', 'Ancient', 'Ancient Chinese')
VALUES (10, 'Ram Suttar', 'Statue of Unity', '1925', ,'India', 'Modern', 'Modern')
VALUES (11, 'Michelangelo', 'The Statue David', 1475, 1564, 'Italy', 'Renaissance', 'Renaissance')
VALUES (12, 'Gian Lorenzo Bernini', 'Ecstasy of Saint Teresa', 1598, 1680, 'Italy', 'Renaissance', 'Renaissance')
VALUES (13, 'Auguste Rodin', 'The Thinker', 1840, 1917, 'France', 'Modern', 'Expressionist Human')
VALUES (14, 'Jerome Duquesnoy', 'Manekken Pis', 1602, 1654, 'Belgium' , 'Renaissance', 'Renaissance')
VALUES (15, 'Michelangelo', 'Pieta', 1475, 1564, 'Italy', 'Renaissance', 'Renaissance')
VALUES (16, 'Henri Cartier-Bresson', 'Puddle', '1908', 2004, 'French', 'Modern', 'Modern')
VALUES (17, 'Charles Clyde Ebbets', 'Lunch atop a skyscraper',1905,1978, 'American', 'Modern','Modern')
VALUES (18, 'Alfred Eisenstaedt', 'V-J Day in Times Square', 1898, 1995, 'Polish', 'Modern', 'Modern')
VALUES (19, 'Malcome Brown', 'The Burning Monk', 1931, 2012, 'American', 'Modern', 'Modern')
VALUES (20, 'Nick Ut', 'Napalm Girl', 1951, ,'American', 'Modern', 'Modern')


INSERT INTO PAINTING (id_no, paint_type, drawn_on, Style)
VALUES (1, 'Portrait', 1503, 'Renaissance')
VALUES (2, 'Mural', 1496, 'Renaissance')
VALUES (3, 'Landscape', 1889, 'Modern')
VALUES (4, 'Abstract', 1893, 'Modern')
VALUES (5, 'Animal', 1960, 'Modern')

INSERT INTO SCULPTURE (id_no, Material, Height, Weight, Style)
VALUES (6, 'Concrete/Soapstone', 30, 635)
VALUES (7, 'Copper/Steel', 93, 204)
VALUES (8, 'Concrete/Metal', 85, 8000)
VALUES (9, 'Copper', 128, 1000)
VALUES (10, 'Concrete/Bronze', 182, 67000)

INSERT INTO STATUE (id_no, Material, Height, Weight, Style)
VALUES (11, 'Marble', 5.17, 6, 'Renaissance')
VALUES (12, 'Marble', 3.5, 4.2, 'Renaissance')
VALUES (13, 'Marble', 1.89, 5.4, 'Renaissance')
VALUES (14, 'Marble', 10, 1, 'Renaissance')
VALUES (15, 'Marble', 1.74, 6.1, 'Renaissance')

INSERT INTO OTHER (id_no, Type, Style)
VALUES (16, 'Photo', 'Humanist')
VALUES (17, 'Photo', 'Humanist')
VALUES (18, 'Photo', 'Humanist')
VALUES (19, 'Photo', 'Photojournalism')
VALUES (20, 'Photo', 'Photojournalism')

INSERT INTO COLLECTIONS (Name, Phone, Contact_person, Street_address, City, Country, Postal_code, Type, Description)
VALUES ('Louvre', 140205050, 'Jean Hollande', 'Musée du Louvre', 'Paris', 'France', 75001, 'Renaissance', 'Renaissance art')
VALUES ('The Museum of Modern Art', 2127089400, 'Adam McCormick', '11 W 53rd St', 'New York City', 'USA', 10019, 'Modern', 'Modern Art')
VALUES ('National Museum of Oslo', 21982000, 'Erik Magnusson', 'Brynjulf Bulls plass 3', 'Oslo', 'Norway', 250)
VALUES ('Accademia Gallery', 0550987100, 'Antonio Basillieni', 'Via Ricasoli, 58/60', 'Firenze Fi', 'Italy', 50129)
VALUES ('Musée Rodin', 144186110, 'Francois Dubois', '77 Rue de Varenne', 'Paris', 'France', 75007)
VALUES ('Brussels City Museum', 22794350, 'Michel Peeters', 'Grote Markt van', 'Brussels', 'Belgium', 1000)


INSERT INTO PERMANENT_COLLECTION (id_no, Status, Cost, Date_acquired)
VALUES (1, 'On Display', 870000000, 1804)
VALUES (3, 'On Display', 100000000, 1941)
VALUES (4, 'On Display', 120000000, 1910)
VALUES (11, 'On Display', 200000000, 1910)
VALUES (13, 'In Collection', 16000000, 1922)
VALUES (14, 'stored', 5000000, 1966)


INSERT INTO BORROWED (id_no, Collection_origin, Date_borrowed, Date_returned)


INSERT INTO EXHIBITIONS (Name, Start_date, End_date)
VALUES ('The Tudors', '03/12/2021', '03/02/2022')

INSERT INTO IN_COLLECTION (id_no, Name)
VALUES (13, 'The Thinker')

INSERT INTO ON_DISPLAY (id_no, Name)
VALUES (1, 'Mona Lisa')
VALUES (3, 'The Starry Night')
VALUES (4, 'The Scream')
VALUES (11, 'The Statue David')