def calculate_calories_in(food_items):
    total_calories_in = 0
    for food, calories in food_items.items():
        total_calories_in += calories
    return total_calories_in


def calculate_calories_burned(exercise_duration, metabolic_rate):
    calories_burned = exercise_duration * metabolic_rate
    return calories_burned  # Return the calculated number of calories burned.


def calculate_energy_balance(calories_in, calories_burned):
    # Check if more calories have been consumed than burned.
    if calories_in > calories_burned:
        return "Surplus"
    elif calories_in < calories_burned:
        return "Deficit"  # Return 'Deficit'(weight loss potential).
    else:
        return "Maintenance"


food_items = {
    "apple": 95,
    "banana": 105,
    "sandwich": 300
}
exercise_duration = 1.5
metabolic_rate = 70
calories_in = calculate_calories_in(food_items)
calories_burned = calculate_calories_burned(exercise_duration, metabolic_rate)
energy_balance = calculate_energy_balance(calories_in, calories_burned)
print(f"Calories consumed: {calories_in}")
print(f"Calories burned: {calories_burned}")
print(f"Energy balance: {energy_balance}")
