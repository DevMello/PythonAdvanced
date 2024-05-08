import mysql.connector

# Sample data of products
products_data = [
    {"Name": "Smartphone", "Description": "Latest smartphone with advanced features", "Price": 599.99,
     "Category": "Electronics", "Image": "smartphone.jpg", "User_id": 1},
    {"Name": "Laptop", "Description": "Powerful laptop for work and entertainment", "Price": 999.99,
     "Category": "Electronics", "Image": "laptop.jpg", "User_id": 2},
    {"Name": "Headphones", "Description": "High-quality headphones for immersive audio experience", "Price": 149.99,
     "Category": "Electronics", "Image": "headphones.jpg", "User_id": 3},
    {"Name": "Running Shoes", "Description": "Comfortable running shoes for athletes", "Price": 79.99,
     "Category": "Footwear", "Image": "shoes.jpg", "User_id": 4},
    {"Name": "Watch", "Description": "Stylish watch with elegant design", "Price": 199.99, "Category": "Accessories",
     "Image": "watch.jpg", "User_id": 5},
    {"Name": "Backpack", "Description": "Durable backpack for everyday use", "Price": 49.99, "Category": "Accessories",
     "Image": "backpack.jpg", "User_id": 6},
    {"Name": "Bluetooth Speaker", "Description": "Portable Bluetooth speaker for music lovers", "Price": 129.99,
     "Category": "Electronics", "Image": "speaker.jpg", "User_id": 7},
    {"Name": "Office Chair", "Description": "Ergonomic office chair for improved posture", "Price": 199.99,
     "Category": "Furniture", "Image": "chair.jpg", "User_id": 8},
    {"Name": "Coffee Maker", "Description": "Automatic coffee maker for coffee enthusiasts", "Price": 69.99,
     "Category": "Appliances", "Image": "coffee.jpg", "User_id": 9},
    {"Name": "Television", "Description": "Ultra HD television with vibrant colors", "Price": 799.99,
     "Category": "Electronics", "Image": "tv.jpg", "User_id": 10}
]
# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="devmello",
    password="Pranav2019",
    database="Test Database"
)
# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


# Function to insert product data into the database
def insert_product(product):
    sql = ("INSERT INTO Products (Name, Description, Price, Category, image_path, User_id) VALUES (%s, %s, %s, %s, %s, "
           "%s)")
    val = (product["Name"], product["Description"], product["Price"], product["Category"], product["Image"],
           product["User_id"])
    mycursor.execute(sql, val)
    mydb.commit()


# Insert products into the database
for product in products_data:
    insert_product(product)

print("Product data inserted successfully!")

# Close the database connection
mydb.close()
