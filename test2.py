# import test as t
#
# def input1(): #Возвращает 1 целое числа
#     while True:
#         try:
#             a = float(input("Введите число: "))
#             return a  # Возвращаем введённое число, если оно корректное
#         except ValueError:
#             print("Ошибка: введите число. Попробуйте снова.")
# def input2(): #Возвращает 2 целых числа
#     while True:
#         try:
#             a = float(input("Введите число1: "))
#             b = float(input("Введите число2: "))
#             return a ,b  # Возвращаем введённое число, если оно корректное
#         except ValueError:
#             print("Ошибка: введите число. Попробуйте снова.")
# def input3(): # Возвращает 3 целых числа
#     while True:
#         try:
#             a = float(input("Введите число1: "))
#             b = float(input("Введите число2: "))
#             с = float(input("Введите число3: "))
#             return a , b, с  # Возвращаем введённое число, если оно корректное
#         except ValueError:
#             print("Ошибка: введите целые числа. Попробуйте снова.")
# def print_question_area(*args):
#     if len(args) == 2:
#         name, b = args
#         print(f'Чтобы вычислить площадь {name}, введите {b}:')
#     elif len(args) == 3:
#         name, b, c = args
#         print(f'Чтобы вычислить площадь {name}, введите {b} и {c}:')
#     elif len(args) == 4:
#         name, b, c, d = args
#         print(f'Чтобы вычислить площадь {name}, введите {b}, {c} и {d}:')
# def print_question_per(*args):
#     if len(args) == 2:
#         name, b = args
#         print(f'Чтобы вычислить периметр {name}, введите {b}:')
#     elif len(args) == 3:
#         name, b, c = args
#         print(f'Чтобы вычислить периметр {name}, введите {b} и {c}:')
#     elif len(args) == 4:
#         name, b, c, d = args
#         print(f'Чтобы вычислить периметр {name}, введите {b}, {c} и {d}:')
#
#
# # Вычисляем и выводим площадь квадрата со стороной
# def square_area():
#     name = 'квадрата'
#     stor = "длину одной стороны"
#     print_question_area(name,stor)
#     square_area = t.calculate_square_area(input1())
#     print(f"Площадь квадрата: {square_area}")
# #вычисляет площадь прямоугольника по его длине и ширине.
# def rectangle_area():
#     name = 'прямоугольника'
#     length_n = 'длину'
#     width_n = 'ширину'
#     poka = True
#     while poka:
#         print_question_area(name, length_n, width_n)
#         length, width = input2()
#         if length != width:
#             area = t.calculate_rectangle_area(length, width)
#             print(f"Площадь прямоугольника: {area}")
#             break
#         else:
#             choice_sq_or_rec = int(input("Ошибка: у прямоугольника стороны должны быть разными. Попробуйте снова.Или у вас квадарат. Введити 1 если у вас квадрат, если нет то 2 "))
#             if choice_sq_or_rec == 1:
#                 print(f'Площадь вашего квадарата: {length**2}')
#                 poka = False
#             else:
#                 poka = True
#
#
# #вычисляет площадь круга по его радиусу.
# def circle_area():
#     name = 'круга'
#     stor = "радиус"
#     print_question_area(name, stor)
#     radius = input1()
#     crc = t.calculate_circle_area(radius)
#     print(f"Площадь круга: {crc}")
#
# #вычисляет площадь треугольника по его основанию и высоте.
# def triangle_area():
#     name = 'треугольника'
#     stor = "его основание и высоту"
#     print_question_area(name, stor)
#     base, height = input2()
#     tri = t.calculate_triangle_area(base, height)
#     print(f"Площадь тругольника: {tri}")
# # #вычисляет периметр квадраpr
#
# def square_perimeter():
#     name = 'квадрата'
#     stor = "длину одной стороны"
#     print_question_per(name, stor)
#     square_per = t.calculate_square_perimeter(input1())
#     print(f"Периметр квадрата: {square_per}")
#
# # #вычисляет периметр прямоугольника по его длине и ширине.
# def rectangle_perimeter():
#     name = 'прямоугольника'
#     length_n = 'длину'
#     width_n = 'ширину'
#     poka = True
#     while poka:
#         print_question_per(name, length_n, width_n)
#         length, width = input2()
#         if length != width:
#             area = t.calculate_rectangle_perimeter(length, width)
#             print(f"Периметр прямоугольника: {area}")
#             break
#         else:
#             choice_sq_or_rec=int(input("Ошибка: у прямоугольника стороны должны быть разными. Попробуйте снова.Или у вас квадарат. Введити 1 если у вас квадрат, если нет то 2 "))
#             if choice_sq_or_rec == 1:
#                 print(f'Периметр вашего квадарата: {length*4}')
#                 poka = False
#             else:
#                 poka = True
#     # rec_p = t.calculate_rectangle_perimeter(input2())
#     # return rec_p
# #вычисляет периметр круга по его радиусу.
# def circle_perimeter():
#     name = 'круга'
#     stor = "радиус"
#     print_question_per(name, stor)
#     radius = input1()
#     crc = t.calculate_circle_perimeter(radius)
#     print(f"Периметр круга: {crc}")
#     # return t.calculate_circle_perimeter(input1())
#
# #вычисляет периметр треугольника по его трем сторонам.
# def triangle_perimeter():
#     name = 'треугольника'
#     stor = "его три стороны"
#     print_question_per(name, stor)
#     a, b, c = input3()
#     tri = t.calculate_triangle_perimeter(a, b, c)
#     print(f"Периметр тругольника: {tri}")
#     # return t.calculate_triangle_perimeter(input3())
#
#
# if __name__ == "__main__":
#     # while True:
#         # square_area()
#         # rectangle_area()
#         # circle_area()
#         # triangle_area()
#         square_perimeter()
#         rectangle_perimeter()
#         circle_perimeter()
#         triangle_perimeter()
# chat gpt

