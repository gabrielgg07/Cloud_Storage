from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import dbFunc as dbf
from flask_cors import CORS  # Import CORS


app = Flask(__name__)
CORS(app)
# In-memory database (for demonstration purposes)
users_db = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate input
    if 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing email or password"}), 400

    email = data['email']
    password = data['password']
    
    # Connect to the database
    db = dbf.connectToDb("localhost", "root", "Bulldog0721", "Cloud_Users")
    cursor = db.cursor()

    # Check if the user already exists
    user = dbf.findUser(email, cursor)
    if user:
        cursor.close()  # Close the cursor before returning
        db.close()  # Close the database connection
        return jsonify({"error": "Email already registered"}), 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Prepare the fields and values
    fields = "email, password"
    values = f"'{email}', '{hashed_password}'"

    # Add the user to the database
    if dbf.addUser(db, cursor, fields, values):
        cursor.close()  # Close the cursor after insertion
        db.close()  # Close the connection
        return jsonify({"message": "Account created successfully!"}), 201
    else:
        cursor.close()  # Close the cursor on failure
        db.close()  # Close the connection
        return jsonify({"error": "Failed to create account"}), 500

if __name__ == '__main__':
    app.run(debug=True)

