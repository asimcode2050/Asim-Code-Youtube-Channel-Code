
class FoodItem:
    def __init__(self, name, calories, fat, protein, carbs):
        self.name = name
        self.calories = calories
        self.fat = fat
        self.protein = protein
        self.carbs = carbs

    def __str__(self):
        return f'{self.name} - Calories: {self.calories}, Fat: {self.fat}g, Protein: {self.protein}g, Carbs: {self.carbs}g'


apple = FoodItem('Apple', 95, 0.3, 0.5, 25)
banana = FoodItem('Banana', 105, 0.3, 1.3, 27)
chicken_breast = FoodItem('Chicken Breast', 165, 3.6, 31, 0)
food_database = {
    'apple': apple,
    'banana': banana,
    'chicken_breast': chicken_breast
}


def get_nutrition(food_name):
    food = food_database.get(food_name.lower())
    if food:
        print(food)
    else:
        print(f'Sorry, we do not have nutritional information for {
              food_name}.')


get_nutrition('banana')
get_nutrition('pizza')
