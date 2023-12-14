import math

class Calculator:
    """
    Клас калькулятора для базових арифметичних операцій.

    Attributes:
    - result (float): Результат останнього обчислення.
    - history (list): Список для зберігання історії обчислень.
    """

    def __init__(self):
        """Ініціалізація об'єкта Calculator."""
        self.result = None
        self.history = []

    def calculate(self, expression):
        """
        Виконати обчислення на основі заданого виразу.

        Args:
        - expression (str): Математичний вираз для оцінки.

        Returns:
        - float: Результат обчислення.
        """
        num1, operator, num2 = map(str.strip, expression.split())

        if operator not in ('+', '-', '*', '/', '^', '√', '%'):
            raise ValueError("Невірний оператор!")

        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            self.result = num1 + num2
        elif operator == '-':
            self.result = num1 - num2
        elif operator == '*':
            self.result = num1 * num2
        elif operator == '/':
            if num2 == 0 or num1 == 0:
                raise ValueError("Неможливо ділити на нуль!")
            self.result = num1 / num2
        elif operator == '^':
            self.result = num1 ** num2
        elif operator == '√':
            self.result = math.sqrt(num1)
        elif operator == '%':
            self.result = num1 % num2

        self.history.append((expression, self.result))
        return self.result

class CalculatorApp:
    """
    Клас CalculatorApp для запуску додатку калькулятора.

    Attributes:
    - calculator (Calculator): Об'єкт Calculator для виконання обчислень.
    """

    def __init__(self):
        """Ініціалізація об'єкта CalculatorApp."""
        self.calculator = Calculator()


def run_lab1():
    """Запустити додаток калькулятора."""
    app = CalculatorApp()
    while True:
        expression = input("Введіть вираз (наприклад 1 + 1): ")

        if expression.lower() == 'вихід':
            break

        try:
            result = app.calculator.calculate(expression)
            print(f"Результат: {result}")

            print("Історія обчислень:")
            for expr, res in app.calculator.history:
                print(f"{expr} = {res}")

            next_operation = input("Продовжити (так/ні)? ")
            if next_operation.lower() != 'так':
                break

        except ValueError as e:
            print(f"Помилка: {e}")

    print("Вихід з калькулятора")

if __name__ == "__main__":
    run_lab1()
