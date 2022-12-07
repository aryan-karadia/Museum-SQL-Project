USE MUSEUM;

-- 1) Show all tables and explain how they are related to one another (keys, triggers, etc.)
SHOW TABLES;
-- 

-- 2) A basic retrieval query
SELECT Name, Description, Date_born, Date_died
FROM ARTIST
WHERE id_no = 2;

-- 3) A retrieval query with ordered results
SELECT id_no, Name, Description, Date_born, Date_died
FROM ARTIST
ORDER BY id_no ASC;

-- 4) A nested retrieval query
SELECT Status, Cost
FROM PERMANENT_COLLECTION
WHERE id_no IN (SELECT id_no
                FROM ART_OBJECT
                WHERE id_no = 4);

-- 5) A retrieval query using joined tables
SELECT SCULPTURE.id_no, SCULPTURE.Material, SCULPTURE.Height, SCULPTURE.Weight
FROM SCULPTURE
INNER JOIN ART_OBJECT
ON SCULPTURE.id_no = ART_OBJECT.id_no;

-- 6) An update operation with any necessary triggers
DELIMITER $$

CREATE TRIGGER COLLECTION_DISPLAY
AFTER UPDATE
ON IN_COLLECTION FOR EACH ROW
BEGIN
    IF OLD.IN_COLLECTION <> new.IN_COLLECTION THEN
        INSERT INTO ON_DISPLAY (id_no, Name)
        VALUES(old.id_no, old.Name);
    END IF;
END$$

DELIMITER ;

UPDATE IN_COLLECTION 
SET id_no = 5
WHERE id_no = 5;

-- 7) A deletion operation with any necessary triggers
DELIMITER $$
CREATE TRIGGER DELETE_COLLECTION
AFTER DELETE ON ON_DISPLAY FOR EACH ROW
BEGIN
INSERT INTO IN_COLLECTION (id_no, Nme)
VALUES (OLD.id_no, OLD.Name);
END$$
DELIMITER ;

DELETE FROM ON_DISPLAY
WHERE id_no = 5;

