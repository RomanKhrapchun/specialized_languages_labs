import unittest
from lab2 import Calculator

class TestCalculator(unittest.TestCase):
    """Набір тестів для класу Calculator."""

    def test_addition(self):
        """Тест для операції додавання."""
        calculator = Calculator()
        result = calculator.calculate(2, '+', 3)
        self.assertEqual(result, 5, "Додавання не працює для позитивних чисел")

        result = calculator.calculate(-2, '+', -3)
        self.assertEqual(result, -5, "Додавання не працює для від'ємних чисел")

    def test_subtraction(self):
        """Тест для операції віднімання."""
        calculator = Calculator()
        result = calculator.calculate(5, '-', 3)
        self.assertEqual(result, 2, "Віднімання не працює для позитивних чисел")

        result = calculator.calculate(-3, '-', -1)
        self.assertEqual(result, -2, "Віднімання не працює для від'ємних чисел")

    def test_multiplication(self):
        """Тест для операції множення."""
        calculator = Calculator()
        result = calculator.calculate(5, '*', 0)
        self.assertEqual(result, 0, "Множення не працює з нулем")

        result = calculator.calculate(5, '*', 3)
        self.assertEqual(result, 15, "Множення не працює для позитивних чисел")

        result = calculator.calculate(5, '*', -3)
        self.assertEqual(result, -15, "Множення не працює для від'ємних чисел")

    def test_division(self):
        """Тест для операції ділення."""
        calculator = Calculator()
        result = calculator.calculate(15, '/', 3)
        self.assertEqual(result, 5, "Ділення працює для позитивних чисел")

        result = calculator.calculate(15, '/', -3)
        self.assertEqual(result, -5, "Ділення не працює для від'ємних чисел")

        result = calculator.calculate(5, '/', 0)
        self.assertEqual(result, "Не можна ділити на нуль", "Помилка ділення на нуль")

    def test_error_handling(self):
        """Тест для обробки помилок."""
        calculator = Calculator()
        result = calculator.calculate(3, '+', 'abc')
        self.assertEqual(result, "Невірний формат числа", "Помилка невірного формату числа")

        result = calculator.calculate('abc', '+', 3)
        self.assertEqual(result, "Невірний формат числа", "Помилка невірного формату числа")
        result = calculator.calculate(10, '/', 0)
        self.assertEqual(result, "Помилка: Не можна ділити на нуль!", "Помилка ділення на нуль")

        result = calculator.calculate(-25, '√', 0)
        self.assertEqual(result, "Від'ємне число", "Помилка обчислення кореня з від'ємного числа")

def run_lab6():
    """Функція для запуску тестів."""
    unittest.main()

if __name__ == '__main__':
    run_lab6()
