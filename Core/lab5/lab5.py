from termcolor import colored
from abc import ABC, abstractmethod
import os

class Figure:
    """
    Базовий клас для представлення геометричних фігур.

    Attributes:
        size (int): Розмір фігури.
        color (str): Колір фігури.

    Methods:
        setSize(size: int): Встановлює розмір фігури.
        setColor(color: str): Встановлює колір фігури.
        generateFigure(): Абстрактний метод для генерації фігури.
    """
    
    def __init__(self):
        self.size = 1
        self.color = 'green'

    def setSize(self, size):
        """Встановлює розмір фігури."""
        self.size = size

    def setColor(self, color):
        """Встановлює колір фігури."""
        self.color = color

    def generateFigure(self):
        """Абстрактний метод для генерації фігури."""
        return ""


def paintText(text, color):
    """
    Функція для забарвлення тексту в заданий колір.

    Args:
        text (str): Вхідний текст.
        color (str): Колір для забарвлення.

    Returns:
        str: Забарвлений текст.
    """
    if len(color):
        painted = colored(text, color)
        return painted
    else:
        return text


def textFileSaver(filename, text):
    """Функція для збереження тексту у файл у папці Data."""
    
    # Отримуємо шлях до поточної директорії, де виконується скрипт
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Виходимо на рівень вище до папки Core
    parent_dir = os.path.dirname(current_dir)
    
    # Вказуємо шлях до папки Data, яка знаходиться на тому ж рівні, що й Core
    data_dir = os.path.join(parent_dir, 'Data')
    
    # Створюємо шлях до файлу в папці Data
    file_path = os.path.join(data_dir, filename)
    
    # Зберігаємо текст у файл
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Файл збережено у {file_path}")



class Command(ABC):
    """
    Абстрактний клас для представлення команди.

    Methods:
        execute(): Абстрактний метод для виконання команди.
    """
    @abstractmethod
    def execute(self):
        pass
    
class Square(Figure):
    """
    Клас для представлення квадрата.

    Methods:
        generateSquare(): Генерує квадрат з врахуванням розміру.
        generateFigure(): Перевизначений метод для генерації квадрата з врахуванням кольору.
    """
    def __init__(self):
        super().__init__()

    def generateSquare(self):
        """Генерує квадрат з врахуванням розміру."""
        n = self.size
        line = ''
        if n > 1:
            line += n * 2 * '_'
        else:
            line += '_'

        top_line = ' ' + line
        bottom_line = '|' + line + '|' + '\n'

        inner_spaces = n * 2 * ' '
        inner_fill = '|' + inner_spaces + '|'
        content = ''

        i = 1
        while (i < n):
            content += inner_fill + '\n'
            i += 1

        square = top_line + '\n' + content + bottom_line
        return square

    def generateFigure(self):
        """Перевизначений метод для генерації квадрата з врахуванням кольору."""
        generated = self.generateSquare()
        colored = paintText(generated, self.color)
        return colored
    
class Cube(Figure):
    """
    Клас для представлення куба.

    Methods:
        generateCube(): Генерує куб з врахуванням розміру.
        generateFigure(): Перевизначений метод для генерації куба з врахуванням кольору.
    """
    def __init__(self):
        super().__init__()

    def generateCube(self):
        """Генерує куб з врахуванням розміру."""

        n = self.size
        line = ''
        if n > 1:
            line += n * 2 * 'X'
        else:
            line += 'X'

        top_line = n * ' ' + line
        mid_line_space = 2 * n - 2
        mid_line = '/' + line + '/' + mid_line_space * ' ' + '\\'
        bottom_line = (n - 1) * ' ' + '\\' + line + '\/'

        inner_spaces = n * 2 * ' '
        inner_top = '/' + inner_spaces + '/'
        inner_bottom = '\\' + inner_spaces + '\\'

        top_content = ''
        bottom_content = ''

        for i in range(1, n):
            top_content += (n - i) * ' ' + inner_top + \
                (i - 1) * 2 * ' ' + '\\' + '\n'
            bottom_content += (i - 1) * ' ' + inner_bottom + \
                (n - i) * 2 * ' ' + '/' + '\n'

        cube = top_line + '\n' + top_content + mid_line + \
            '\n' + bottom_content + bottom_line + '\n'
        return cube

    def generateFigure(self):
        """Перевизначений метод для генерації куба з врахуванням кольору."""
        generated = self.generateCube()
        colored = paintText(generated, self.color)
        return colored

