spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spice_over_5 = [food for food in spicy_foods if food["heat_level"] > 5]
    return spice_over_5

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = food["heat_level"] * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spice_over_5 = [food for food in spicy_foods if food["heat_level"] > 5]
    for food in spice_over_5:
        heat = food["heat_level"] * "🌶"
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def average(list):
    average = sum(list) / len(list)
    return average

def heat_levels(foods):
    heat = [food["heat_level"] for food in foods]
    return heat

def get_average_heat_level(spicy_foods):
    return average(heat_levels(spicy_foods))
    
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods