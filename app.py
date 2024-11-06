from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    # List of products with names and prices
    products = [
        {"name": "Banana", "price": 20},
        {"name": "Apple", "price": 30},
        {"name": "Orange", "price": 25},
    ]
    
    # Context to pass username and other info
    context = {
        "username": "Ezzat",
        "age": 24,
        "height": 5.7,
        "products": products
    }

    return render_template("home.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
