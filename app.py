from flask import Flask, render_template, redirect, request

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


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):

    for product in products:

        found = False

        for item in cart:
            if item["id"] == product_id:
                item["qty"] += 1
                found = True

        if product["id"] == product_id and not found:
            cart.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "image": product["image"],
                "qty": 1
            })

    return redirect("/")


@app.route("/increase/<int:index>")
def increase_qty(index):
    cart[index]["qty"] += 1
    return redirect("/cart")


@app.route("/decrease/<int:index>")
def decrease_qty(index):
    if cart[index]["qty"] > 1:
        cart[index]["qty"] -= 1
    return redirect("/cart")


@app.route("/remove/<int:index>")
def remove_item(index):
    cart.pop(index)
    return redirect("/cart")


@app.route("/cart")
def view_cart():

    total = sum(item["price"] * item["qty"] for item in cart)

    return render_template("cart.html", cart=cart, total=total)


@app.route("/checkout")
def checkout():

    total = sum(item["price"] * item["qty"] for item in cart)

    return render_template("checkout.html", total=total)


if __name__ == "__main__":
    app.run(debug=True)