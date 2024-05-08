import mysql.connector

# Connect to the newly created database
mydb = mysql.connector.connect(
    host="localhost",
    user="devmello",
    password="Pranav2019",
)

# Create a database named "Test Database" if it doesn't exist
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS `Test Database`")

# Switch to the newly created database
mycursor.execute("USE `Test Database`")

mycursor.execute("CREATE TABLE IF NOT EXISTS Users ("
                 "Id INT AUTO_INCREMENT PRIMARY KEY,"
                 "name VARCHAR(255) NOT NULL,"
                 "address VARCHAR(255),"
                 "email VARCHAR(255) UNIQUE,"
                 "password VARCHAR(64) NOT NULL,"
                 "cookie VARCHAR(36))"
                 )

# Create Products table
mycursor.execute("CREATE TABLE IF NOT EXISTS Products ("
                 "ID INT AUTO_INCREMENT PRIMARY KEY,"
                 "name VARCHAR(255) NOT NULL,"
                 "description TEXT,"
                 "image_path VARCHAR(255),"
                 "user_id INT,"
                 "price DECIMAL(10, 2),"
                 "FOREIGN KEY (user_id) REFERENCES Users(Id))"
                 )

# Create Cart table
mycursor.execute("CREATE TABLE IF NOT EXISTS Cart ("
                 "Id INT AUTO_INCREMENT PRIMARY KEY,"
                 "UserID INT,"
                 "Products_id INT,"
                 "FOREIGN KEY (UserID) REFERENCES Users(Id),"
                 "FOREIGN KEY (Products_id) REFERENCES Products(ID))"
                 )

# Create Transactions table
mycursor.execute("CREATE TABLE IF NOT EXISTS Transactions ("
                 "ID INT AUTO_INCREMENT PRIMARY KEY,"
                 "User_id INT,"
                 "Address VARCHAR(255),"
                 "Total DECIMAL(10, 2),"
                 "Receipt_ID VARCHAR(8),"
                 "FOREIGN KEY (User_id) REFERENCES Users(Id))"
                 )

# Commit changes and close connection
mydb.commit()
mydb.close()

print("Database created successfully with the same schema as the Flask application.")