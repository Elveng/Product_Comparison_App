import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import mysql.connector

# Connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Berk2002",
            database="SEproject"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
        return None




class ProductComparisonApp(QMainWindow):
    def __init__(self):
    
        super(ProductComparisonApp, self).__init__()
        uic.loadUi('main.ui', self)  # Load the UI file
        self.show()

        # Connect to the MySQL database
        self.connection = connect_to_database()
        if self.connection is None:
            sys.exit(1)

        
        

        # Connect the buttons to their functions
        #self.pushButton.clicked.connect(self.login)
        #self.pushButton_2.clicked.connect(self.signup)
        self.actionClose.triggered.connect(exit)
        self.refresh_list()
        self.ProductTable.cellClicked.connect(self.select_item)
        self.firstelement.clicked.connect(self.add_to_comparison_button1)
        self.secondelement.clicked.connect(self.add_to_comparison_button2)
        self.favourite_list()
        self.favourite1.clicked.connect(self.favourite_button1)
        self.favourite2.clicked.connect(self.favourite_button2)
        self.Delete.clicked.connect(self.delete_favourite)
        self.FavouriteTable.cellClicked.connect(self.select_item2)

    selected_item = None
    selected_item2 = None

    def refresh_list(self):
        
        # Get the list of products from the database
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Products")
        result = cursor.fetchall()
        

        self.ProductTable.setRowCount(len(result))
        self.ProductTable.setColumnCount(len(result[0]))
        self.ProductTable.setHorizontalHeaderLabels(["Product ID", "Product Name", "Product Price", "Product Description", "Product Image"])
        for i in range(len(result)):
            for j in range(len(result[i])):
                self.ProductTable.setItem(i, j, QTableWidgetItem(str(result[i][j])))
        self.ProductTable.resizeColumnsToContents()
        self.ProductTable.resizeRowsToContents()
    
    def favourite_list(self):
        # Get the list of products from the database
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Favourite")
        result = cursor.fetchall()
       
        if len(result) == 0:
            print("No favourite item") 
        else:
            self.FavouriteTable.setRowCount(len(result))
            self.FavouriteTable.setColumnCount(len(result[0]))
            self.FavouriteTable.setHorizontalHeaderLabels(["Product ID", "Product Name", "Product Price", "Product Description", "Product Image"])
            for i in range(len(result)):
                for j in range(len(result[i])):
                    self.FavouriteTable.setItem(i, j, QTableWidgetItem(str(result[i][j])))
            self.FavouriteTable.resizeColumnsToContents()
            self.FavouriteTable.resizeRowsToContents()

    def select_item(self, row, column):
        # Get the selected item
        self.selected_item = self.ProductTable.item(row, 0)
    def select_item2(self, row, column):
        # Get the selected item
        self.selected_item2 = self.FavouriteTable.item(row, 0)
   
    def add_to_comparison_button1(self):
        if self.selected_item is None:
            print("No item selected")
        else:
            # Get the product ID of the selected item
            product_id = self.selected_item.text()
            
            # Get the product from the products table
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Products WHERE ProductID = %s", (product_id,))
            result = cursor.fetchone()
            
            # Show the product in the comparison table
            if result is not None:
                
                
                self.ComparisonTable1.setRowCount(1)
                self.ComparisonTable1.setColumnCount(len(result))
                self.ComparisonTable1.setHorizontalHeaderLabels(["Product ID", "Product Name", "Product Price", "Product Description", "Product Image"])
                
                for i in range(len(result)):
                   self.ComparisonTable1.setItem(0, i, QTableWidgetItem(str(result[i])))
                self.ComparisonTable1.resizeColumnsToContents()
                self.ComparisonTable1.resizeRowsToContents()
            else:
                print("Product not found")
    
    def add_to_comparison_button2(self):
        if self.selected_item is None:
            print("No item selected")
        else:
            # Get the product ID of the selected item
            product_id = self.selected_item.text()
            
            # Get the product from the products table
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Products WHERE ProductID = %s", (product_id,))
            result = cursor.fetchone()
           
            # Show the product in the comparison table
            if result is not None:
                
                
                self.ComparisonTable2.setRowCount(1)
                self.ComparisonTable2.setColumnCount(len(result))
                self.ComparisonTable2.setHorizontalHeaderLabels(["Product ID", "Product Name", "Product Price", "Product Description", "Product Image"])
                
                for i in range(len(result)):
                   self.ComparisonTable2.setItem(0, i, QTableWidgetItem(str(result[i])))
                self.ComparisonTable2.resizeColumnsToContents()
                self.ComparisonTable2.resizeRowsToContents()
            else:
                print("Product not found")
    def favourite_button1(self):
        
        
            # Get the product ID of the selected item
            values=[]
            for i in range (4): 
                values.append(self.ComparisonTable1.item(0, i).text())  
            
            # Get the product from the products table
            cursor = self.connection.cursor()
            try:
                cursor.execute("INSERT INTO Favourite (ProductID, TypeName, ProductName, Price) VALUES (%s, %s, %s, %s);", (values[0], values[1], values[2], values[3]))
                result = cursor.fetchone()
                self.connection.commit()
            except:
                print("Item already in favourite list")
                

            print(result)
            self.favourite_list()
    def favourite_button2(self):
        
        
            # Get the product ID of the selected item
            values=[]
            for i in range (4): 
                values.append(self.ComparisonTable2.item(0, i).text())  
            
            # Get the product from the products table
            cursor = self.connection.cursor()
            try:
                cursor.execute("INSERT INTO Favourite (ProductID, TypeName, ProductName, Price) VALUES (%s, %s, %s, %s);", (values[0], values[1], values[2], values[3]))
                result = cursor.fetchone()
                self.connection.commit()
            except:
                print("Item already in favourite list")
                
            
            print(result)
            self.favourite_list()
    
    def delete_favourite(self):
        if self.selected_item2 is None:
            print("No item selected")
        else:
            # Get the product ID of the selected item
            product_id = self.selected_item2.text()
            
            # Get the product from the products table
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Favourite WHERE ProductID = %s", (product_id,))
            result = cursor.fetchone()
            self.connection.commit()
           

        self.favourite_list()

           
            
        


    def login(self):
        # Get the username and password from the text boxes
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(username, password)

        # Check if the username and password are correct
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM customers WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        if result is None:
            print("Invalid username or password")
        else:
            print("Login successful")
    
    def signup(self):
        # Get the username and password from the text boxes
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(username, password)

        # Check if the username already exists
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Customers WHERE username = %s", (username,))
        result = cursor.fetchone()
        if result is not None:
            print("Username already exists")
        else:
            # Insert the new user into the database
            cursor.execute("INSERT INTO Customers (username, password) VALUES (%s, %s)", (username, password))
            self.connection.commit()
            print("Signup successful")
    
    def __del__(self):
        self.connection.close() # Close the connection to the database
    


        
   
def main():
    
    app = QApplication([])
    window = ProductComparisonApp()
    app.exec_()

if __name__ == '__main__':
    main()