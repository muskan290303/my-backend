from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to interact with the backend

# PostgreSQL Connection
DATABASE_URL = "postgresql://neondb_owner:npg_DAux0z2UCNSi@ep-ancient-thunder-a8f0n6zi-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
 # Get database URL from environment variables

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Connect to PostgreSQL with SSL
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# Home route
@app.route("/")
def home():
    return "Flask backend is running!"

# Endpoint to submit contact form
@app.route("/contact", methods=["POST"])
def contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    cursor.execute(
        "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message),
    )
    conn.commit()
    return jsonify({"message": "Message received!"}), 201

# Fetch projects from database
@app.route("/projects", methods=["GET"])
def get_projects():
    cursor.execute("SELECT title, img, desc FROM projects")
    projects = cursor.fetchall()
    return jsonify([{"title": p[0], "img": p[1], "desc": p[2]} for p in projects])

if __name__ == "__main__":
    app.run(debug=True)
