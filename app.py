from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load products from JSON file
def load_products():
    with open("products.json") as f:
        return json.load(f)

@app.route("/")
def index():
    items = load_products()
    return render_template("index.html", products=items)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    items = load_products()
    return render_template("products.html", products=items)

@app.route("/api/products")
def api_products():
    return jsonify(load_products())

if __name__ == "__main__":
    app.run(debug=True)
