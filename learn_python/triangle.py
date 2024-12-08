def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides"
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

side1 = 5
side2 = 5
side3 = 5
result = classify_triangle(side1, side2, side3)
print(result)
