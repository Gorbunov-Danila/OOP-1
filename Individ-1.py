#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    valid_nominals = [1, 2, 5, 10, 50, 100, 500, 1000, 5000]  # допустимые номиналы

    def __init__(self, first, second):
        # Проверка на корректность номинала
        if first not in self.valid_nominals:
            raise ValueError(f"Неверный номинал: {first}. Допустимые значения: {self.valid_nominals}")
        # Проверка на то, что количество купюр должно быть целым положительным числом
        if not isinstance(second, int) or second <= 0:
            raise ValueError("Количество купюр должно быть целым положительным числом.")
        # Инициализация полей first и second
        self.first = first
        self.second = second

    def summa(self):
        """Вычисление денежной суммы"""
        # Общая сумма — это произведение номинала на количество купюр
        return self.first * self.second

    def display(self):
        """Вывод номинала и количества купюр"""
        # Вывод номинала и количества купюр на экран
        print(f"Номинал: {self.first}, Количество купюр: {self.second}")

    @staticmethod
    def read():
        """Чтение данных с клавиатуры"""
        try:
            # Ввод номинала купюры
            first = int(input("Введите номинал купюры (1, 2, 5, 10, 50, 100, 500, 1000, 5000): "))
            # Ввод количества купюр
            second = int(input("Введите количество купюр: "))
            # Возвращаем объект Pair, если данные корректны
            return Pair(first, second)
        except ValueError as e:
            # Вывод ошибки, если произошла некорректная передача данных
            print(f"Ошибка: {e}")
            return None


def make_Pair(first, second):
    """Создание объекта Pair с проверкой корректности параметров"""
    try:
        # Создание и возврат объекта Pair
        return Pair(first, second)
    except ValueError as e:
        # Вывод ошибки, если переданы некорректные параметры
        print(f"Ошибка: {e}")
        return None


if __name__ == '__main__':
    # Демонстрация работы класса
    # Чтение данных с клавиатуры для создания объекта Pair
    pair = Pair.read()
    if pair:
        # Если объект успешно создан, выводим его данные
        pair.display()
        # Вывод общей суммы, рассчитанной через метод summa
        print(f"Общая сумма: {pair.summa()} руб.")

    # Тестовый пример создания объекта через make_Pair (необязательно)
    # Создание объекта Pair через make_Pair
    # pair2 = make_Pair(100, 3)
    # if pair2:
    #     # Если объект успешно создан, выводим его данные
    #     pair2.display()
    #     # Вывод общей суммы
    #     print(f"Общая сумма: {pair2.summa()} руб.")


