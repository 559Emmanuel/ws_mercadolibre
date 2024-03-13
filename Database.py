import mysql.connector


# Database connection details
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""

# Create connection
try:
    connection = mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD
    )
    print("Connected to MySQL successfully!")
except mysql.connector.Error as err:
    print(f"Error connecting to MySQL: {err}")
    exit(1)

# Create database
cursor = connection.cursor()
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS ML_database;")
    print("Database created successfully!")
except mysql.connector.Error as err:
    print(f"Error creating database: {err}")
    exit(1)

# Use the created database
cursor.execute("USE ML_database;")

# Create table
TABLE_NAME = "MercadoLibre"
COLUMNS = (
    "Name PRIMARY KEY VARCHAR(255) NOT NULL",
    "Price INT NOT NULL",
    "Delivery_Fee INT NOT NULL",
    "Product_description VARCHAR(255) NOT NULL",
    "Seller_Name VARCHAR(255) NOT NULL",
)
try:
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ({','.join(COLUMNS)});")
    print("Table created successfully!")
except mysql.connector.Error as err:
    print(f"Error creating table: {err}")
    exit(1)

# Insert data
DATA = 
try:
    cursor.executemany(f"INSERT INTO {TABLE_NAME} (Name, Price, Delivery_Fee, Product_description, Seller_Name) VALUES (%s, %s, %s; %s; %s)", DATA)
    connection.commit()
    print("Data inserted successfully!")
except mysql.connector.Error as err:
    print(f"Error inserting data: {err}")
    exit(1)

# Query data
try:
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    results = cursor.fetchall()
    print("Table data:")
    for row in results:
        print(f"Name: {row[0]}, Price: {row[1]}, Delivery_Fee: {row[2]}, Product_description: {row[3]}, Seller_Name: {row[4]}")
except mysql.connector.Error as err:
    print(f"Error querying data: {err}")
    exit(1)


# Close connection
cursor.close()
connection.close()
print("Disconnected from MySQL successfully.")
