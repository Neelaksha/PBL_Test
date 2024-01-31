from flask import Flask, render_template, request, redirect, url_for
from flask import jsonify
app = Flask(__name__)

# Sample dessert data (replace with your actual data)
desserts = [
    {"id": 1, "name": "Chocolate Cake", "price": 10},
    {"id": 2, "name": "Cheesecake", "price": 12},
    {"id": 3, "name": "Apple Pie", "price": 8},
]

# Sample user data (replace with your actual data)
users = {
    "admin": "admin123",
    "user1": "password1",
    "user2": "password2",
}

orders = []

@app.route("/")
def index():
    return render_template("index.html", desserts=desserts)

@app.route("/order", methods=["POST"])


@app.route("/order", methods=["POST"])
def order():
    dessert_id = int(request.form["dessert_id"])
    dessert_name = [dessert["name"] for dessert in desserts if dessert["id"] == dessert_id][0]
    orders.append({"dessert_id": dessert_id, "dessert_name": dessert_name})
    return jsonify({"message": "Order placed successfully!"})


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)
