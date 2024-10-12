from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from lk.sasax.FlaskDataMateX.config.config import get_db_connection

item_bp = Blueprint('item', __name__)

db = get_db_connection()
cursor = db.cursor()

@item_bp.route('/add', methods=['POST'])
@jwt_required()
def add_item():
    data = request.get_json()
    sql = "INSERT INTO items (itemID, itemName, price) VALUES (%s, %s, %s)"
    values = (data['itemID'], data['itemName'], data['price'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Item saved successfully!"})

@item_bp.route('/update', methods=['PUT'])
@jwt_required()
def update_item():
    data = request.get_json()
    sql = "UPDATE items SET itemName=%s, price=%s WHERE itemID=%s"
    values = (data['itemName'], data['price'], data['itemID'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Item updated successfully!"})

@item_bp.route('/delete/<itemID>', methods=['DELETE'])
@jwt_required()
def delete_item(itemID):
    sql = "DELETE FROM items WHERE itemID=%s"
    cursor.execute(sql, (itemID,))
    db.commit()
    return jsonify({"message": "Item deleted successfully!"})
