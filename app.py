from flask import Flask, render_template, request
import random

app = Flask(__name__)

dish_names = ["Paneer", "Chicken", "Mutton", "Veg", "Egg", "Fish",
              "Pasta", "Pizza", "Burger", "Noodles", "Rice", "Soup"]

styles = ["Butter Masala", "Korma", "Fry", "Gravy", "Spicy",
          "Tandoori", "Cheese Loaded", "Manchurian", "Classic"]

tastes = ["spicy", "sweet", "savory", "crispy", "creamy", "cheesy"]
cuisines = ["indian", "south indian", "chinese",
            "italian", "mexican", "american"]

# Main Menu (500 dishes)
menu = [
    {
        "name": f"{random.choice(dish_names)} {random.choice(styles)}",
        "price": random.randint(100, 500),
        "taste": random.choice(tastes),
        "cuisine": random.choice(cuisines)
    }
    for _ in range(500)
]

# Chef Special (premium items)
chef_special = [
    {"name": f"Chef Special {random.choice(dish_names)} Deluxe", "price": random.randint(300, 600)}
    for _ in range(20)
]

# Combos
combos = [
    {"name": f"{random.choice(dish_names)} Combo Meal", "price": random.randint(200, 400)}
    for _ in range(20)
]

# Offers
offers = [
    {"name": f"{random.choice(dish_names)} Offer Deal", "price": random.randint(100, 250)}
    for _ in range(20)
]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/menu')
def show_menu():
    return render_template('menu.html', menu=menu[:120])


@app.route('/chef')
def chef():
    return render_template('simple_list.html', title="👨‍🍳 Chef's Special", data=chef_special)


@app.route('/combos')
def combo():
    return render_template('simple_list.html', title="🍱 Combos", data=combos)


@app.route('/offers')
def offer():
    return render_template('simple_list.html', title="🎁 Special Offers", data=offers)


@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        budget = int(request.form['budget'])
        taste = request.form['taste']
        cuisine = request.form['cuisine']

        results = [
            item for item in menu
            if item["price"] <= budget and
               (taste == "any" or item["taste"] == taste) and
               (cuisine == "any" or item["cuisine"] == cuisine)
        ]

        return render_template('result.html', data=results, count=len(results))

    return render_template('select.html')


if __name__ == '__main__':
    app.run(debug=True)