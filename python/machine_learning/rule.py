def classify_animal(characteristics):
    if characteristics.get('has_fur', False):
        if characteristics.get('gives_birth', False):
            return "Mammal"
        elif characteristics.get('lays_eggs', False):  # If it lays eggs
            return "Monotreme (Egg-laying Mammal)"

        else:
            return "Unknown Mammal-like Animal"

    elif characteristics.get('lays_eggs', False):  # .get() is also used here

        if characteristics.get('has_wings', False):
            return "Bird"
        else:
            return "Reptile"

    elif characteristics.get('has_scales', False) and characteristics.get('cold_blooded', False):
        return "Reptile"

    elif characteristics.get('warm_blooded', False):

        if characteristics.get('has_wings', False):
            return "Bird"
        else:
            return "Mammal"

    return "Unknown Animal"



animal_1 = {'has_fur': True, 'gives_birth': True}
animal_2 = {'lays_eggs': True, 'has_wings': True}
animal_3 = {'has_scales': True, 'cold_blooded': True}

print(classify_animal(animal_1))  
print(classify_animal(animal_2))
print(classify_animal(animal_3))
