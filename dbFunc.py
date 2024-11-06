
import mysql.connector

def addUser(dbArg, cursorArg, fields, values):
    try:
        add_user = (f"INSERT INTO users ({fields}) VALUES ({values})")
        cursorArg.execute(add_user)
        dbArg.commit()
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    


def connectToDb(host, user, password, database):
    db = mysql.connector.connect(
    host=host,        # Replace with your database host
    user=user,    # Replace with your MySQL username
    password=password, # Replace with your MySQL password
    database=database  # Replace with your database name
    )
    return db

def returnTable(cursorArg,table):
    cursorArg.execute(f"SELECT * FROM {table}")
    results = cursorArg.fetchall() 
    return results

def createTable(cursorArg, tableName, columns):
    # Construct the SQL query dynamically
    columns_with_constraints = []
    for column in columns:
        # Expecting column as a dictionary with keys: 'name', 'type', 'constraints'
        column_definition = f"{column['name']} {column['type']}"
        if 'constraints' in column:
            column_definition += f" {column['constraints']}"
        columns_with_constraints.append(column_definition)

    # Join all column definitions into a single string
    columns_sql = ", ".join(columns_with_constraints)

    # Create the final SQL statement
    query = f"CREATE TABLE {tableName} ({columns_sql});"
    
    # Execute the query
    cursorArg.execute(query)

def findUser(email,cursor):
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    return cursor.fetchone()
