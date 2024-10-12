from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token

from customers import customer_bp
from items import item_bp
from transactions import transaction_bp

app = Flask(__name__)
CORS(app)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(customer_bp, url_prefix='/customers')
app.register_blueprint(item_bp, url_prefix='/items')
app.register_blueprint(transaction_bp, url_prefix='/transactions')


# Login route for authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')


    if username == 'admin' and password == '1234':
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200
    else:
        return {"msg": "Invalid credentials"}, 401


if __name__ == "__main__":
    app.run(debug=True)
