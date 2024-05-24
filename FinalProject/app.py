import hashlib
import os
import uuid
from decimal import Decimal

from flask import Flask, render_template, request, jsonify, make_response, redirect, send_file, send_from_directory
import mysql.connector
from werkzeug.security import check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mydb = mysql.connector.connect(
    host="localhost",
    user="devmello",
    password="password",
    database="Test Database"
)

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/order',methods=['POST'])
def order():
    # totalAmount = request.json.get('totalAmount')
    paymentType= request.json.get('cash')

    if paymentType:
        paymentType = "Cash"
    else:
        paymentType = "Card"

    email = request.cookies.get('email')
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE cookie = %s", (email,))
    user = cursor.fetchone()
    
    product_details = ""
    if user:        
        cursor.execute("SELECT * FROM Cart WHERE UserID = %s", (user['Id'],))
        cart = cursor.fetchall()
        products = []
        for item in cart:
            cursor.execute("SELECT * FROM Products WHERE ID = %s", (item['Products_id'],))
            product = cursor.fetchone()
            products.append((product, item['Id']))  

        print(products)
        total_price = sum(product[0]['price'] for product in products)
        shipping_cost = 20
        tax = 0.09 * (float(total_price) + float(shipping_cost))
        total = float(total_price) + float(shipping_cost) + float(tax)
        total = round(total, 2)
        print("Total price:", total)

        for product in products:
            product_details += str(product[0]["ID"]) + ","
        product_details = product_details[:-1]

        cursor.execute("INSERT INTO Orders (userId, details, paymentType, totalAmount, date) VALUES (%s, %s, %s, %s, NOW())",
                       (user['Id'], product_details, paymentType, total))

        mydb.commit()
        print("Order Inserted - success")
        # delete items from cart
        cursor.execute("DELETE FROM Cart WHERE UserID = %s", (user['Id'],))
        mydb.commit()
        cursor.close()
        print("Cart Item Removed - success")



        return jsonify({'total': total}), 201

        # cursor.execute("SELECT * FROM Cart WHERE UserID = %s", (userId,))
        # cartDetails = cursor.fetchall()
        # if cartDetails:
        #     print("Cart details")
        #     for product in cartDetails:
        #         product_details += str(product["Products_id"]) + ","
        #         total_amount += Decimal(product["price"])  # Add product price to total amount

        #     product_details = product_details[:-1]
        #     print("Total price:", total_amount)
        #     # #productdetails = "1,2,3,4,4,1"
        #     # cursor.execute("INSERT INTO ORDERS (userId,productDetails,paymentType,totalAmount) VALUES (%s, %s, %s, %s)",(userId,productDetails,paymentType,totalAmount))
                                                                                                                                     
        #     # mydb.commit()
        #     # print("Order Inserted - success")

        #     # #DELETE ITEM FROM CART
        #     # cursor.execute("DELETE FROM CART WHERE UserID = %s", (userId,))
        #     # mydb.commit()       
        #     # cursor.close() 

        #     # print("Cart Item Removed - success")           
        #     return jsonify({'message': 'Order Placed successfully'}), 201

    else:
        return jsonify({'error': 'Order not Placed'}), 404

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()


@app.route('/')
def hello_world():  
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/passlogin', methods=['POST'])
def passlogin():
    email = request.json.get('email')
    password = request.json.get('password')

    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and (hash_data(password) == user['password']):
        # Generate a unique cookie
        cookie = str(uuid.uuid4())

        # Update the cookie in the database
        cursor.execute("UPDATE Users SET cookie = %s WHERE email = %s", (cookie, email))
        mydb.commit()
        print('Logged in successfully')
        # Set the cookie in the user's browser and redirect to the main page
        resp = make_response(redirect('/'))
        resp.set_cookie('email', cookie)
        return resp
    else:
        print('Invalid email or password')
        return jsonify({'error': 'Invalid email or password'}), 401


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(redirect('/login'))
    resp.set_cookie('email', '', expires=0)
    return resp


@app.route('/product', methods=['GET'])
def product():
    product_id = request.args.get('id')
    if product_id is None:
        return "Product id is required", 400

    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Products WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    print(product)
    if product is None:
        return "Product not found", 404

    return render_template("product.html", product=product, productCount=productCount(request.cookies.get('email')))


@app.route('/passregister', methods=['POST'])
def passregister():
    name = request.json.get('name')
    address = request.json.get('address')
    email = request.json.get('email')
    password = request.json.get('password')

    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE email = %s", (email,))
    user = cursor.fetchone()
    if user:
        return jsonify({'error': 'User with this email already exists'}), 400
    else:
        cursor.execute("INSERT INTO Users (name, address, email, password) VALUES (%s, %s, %s, %s)",
                       (name, address, email, hash_data(password)))
        mydb.commit()
        return jsonify({'message': 'User registered successfully'}), 201


@app.route('/cartCount', methods=['GET'])
def cartCount():
    email = request.cookies.get('email')
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE cookie = %s", (email,))
    user = cursor.fetchone()
    if user:
        cursor.execute("SELECT * FROM Cart WHERE UserID = %s", (user['Id'],))
        cart = cursor.fetchall()
        return jsonify({'count': len(cart)})
    else:
        return jsonify({'count': 0})


