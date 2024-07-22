# from math import pi
#
# def calculate_square_area(side_length):                 #вычисляет площадь квадрата по его стороне.
#     side_length = int(side_length)**2
#     return (side_length)
# #вычисляет площадь прямоугольника по его длине и ширине.
# def calculate_rectangle_area(length, width):
#     if length != width:
#         return length * width
#     else:
#         return "У прямоугольника стороны должны быть разыне"
#
# #вычисляет площадь круга по его радиусу.
# def calculate_circle_area(radius):
#     return f'Площадь круга {radius**2* pi}'
#
# #вычисляет площадь треугольника по его основанию и высоте.
# def calculate_triangle_area(base, height):
#     return f'{base * height / 2}'
#
# #вычисляет периметр квадрата по его стороне.
# def calculate_square_perimeter(side_length):
#     return f' {side_length*4}'
#
# #вычисляет периметр прямоугольника по его длине и ширине.
# def calculate_rectangle_perimeter(length, width):
#     return f'{(length+width)*2}'
#
#
# #вычисляет периметр круга по его радиусу.
# def calculate_circle_perimeter(radius):
#     return f'{radius*(2* pi)}'
#
#
# #вычисляет периметр треугольника по его трем сторонам.
# def calculate_triangle_perimeter(side1, side2, side3):
#     return f'{side1 + side2 + side3}'
#
#
# if __name__ == "__main__":
#     print(calculate_square_area(7))


from math import pi

def calculate_square_area(side_length):
    """Вычисляет площадь квадрата по его стороне."""
    return side_length ** 2

def calculate_rectangle_area(length, width):
    """Вычисляет площадь прямоугольника по его длине и ширине."""
    if length != width:
        return length * width
    else:
        return "У прямоугольника стороны должны быть разными"

def calculate_circle_area(radius):
    """Вычисляет площадь круга по его радиусу."""
    return radius ** 2 * pi

def calculate_triangle_area(base, height):
    """Вычисляет площадь треугольника по его основанию и высоте."""
    return base * height / 2

def calculate_square_perimeter(side_length):
    """Вычисляет периметр квадрата по его стороне."""
    return side_length * 4

def calculate_rectangle_perimeter(length, width):
    """Вычисляет периметр прямоугольника по его длине и ширине."""
    return (length + width) * 2

def calculate_circle_perimeter(radius):
    """Вычисляет периметр круга по его радиусу."""
    return 2 * radius * pi

def calculate_triangle_perimeter(side1, side2, side3):
    """Вычисляет периметр треугольника по его трем сторонам."""
    return side1 + side2 + side3

if __name__ == "__main__":
    # Пример вызова функций
    print(f"Площадь квадрата: {calculate_square_area(7)}")
    print(f"Площадь прямоугольника: {calculate_rectangle_area(5, 10)}")
    print(f"Площадь круга: {calculate_circle_area(3)}")
    print(f"Площадь треугольника: {calculate_triangle_area(6, 4)}")
    print(f"Периметр квадрата: {calculate_square_perimeter(7)}")
    print(f"Периметр прямоугольника: {calculate_rectangle_perimeter(5, 10)}")
    print(f"Периметр круга: {calculate_circle_perimeter(3)}")
    print(f"Периметр треугольника: {calculate_triangle_perimeter(3, 4, 5)}")