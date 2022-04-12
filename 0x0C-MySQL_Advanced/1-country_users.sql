-- tasks mysql advanced
-- second task
CREATE DATABASE IF NOT EXISTS holberton;
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country varchar(2) DEFAULT 'US',
    PRIMARY KEY (`id`)
);