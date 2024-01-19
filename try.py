import mysql.connector
def display_columns(database_name, table_name):
    try:
        # Replace "new_password" with your actual MySQL password
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="new_password",
            database=database_name
        )

        # Creating a cursor object to interact with the database
        cursor = mydb.cursor()

        # Query to retrieve column names and properties from information schema
        query = """
        SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, CHARACTER_SET_NAME, COLLATION_NAME
        FROM information_schema.COLUMNS
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s
        """
        cursor.execute(query, (database_name, table_name))

        # Fetch all the columns and their properties
        columns_info = cursor.fetchall()

        # Display the column names and properties
        for column_info in columns_info:
            column_name = column_info[0]
            column_type = column_info[1]
            is_nullable = column_info[2]
            column_default = column_info[3]
            character_set = column_info[4]
            collation = column_info[5]

            print("Column Name: {}".format(column_name))
            print("    Type: {}".format(column_type))
            print("    Nullable: {}".format(is_nullable))
            print("    Default Value: {}".format(column_default))
            print("    Character Set: {}".format(character_set))
            print("    Collation: {}".format(collation))
            print("\n")

        # Don't forget to close the cursor and connection
        cursor.close()
        mydb.close()

    except Exception as e:
        print("Error connecting to the database:", str(e))


def insert_data(database_name, table_name, data):
    try:
        # Replace "new_password" with your actual MySQL password
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="new_password",
            database=database_name
        )

        # Creating a cursor object to interact with the database
        cursor = mydb.cursor()

        # Prepare the SQL query for data insertion
        query = "INSERT INTO {} ({}) VALUES ({})".format(
            table_name,
            ', '.join(data.keys()),
            ', '.join(["%s"] * len(data))
        )

        # Execute the query with the provided data
        cursor.execute(query, tuple(data.values()))

        # Commit the changes to the database
        mydb.commit()

        print("Data inserted successfully.")

        # Don't forget to close the cursor and connection
        cursor.close()
        mydb.close()

    except Exception as e:
        print("Error inserting data:", str(e))


# Specify the database name and table name you want to display columns for
database_name = "Attendance_System"
table_name = "student_info"  # Replace with your actual table name

# Call the function to display columns in the specified table
display_columns(database_name, table_name)
data_to_insert = {
    'Stream': 'Engineering',
    'Grade': 10,
    'Section': 'A',
    'Year': '2024',
    'Student_id': 1,
    'Name': 'John Doe',
    'Roll_No': 101,
    'Gender': 'Male',
    'Email': 'john.doe@example.com',
    'Phone': '123-456-7890',
    'DOB': '2000-01-01',
    'Photo_Sample': 'Yes'
}

# Call the function to insert data into the specified table
insert_data(database_name, table_name, data_to_insert)