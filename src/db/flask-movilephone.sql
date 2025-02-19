DROP DATABASES IF EXISTS flask_contacts;

CREATE DATABASES flask_contacts;

CREATE TABLE users{
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50) UNIQUE,
    password VARCHAR(255),  
    fullname VARCHAR(35)
}

CREATE TABLE contacts {
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(35),
    number VARCHAR(9),
    user_id INT UNSIGNED,
    FOREIGN KEY (user_id) REFERENCES user(id)
}