/* Not an actual schema as instead these lines will be pulled in and run at start time.
   In an actual project I would design this better but the solution to having a schema 
   run on start up is not worth the effort when this will do nicely for this project */

DROP TABLE IF EXISTS blog;
CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255));

DROP TABLE IF EXISTS Routes;
CREATE TABLE Routes (id INT PRIMARY KEY, long_name VARCHAR(255));
