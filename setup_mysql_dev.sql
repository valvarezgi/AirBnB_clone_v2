-- Prepares a MySQL server for the project
-- Creates data base if doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user if doesn't exist
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privileges to the user hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
-- GRant SELECT privileges
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
