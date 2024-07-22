# import test2 as t2
#
# print('''Это программа калькулятор вычислений а именно он вычисляет:
#
#            площадь квадрата по его стороне.
#            площадь прямоугольника по его длине и ширине.
#            площадь круга по его радиусу.
#            площадь треугольника по его основанию и высоте.
#            периметр квадрата по его стороне.
#            периметр прямоугольника по его длине и ширине.
#            периметр круга по его радиусу.
#            периметр треугольника по его трем сторонам.
#  ''')
# answer1= True
# while answer1:
#     choice = int(input('''Что вы хотите вычислить? Площадь или периметр? если площадь введите 1, если перимметр 2: '''))
#     if choice == 1:
#         while True:
#             choice_2 = int(input('''
#             1.Квадарата
#             2.прямоугольника
#             3.круга по радиусу
#             4.треугольника
#             5.выбрать другое: '''))
#             if choice_2 == 1:
#                 t2.square_area()
#                 break
#
#             elif choice_2 ==2:
#                 t2.rectangle_area()
#                 break
#
#             elif choice_2 == 3:
#                 t2.circle_area()
#                 break
#
#             elif choice_2 ==4:
#                 t2.triangle_area()
#                 break
#
#             elif choice_2 == 5:
#                 break
#
#             else:
#                 print('ошибка')
#         # qu= int(input('''Вы хотите продолжить? Введите 1 чтобы продолжить, 2 если нет: '''))
#         # if qu == 1:
#         #     answer1 =True
#         # elif qu == 2:
#         #   break
#         # else:
#         #         print('вы ввели неправильное значаение')
#
#     elif choice == 2:
#         while True:
#             choice_2 = int(input('''
#             1.Квадарата
#             2.прямоугольника
#             3.круга по радиусу
#             4.треугольника
#             5.выбрать другое:
#             '''))
#             if choice_2 == 1:
#                 t2.square_perimetr()
#                 break
#
#             elif choice_2 ==2:
#                 t2.rectangle_perimetr()
#                 break
#
#
#             elif choice_2 ==3:
#                 t2.circle_perimetr()
#                 break
#
#             elif choice_2 ==4:
#                 t2.triangle_perimetr()
#                 break
#             elif choice_2 == 5:
#                 break
#
#             else:
#                 print('ошибка')
#
#     qu = int(input('''Вы хотите продолжить? Введите 1 чтобы продолжить, 2 если нет: '''))
#     if qu == 1:
#         answer1 = True
#     elif qu == 2:
#         break
#     else:
#         print('вы ввели неправильное значаение')
#     # else:
#     #     print('вы ввели неправильное значение, повторите попытку')
#
# Улучшение чат4

import test2 as t2


def print_welcome_message():
    print('''Это программа калькулятор вычислений, а именно он вычисляет:
           площадь квадрата по его стороне.
           площадь прямоугольника по его длине и ширине.
           площадь круга по его радиусу.
           площадь треугольника по его основанию и высоте.
           периметр квадрата по его стороне.
           периметр прямоугольника по его длине и ширине.
           периметр круга по его радиусу.
           периметр треугольника по его трем сторонам.
    ''')


def get_choice(prompt, choices):
    while True:
        try:
            choice = int(input(prompt))
            if choice in choices:
                return choice
            else:
                print('Ошибка: выберите правильный номер.')
        except ValueError:
            print('Ошибка: введите число.')


def handle_area_choice():
    while True:
        choice_2 = get_choice('''
            1. Квадрат
            2. Прямоугольник
            3. Круг
            4. Треугольник
            5. Вернуться в меню
        ''', {1, 2, 3, 4, 5})

        if choice_2 == 1:
            t2.square_area()
        elif choice_2 == 2:
            t2.rectangle_area()
        elif choice_2 == 3:
            t2.circle_area()
        elif choice_2 == 4:
            t2.triangle_area()
        elif choice_2 == 5:
            break
        break


def handle_perimeter_choice():
    while True:
        choice_2 = get_choice('''
            1. Квадрат
            2. Прямоугольник
            3. Круг
            4. Треугольник
            5. Вернуться в меню
        ''', {1, 2, 3, 4, 5})

        if choice_2 == 1:
            t2.square_perimeter()
        elif choice_2 == 2:
            t2.rectangle_perimeter()
        elif choice_2 == 3:
            t2.circle_perimeter()
        elif choice_2 == 4:
            t2.triangle_perimeter()
        elif choice_2 == 5:
            break
        break

def main():
    print_welcome_message()

    while True:
        choice = get_choice('''Что вы хотите вычислить? Площадь или периметр?
            Введите 1 для площади, 2 для периметра: ''', {1, 2})

        if choice == 1:
            handle_area_choice()
        elif choice == 2:
            handle_perimeter_choice()

        qu = get_choice('''Вы хотите продолжить? Введите 1, чтобы продолжить, 2, если нет: ''', {1, 2})
        if qu == 2:
            print("Спасибо за использование программы!")
            break


if __name__ == "__main__":
    main()





