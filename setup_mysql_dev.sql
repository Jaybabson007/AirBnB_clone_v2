--A script that prepares a dev MySQL server for the AirBnB clone project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- a new user hbnb_dev (in localhost).
-- the password of hbnb_dev should be set to hbnb_dev_pwd(solution below)
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have all privileges on the database hbnb_dev_db only(solution below)
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have SELECT privilege on the database performance_schema(solution below)
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
