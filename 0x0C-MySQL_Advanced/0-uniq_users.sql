-- first task mysql advanced
-- yep
CREATE DATABASE IF NOT EXISTS holberton;
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    PRIMARY KEY (`id`)
);