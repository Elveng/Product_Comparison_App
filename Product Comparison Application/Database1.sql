CREATE DATABASE  IF NOT EXISTS `SEproject`;
USE `SEproject`;




CREATE TABLE `Customers` (
  CustomerID Int,
  PRIMARY KEY (CustomerID),
  username text(16),
  Password text(16)
);


);

CREATE TABLE `Products` (
  ProductID int,
  PRIMARY KEY (ProductID),
  TypeName text,
  ProductName text,
  Price int
);
CREATE TABLE `Favourite` (
  ProductID int,
  PRIMARY KEY (ProductID),
  TypeName text,
  ProductName text,
  Price int
);
-- Inserting a product with ID 1, TypeName 'Electronics', ProductName 'Smartphone', and Price 499.99
INSERT INTO Products (ProductID, TypeName, ProductName, Price) VALUES (1, 'Electronics', 'Smartphone', 499.99);

-- Inserting a product with ID 2, TypeName 'Clothing', ProductName 'T-Shirt', and Price 19.99
INSERT INTO Products (ProductID, TypeName, ProductName, Price) VALUES (2, 'Clothing', 'T-Shirt', 19.99);

-- Inserting a product with ID 3, TypeName 'Home Appliances', ProductName 'Coffee Maker', and Price 89.99
INSERT INTO Products (ProductID, TypeName, ProductName, Price) VALUES (3, 'Home Appliances', 'Coffee Maker', 89.99);




