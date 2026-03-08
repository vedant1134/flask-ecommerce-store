from flask import Flask, render_template, request, redirect

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1000, "image": "laptop.jpg"},
    {"id": 2, "name": "Phone", "price": 500, "image": "phone.jpg"},
    {"id": 3, "name": "Headphones", "price": 100, "image": "headphones.jpg"}
]

cart = []

@app.route("/")
def home():
    search = request.args.get("search")

    if search:
        filtered = [p for p in products if search.lower() in p["name"].lower()]
    else:
        filtered = products

    return render_template("index.html", products=filtered)

@app.route("/cart")
def cart_page():
    return render_template("cart.html", cart=cart)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    for product in products:
        if product["id"] == product_id:
            cart.append(product)
            break
    return redirect("/cart")