@app.route('/addToCart', methods=['POST'])
def addToCart():
    email = request.cookies.get('email')
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE cookie = %s", (email,))
    user = cursor.fetchone()
    if user:
        product_id = request.json.get('id')
        cursor.execute("SELECT * FROM Products WHERE ID = %s", (product_id,))
        product = cursor.fetchone()
        if product:
            cursor.execute("INSERT INTO Cart (UserID, Products_id) VALUES (%s, %s)", (user['Id'], product_id))
            mydb.commit()
            return jsonify({'message': 'Product added to cart successfully'}), 201
        else:
            return jsonify({'error': 'Product not found'}), 404
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/removeFromCart', methods=['POST'])
def removeFromCart():
    email = request.cookies.get('email')
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE cookie = %s", (email,))
    user = cursor.fetchone()

    if user:
        product_id = request.json.get('id')
        cursor.execute("SELECT * FROM Cart WHERE UserID = %s AND Id = %s", (user['Id'], product_id))
        product = cursor.fetchone()
        if product:
            cursor.execute("DELETE FROM Cart WHERE UserID = %s AND Id = %s", (user['Id'], product_id))
            mydb.commit()
            return jsonify({'message': 'Product removed from cart successfully'}), 201
        else:
            return jsonify({'error': 'Product not found'}), 404
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/cart', methods=['GET'])
def cart():
    email = request.cookies.get('email')
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE cookie = %s", (email,))
    user = cursor.fetchone()
    if user:
        cursor.execute("SELECT * FROM Cart WHERE UserID = %s", (user['Id'],))
        cart = cursor.fetchall()
        products = []
        for item in cart:
            cursor.execute("SELECT * FROM Products WHERE ID = %s", (item['Products_id'],))
            product = cursor.fetchone()
            products.append((product, item['Id']))  
        product_count = len(products)
        print(products)
        total_price = sum(product[0]['price'] for product in products)
        shipping_cost = 20
        tax = 0.09 * (float(total_price) + float(shipping_cost))
        total = float(total_price) + float(shipping_cost) + float(tax)
        return render_template("cart.html", products=products, total_price=total_price, shipping=shipping_cost, tax=tax,
                               total=total, product_count=product_count)
    else:
        return redirect('/login')


@app.route('/products')
def products():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    return render_template("products.html", products=all_products,
                           productCount=productCount(request.cookies.get('email')))


@app.route('/images/<path:filename>')
def image(filename):
    return send_from_directory('images', filename)


def productCount(cookie):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE cookie = %s", (cookie,))
    user = cursor.fetchone()
    if user:
        cursor.execute("SELECT * FROM Cart WHERE UserID = %s", (user['Id'],))
        cart = cursor.fetchall()
        return len(cart)
    else:
        return 0


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        # Check if the file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected for uploading'}), 400

        # Save the uploaded file to the UPLOAD_FOLDER
        filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
        # check if the filename already exists
        if os.path.exists(os.path.join(UPLOAD_FOLDER, filename)):
            return jsonify({'error': 'File already exists'}), 400
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        if os.path.getsize(os.path.join(UPLOAD_FOLDER, filename)) > 5 * 1024 * 1024:  # 5MB limit
            os.remove(os.path.join(UPLOAD_FOLDER, filename)) 
            return jsonify({'error': 'File size exceeds the limit (5MB)'}), 400

        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        cookie = request.cookies.get('email')

        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE cookie = %s", (cookie,))
        user = cursor.fetchone()
        if user:
            pass
        else:
            os.remove(os.path.join(UPLOAD_FOLDER, filename))  
            return jsonify({'error': 'User not found'}), 404
        user_id = user['Id']


        cursor = mydb.cursor()
        cursor.execute(
            "INSERT INTO Products (name, description, image_path, user_id, price) VALUES (%s, %s, %s, %s, %s)",
            (name, description, filename, user_id, price))
        mydb.commit()
        cursor.close()

        return jsonify({'message': 'File uploaded successfully'}), 200
    else:
        return render_template('upload.html')


@app.route('/get_image/<product_id>')
def get_image(product_id):
    cursor = None
    try:
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Products WHERE ID = %s", (product_id,))
        product = cursor.fetchone()
        if product is None:
            return "Product not found", 404
        if product['image_path'] is None:
            return "Image not found", 404
        filename = product['image_path']
        print(filename)
        if filename:
            return send_from_directory(UPLOAD_FOLDER, filename)
        else:
            return "Image not found", 404
    except Exception as e:
        print(e)  # Log the error for debugging purposes
        return "Internal Server Error", 500
    finally:
        if cursor:
            cursor.close()

@app.route('/logo')
def logo():
    return send_from_directory(UPLOAD_FOLDER, 'logo.png')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        cookie = request.cookies.get('email')
        if cookie:
            cursor = mydb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Users WHERE cookie = %s", (cookie,))
            user = cursor.fetchone()
            if user:
                return render_template('upload.html', productCount=productCount(cookie))
            else:
                return redirect('/login')
    else:
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        cookie = request.cookies.get('email')

        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users WHERE cookie = %s", (cookie,))
        user = cursor.fetchone()
        if user:
            pass
        else:
            return jsonify({'error': 'User not found'}), 404
        user_id = user['Id']

        cursor = mydb.cursor()
        cursor.execute(
            "INSERT INTO Products (name, description, user_id, price) VALUES (%s, %s, %s, %s)",
            (name, description, user_id, price))
        mydb.commit()
        cursor.close()

        return redirect('/products')
    
@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
