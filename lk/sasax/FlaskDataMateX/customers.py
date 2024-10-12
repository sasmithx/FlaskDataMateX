from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from lk.sasax.FlaskDataMateX.config.config import get_db_connection

customer_bp = Blueprint('customer', __name__)

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Sas@1234",
#     database="FlaskDataMateX"
# )
# cursor = db.cursor()

# Get database connection from config.py
db = get_db_connection()
cursor = db.cursor()

@customer_bp.route('/add', methods=['POST'])
@jwt_required()
def add_customer():
    data = request.get_json()
    sql = "INSERT INTO customers (customerID, customerName, email, phone) VALUES (%s, %s, %s, %s)"
    values = (data['customerID'], data['customerName'], data['email'], data['phone'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Customer saved successfully!"})

@customer_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_customer():
    data = request.get_json()
    sql = "UPDATE customers SET customerName=%s, email=%s, phone=%s WHERE customerID=%s"
    values = (data['customerName'], data['email'], data['phone'], data['customerID'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Customer updated successfully!"})

@customer_bp.route('/delete/<customerID>', methods=['DELETE'])
@jwt_required()
def delete_customer(customerID):
    sql = "DELETE FROM customers WHERE customerID=%s"
    cursor.execute(sql, (customerID,))
    db.commit()
    return jsonify({"message": "Customer deleted successfully!"})
