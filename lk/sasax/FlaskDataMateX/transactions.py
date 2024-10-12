from flask import Blueprint, request, jsonify

from lk.sasax.FlaskDataMateX.config.config import get_db_connection

transaction_bp = Blueprint('transaction', __name__)

db = get_db_connection()
cursor = db.cursor()

@transaction_bp.route('/add', methods=['POST'])
def add_transaction():
    data = request.get_json()
    sql = "INSERT INTO transactions (transactionID, customerID, itemID, quantity) VALUES (%s, %s, %s, %s)"
    values = (data['transactionID'], data['customerID'], data['itemID'], data['quantity'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Transaction saved successfully!"})

@transaction_bp.route('/update', methods=['PUT'])
def update_transaction():
    data = request.get_json()
    sql = "UPDATE transactions SET customerID=%s, itemID=%s, quantity=%s WHERE transactionID=%s"
    values = (data['customerID'], data['itemID'], data['quantity'], data['transactionID'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Transaction updated successfully!"})

@transaction_bp.route('/delete/<transactionID>', methods=['DELETE'])
def delete_transaction(transactionID):
    sql = "DELETE FROM transactions WHERE transactionID=%s"
    cursor.execute(sql, (transactionID,))
    db.commit()
    return jsonify({"message": "Transaction deleted successfully!"})
