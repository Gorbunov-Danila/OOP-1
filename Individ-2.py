#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        """Инициализация треугольника с проверкой корректности данных."""
        # Проверка, что стороны и углы треугольника корректны
        if not self._validate_sides_and_angles(side1, side2, side3, angle1, angle2, angle3):
            raise ValueError("Неправильные стороны или углы.")
        # Инициализация сторон и углов треугольника
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    @staticmethod
    def _validate_sides_and_angles(side1, side2, side3, angle1, angle2, angle3):
        """Проверка корректности введенных данных."""
        # Все стороны должны быть положительными
        sides_positive = all(side > 0 for side in [side1, side2, side3])
        # Сумма углов треугольника должна быть 180 градусов
        angles_sum_180 = math.isclose(angle1 + angle2 + angle3, 180)
        # Возвращаем результат проверки
        return sides_positive and angles_sum_180

    def get_sides(self):
        """Получение сторон треугольника."""
        # Возвращаем стороны треугольника
        return self.side1, self.side2, self.side3

    def get_angles(self):
        """Получение углов треугольника."""
        # Возвращаем углы треугольника
        return self.angle1, self.angle2, self.angle3

    def set_sides(self, side1, side2, side3):
        """Установка новых сторон треугольника с проверкой."""
        # Проверка корректности новых сторон
        if self._validate_sides_and_angles(side1, side2, side3, self.angle1, self.angle2, self.angle3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise ValueError("Некорректные стороны.")

    def set_angles(self, angle1, angle2, angle3):
        """Установка новых углов треугольника с проверкой."""
        # Проверка корректности новых углов
        if self._validate_sides_and_angles(self.side1, self.side2, self.side3, angle1, angle2, angle3):
            self.angle1 = angle1
            self.angle2 = angle2
            self.angle3 = angle3
        else:
            raise ValueError("Некорректные углы.")

    def perimeter(self):
        """Вычисление периметра треугольника."""
        # Периметр — это сумма всех сторон
        return self.side1 + self.side2 + self.side3

    def area(self):
        """Вычисление площади треугольника по формуле Герона."""
        # Полупериметр для использования в формуле Герона
        p = self.perimeter() / 2
        # Формула Герона для вычисления площади
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def height(self):
        """Вычисление высот треугольника."""
        # Высоты вычисляются как (2 * площадь) / соответствующая сторона
        area = self.area()
        return (2 * area / self.side1, 2 * area / self.side2, 2 * area / self.side3)

    def triangle_type(self):
        """Определение типа треугольника: равносторонний, равнобедренный или прямоугольный."""
        # Если все стороны равны — треугольник равносторонний
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний"
        # Если две стороны равны — треугольник равнобедренный
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return "Равнобедренный"
        # Если один из углов равен 90 градусов — треугольник прямоугольный
        elif math.isclose(self.angle1, 90) or math.isclose(self.angle2, 90) or math.isclose(self.angle3, 90):
            return "Прямоугольный"
        # Если ни одно из условий не выполнено — треугольник произвольный
        else:
            return "Произвольный"

    def display(self):
        """Вывод треугольника."""
        # Вывод сторон и углов треугольника на экран
        print(f"Стороны: {self.side1}, {self.side2}, {self.side3}")
        print(f"Углы: {self.angle1}, {self.angle2}, {self.angle3}")

    @staticmethod
    def read():
        """Чтение данных с клавиатуры для создания треугольника."""
        try:
            # Ввод сторон треугольника
            side1 = float(input("Введите сторону 1: "))
            side2 = float(input("Введите сторону 2: "))
            side3 = float(input("Введите сторону 3: "))
            # Ввод углов треугольника
            angle1 = float(input("Введите угол 1: "))
            angle2 = float(input("Введите угол 2: "))
            angle3 = float(input("Введите угол 3: "))
            # Создание и возврат объекта Triangle
            return Triangle(side1, side2, side3, angle1, angle2, angle3)
        except ValueError as e:
            # Обработка ошибки ввода
            print(f"Ошибка: {e}")
            return None


def make_Triangle(side1, side2, side3, angle1, angle2, angle3):
    """Создание объекта Triangle с проверкой параметров."""
    try:
        # Создание и возврат объекта Triangle
        return Triangle(side1, side2, side3, angle1, angle2, angle3)
    except ValueError as e:
        # Обработка ошибки создания треугольника
        print(f"Ошибка: {e}")
        return None


if __name__ == '__main__':
    # Демонстрация работы класса
    triangle = Triangle.read()
    if triangle:
        # Вывод сторон и углов треугольника
        triangle.display()
        # Вычисление и вывод периметра треугольника
        print(f"Периметр: {triangle.perimeter()}")
        # Вычисление и вывод площади треугольника
        print(f"Площадь: {triangle.area()}")
        # Вычисление и вывод высот треугольника
        print(f"Высоты: {triangle.height()}")
        # Определение и вывод типа треугольника
        print(f"Тип треугольника: {triangle.triangle_type()}")
