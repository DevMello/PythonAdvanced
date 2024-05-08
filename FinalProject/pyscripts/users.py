import mysql.connector
from faker import Faker
import hashlib
import json

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="devmello",
    password="Pranav2019",
    database="Test Database"
)
# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Create Faker instance
fake = Faker()

# Function to hash data
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# List to store user data before hashing
users_data = []

# Generate and insert random users
for _ in range(10):  # Change the number as needed
    email = fake.email()
    password = fake.password()
    hashed_password = hash_data(password)
    name = fake.name()
    address = fake.address()
    hashed_address = hash_data(address)

    # Save user data before hashing
    user_info = {
        "email": email,
        "password": password,
        "name": name,
        "address": address
    }
    users_data.append(user_info)

    # Insert hashed data into database
    sql = "INSERT INTO Users (Email, Password, Name, Address) VALUES (%s, %s, %s, %s)"
    val = (email, hashed_password, name, hashed_address)
    mycursor.execute(sql, val)

    mydb.commit()

print("Random users generated and inserted successfully!")

# Close the database connection
mydb.close()

# Save user data to a JSON file
with open('user_data.json', 'w') as f:
    json.dump(users_data, f)

print("User data saved to user_data.json file.")