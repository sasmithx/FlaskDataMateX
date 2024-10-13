create database if not exists FlaskDataMateX;

use FlaskDataMateX;

CREATE TABLE customers (
    customerID VARCHAR(10) PRIMARY KEY,
    customerName VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL
);


CREATE TABLE items (
    itemID VARCHAR(10) PRIMARY KEY,
    itemName VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);


CREATE TABLE transactions (
    transactionID INT AUTO_INCREMENT PRIMARY KEY,
    customerID VARCHAR(10),
    itemID VARCHAR(10),
    quantity INT NOT NULL,
    transactionDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) AS (quantity * price) VIRTUAL,
    FOREIGN KEY (customerID) REFERENCES customers(customerID),
    FOREIGN KEY (itemID) REFERENCES items(itemID)
);