class Generate3DFigureCommand(Command):
    """
    Команда для генерації 3D фігури через інтерфейс.

    Attributes:
        figure_interface (FigureArtInterface): Інтерфейс фігури, через який відбувається генерація.

    Methods:
        execute(): Виконує команду генерації 3D фігури.
    """
    def __init__(self, figure_interface):
        self.figure_interface = figure_interface

    def execute(self):
        """Виконує команду генерації 3D фігури."""
        print(self.figure_interface.generate3dFigure())


class SetSizeCommand(Command):
    """
    Команда для встановлення розміру фігури через інтерфейс.

    Attributes:
        figure_interface (FigureArtInterface): Інтерфейс фігури, для якого встановлюється розмір.
        new_size (int): Новий розмір фігури.

    Methods:
        execute(): Виконує команду встановлення розміру фігури.
    """
    def __init__(self, figure_interface, new_size):
        self.figure_interface = figure_interface
        self.new_size = new_size

    def execute(self):
        """Виконує команду встановлення розміру фігури."""
        self.figure_interface.setSize(self.new_size)


class SetColorCommand(Command):
    """
    Команда для встановлення кольору фігури через інтерфейс.

    Attributes:
        figure_interface (FigureArtInterface): Інтерфейс фігури, для якого встановлюється колір.
        new_color (str): Новий колір фігури.

    Methods:
        execute(): Виконує команду встановлення коліру фігури.
    """
    def __init__(self, figure_interface, new_color):
        self.figure_interface = figure_interface
        self.new_color = new_color

    def execute(self):
        """Виконує команду встановлення коліру фігури."""
        self.figure_interface.setColor(self.new_color)