import test as t

def input1():
    """Возвращает одно число типа float после проверки."""
    while True:
        try:
            a = float(input("Введите число: "))
            return a
        except ValueError:
            print("Ошибка: введите число. Попробуйте снова.")

def input2():
    """Возвращает два числа типа float после проверки."""
    while True:
        try:
            a = float(input("Введите число1: "))
            b = float(input("Введите число2: "))
            return a, b
        except ValueError:
            print("Ошибка: введите числа. Попробуйте снова.")

def input3():
    """Возвращает три числа типа float после проверки."""
    while True:
        try:
            a = float(input("Введите число1: "))
            b = float(input("Введите число2: "))
            c = float(input("Введите число3: "))
            return a, b, c
        except ValueError:
            print("Ошибка: введите числа. Попробуйте снова.")

def print_question_area(name, *args):
    """Выводит запрос на ввод данных для расчета площади."""
    args_str = ' и '.join(args)
    print(f'Чтобы вычислить площадь {name}, введите {args_str}:')

def print_question_per(name, *args):
    """Выводит запрос на ввод данных для расчета периметра."""
    args_str = ' и '.join(args)
    print(f'Чтобы вычислить периметр {name}, введите {args_str}:')

def square_area():
    """Вычисляет и выводит площадь квадрата по стороне."""
    print_question_area('квадрата', 'длину одной стороны')
    side = input1()
    area = t.calculate_square_area(side)
    print(f"Площадь квадрата: {area}")

def rectangle_area():
    """Вычисляет и выводит площадь прямоугольника по длине и ширине."""
    while True:
        print_question_area('прямоугольника', 'длину', 'ширину')
        length, width = input2()
        if length != width:
            area = t.calculate_rectangle_area(length, width)
            print(f"Площадь прямоугольника: {area}")
            break
        else:
            choice = int(input("Ошибка: у прямоугольника стороны должны быть разными. Введите 1 если это квадрат, или 2 если хотите повторить ввод: "))
            if choice == 1:
                print(f'Площадь квадрата: {length ** 2}')
                break

def circle_area():
    """Вычисляет и выводит площадь круга по радиусу."""
    print_question_area('круга', 'радиус')
    radius = input1()
    area = t.calculate_circle_area(radius)
    print(f"Площадь круга: {area}")

def triangle_area():
    """Вычисляет и выводит площадь треугольника по основанию и высоте."""
    while True:
        print_question_area('треугольника', 'основание', 'высоту')
        base, height = input2()
        if base != height:
            area = t.calculate_triangle_area(base, height)
            print(f"Площадь треугольника: {area}")

            return
        else:
            print("Ошибка: основание и высота не могут быть одинаковыми.попробуйте еще раз")

def square_perimeter():
    """Вычисляет и выводит периметр квадрата по стороне."""
    print_question_per('квадрата', 'длину одной стороны')
    side = input1()
    perimeter = t.calculate_square_perimeter(side)
    print(f"Периметр квадрата: {perimeter}")

def rectangle_perimeter():
    """Вычисляет и выводит периметр прямоугольника по длине и ширине."""
    while True:
        print_question_per('прямоугольника', 'длину', 'ширину')
        length, width = input2()
        if length != width:
            perimeter = t.calculate_rectangle_perimeter(length, width)
            print(f"Периметр прямоугольника: {perimeter}")
            break
        else:
            choice = int(input("Ошибка: у прямоугольника стороны должны быть разными. Введите 1 если это квадрат, или 2 если хотите повторить ввод: "))
            if choice == 1:
                print(f'Периметр квадрата: {length * 4}')
                break

def circle_perimeter():
    """Вычисляет и выводит периметр круга по радиусу."""
    print_question_per('круга', 'радиус')
    radius = input1()
    perimeter = t.calculate_circle_perimeter(radius)
    print(f"Периметр круга: {perimeter}")

def triangle_perimeter():
    """Вычисляет и выводит периметр треугольника по трем сторонам."""
    print_question_per('треугольника', 'три стороны')
    a, b, c = input3()
    perimeter = t.calculate_triangle_perimeter(a, b, c)
    print(f"Периметр треугольника: {perimeter}")

if __name__ == "__main__":
    # Пример вызова функций. Можно раскомментировать нужные функции для запуска.
    # square_area()
    # rectangle_area()
    # circle_area()
    # triangle_area()
    # square_perimeter()
    rectangle_perimeter()
    # circle_perimeter()
    # triangle_perimeter()
