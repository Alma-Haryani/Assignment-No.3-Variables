# Q# 01: Calculate Sum, Difference, Product, and Average of Three Numbers

def calculate_operations(num1, num2, num3):
    # Calculate sum
    total_sum = num1 + num2 + num3
    
    # Calculate difference
    difference = num1 - num2 - num3
    
    # Calculate product
    product = num1 * num2 * num3
    
    # Calculate average
    average = total_sum / 3
    
    return total_sum, difference, product, average

# Input: Three numbers from the user
try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    number3 = float(input("Enter the third number: "))
    
    # Perform calculations
    total_sum, difference, product, average = calculate_operations(number1, number2, number3)
    
    # Output the results
    print(f"Sum: {total_sum}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Average: {average}")

except ValueError:
    print("Please enter valid numbers.")

# Q# 02: Calculate the Area of Different Shapes

import math

def calculate_area(shape, *dimensions):
    if shape == "triangle":
        base, height = dimensions
        area = 0.5 * base * height
    elif shape == "square":
        side = dimensions[0]
        area = side ** 2
    elif shape == "circle":
        radius = dimensions[0]
        area = math.pi * (radius ** 2)
    elif shape == "rectangle":
        length, width = dimensions
        area = length * width
    else:
        area = None
    return area

# Input: Shape type and dimensions from the user
shape_type = input("Enter the shape (triangle, square, circle, rectangle): ").lower()

if shape_type == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = calculate_area(shape_type, base, height)

elif shape_type == "square":
    side = float(input("Enter the side length of the square: "))
    area = calculate_area(shape_type, side)

elif shape_type == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area(shape_type, radius)

elif shape_type == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculate_area(shape_type, length, width)

else:
    area = None

if area is not None:
    print(f"The area of the {shape_type} is: {area}")
else:
    print("Invalid shape type.")