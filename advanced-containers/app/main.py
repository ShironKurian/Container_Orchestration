from flask import Flask, request, jsonify  
import os  
import psycopg2  

app = Flask(__name__)  

# Database connection
DB_HOST = os.getenv("DB_HOST", "db")  
DB_NAME = os.getenv("DB_NAME", "mydatabase")  
DB_USER = os.getenv("DB_USER", "myuser")  
DB_PASS = os.getenv("DB_PASS", "mypassword")  

def get_db_connection():  
    return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)  

# Create User
@app.route('/user', methods=['POST'])  
def create_user():  
    data = request.json  
    conn = get_db_connection()  
    cur = conn.cursor()  
    cur.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id;", (data["first_name"], data["last_name"]))  
    user_id = cur.fetchone()[0]  
    conn.commit()  
    cur.close()  
    conn.close()  
    return jsonify({"id": user_id, "message": "User created successfully"}), 201  

# Get User
@app.route('/user/<int:user_id>', methods=['GET'])  
def get_user(user_id):  
    conn = get_db_connection()  
    cur = conn.cursor()  
    cur.execute("SELECT id, first_name, last_name FROM users WHERE id = %s;", (user_id,))  
    user = cur.fetchone()  
    cur.close()  
    conn.close()  
    if user:  
        return jsonify({"id": user[0], "first_name": user[1], "last_name": user[2]})  
    return jsonify({"message": "User not found"}), 404  

if __name__ == '__main__':  
    app.run(host="0.0.0.0", port=5000)