class FigureArtInterface(Figure):
    """
    Клас інтерфейсу для взаємодії з геометричними фігурами.

    Attributes:
        type (str): Тип фігури.
        left_padding (int): Лівий відступ.
        top_padding (int): Верхній відступ.
        bottom_padding (int): Нижній відступ.
        commands (dict): Словник команд для взаємодії з інтерфейсом.

    Methods:
        setType(type: str): Встановлює тип фігури.
        setPaddings(left_padding: int, top_padding: int, bottom_padding: int): Встановлює відступи фігури.
        setPrimaryData(): Запитує користувача про основні дані фігури.
        generateWithLeftPadding(text: str): Генерує текст з лівим відступом.
        generateWithTopPadding(text: str): Генерує текст з верхнім відступом.
        generateWithBottomPadding(text: str): Генерує текст з нижнім відступом.
        generateWithPaddings(text: str): Генерує текст з врахуванням усіх відступів.
        generate3dFigure(): Генерує 3D фігуру відповідно до вказаного типу.
        generate2dFigure(): Генерує 2D фігуру відповідно до вказаного типу.
        saveToFile2d(): Записує 2D фігуру в файл.
        saveToFile3d(): Записує 3D фігуру в файл.
        show_menu(): Виводить меню для взаємодії з інтерфейсом.
        loopMenu(): Запускає цикл взаємодії з інтерфейсом.
        launch(): Запускає інтерфейс.
    """
    def __init__(self):
        super().__init__()
        self.type = "cube"
        self.left_padding = 5
        self.top_padding = 5
        self.bottom_padding = 5
        self.commands = {
            1: Generate3DFigureCommand(self),
            2: SetSizeCommand(self, 0),
            3: SetColorCommand(self, "")
        }

    def setType(self, type):
        """Встановлює тип фігури."""
        self.type = type

    def setPaddings(self, left_padding, top_padding, bottom_padding):
        """Встановлює відступи фігури."""
        self.left_padding = left_padding
        self.top_padding = top_padding
        self.bottom_padding = bottom_padding

    def setPrimaryData(self):
        """Запитує користувача про основні дані фігури."""
        size = int(input("Розмір фігури: "))
        self.setSize(size)

        color = input(
            "Колір фігури (blue, green, red, magenta, yellow, white, cyan): ")
        self.setColor(color)

        type = input("Тип фігури (є тільки 'куб')(пропустити для типу за замовчуванням): ")
        if len(type):
            self.setType(type)

    def generateWithLeftPadding(self, text):
        """Генерує текст з лівим відступом."""
        lines = text.split('\n')
        padded_lines = [f"{' ' * self.left_padding}{line}" for line in lines]
        return '\n'.join(padded_lines)

    def generateWithTopPadding(self, text):
        """Генерує текст з верхнім відступом."""
        space = self.top_padding * '\n'
        padded_lines = space + text
        return padded_lines

    def generateWithBottomPadding(self, text):
        """Генерує текст з нижнім відступом."""
        space = self.bottom_padding * '\n'
        padded_lines = text + space
        return padded_lines

    def generateWithPaddings(self, text):
        """Генерує текст з врахуванням усіх відступів."""
        return self.generateWithBottomPadding(self.generateWithTopPadding(self.generateWithLeftPadding(text)))

    def generate3dFigure(self):
        """Генерує 3D фігуру відповідно до вказаного типу."""
        if self.type == 'куб':
            cube = Cube()
            cube.setSize(self.size)
            cube.setColor(self.color)
            return self.generateWithPaddings(cube.generateFigure())
        return super().generateFigure()

    def generate2dFigure(self):
        """Генерує 2D фігуру відповідно до вказаного типу."""
        if self.type == 'куб':
            square = Square()
            square.setSize(self.size)
            square.setColor(self.color)
            return self.generateWithPaddings(square.generateFigure())
        return super().generateFigure()

    def saveToFile2d(self):
        """Записує 2D фігуру в файл."""
        filename = input("Введіть ім'я файлу перед збереженням: ")
        textFileSaver(
            filename, self.generate2dFigure())

    def saveToFile3d(self):
        """Записує 3D фігуру в файл."""
        filename = input("Введіть ім'я файлу перед збереженням: ")
        textFileSaver(
            filename, self.generate3dFigure())

    @staticmethod
    def show_menu():
        """Виводить меню для взаємодії з інтерфейсом."""
        print("Виберіть пункт меню")
        print("1 - Згенерувати 3D фігуру")
        print("2 - Встановити розмір")
        print("3 - Встановити колір (blue, green, red, magenta, yellow, white, cyan)")
        print("4 - Встановити тип (куб)")
        print("5 - Встановити відступи")
        print("6 - Отримати 2D версію фігури")
        print("7 - Зберегти у файл (3D)")
        print("8 - Зберегти у файл (2D)")
        print("0 - Вихід")

    def loopMenu(self):
        """Запускає цикл взаємодії з інтерфейсом."""
        while True:
            self.show_menu()
            menu_choice = int(input("Ключ меню: "))
            if menu_choice == 1:
                print(self.generate3dFigure())
            elif menu_choice == 2:
                new_size = int(input("Введіть новий розмір: "))
                self.setSize(new_size)
            elif menu_choice == 3:
                new_color = input("Введіть новий колір: ")
                self.setColor(new_color)
            elif menu_choice == 4:
                new_type = input("Введіть новий тип: ")
                self.setType(new_type)
            elif menu_choice == 5:
                left_padding = int(input("Введіть лівий відступ: "))
                top_padding = int(input("Введіть верхній відступ: "))
                bottom_padding = int(input("Введіть нижній відступ: "))
                self.setPaddings(left_padding, top_padding, bottom_padding)
            elif menu_choice == 6:
                print(self.generate2dFigure())
            elif menu_choice == 7:
                self.saveToFile3d()
            elif menu_choice == 8:
                self.saveToFile2d()
            else:
                break

    def launch(self):
        """Запускає інтерфейс."""
        self.setPrimaryData()
        print(self.generate3dFigure())
        self.loopMenu()

def run_lab5():
    interface = FigureArtInterface()
    interface.launch()
    
if __name__ == "__main__":
    run_lab5()