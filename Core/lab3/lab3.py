import os
import pyfiglet
from termcolor import colored

def get_user_input():
    """Функція для отримання введення користувача."""
    user_input = input("Введіть слово або фразу, яку ви хочете перетворити в ASCII-арт: ")
    return user_input

def select_font():
    """Функція для вибору шрифту."""
    print("Доступні шрифти:")
    print("1. standard")
    print("2. slant")
    print("3. script")
    font_choice = input("Виберіть номер шрифту (1/2/3): ")

    fonts = ["standard", "slant", "script"]
    if font_choice in ['1', '2', '3']:
        return fonts[int(font_choice) - 1]
    else:
        print("Невірний вибір шрифту. Виберіть номер зі списку.")
        return select_font()

def select_color():
    """Функція для вибору кольору тексту."""
    print("Доступні кольори:")
    print("1. Червоний")
    print("2. Синій")
    print("3. Зелений")
    color_choice = input("Виберіть номер кольору (1/2/3): ")

    colors = ["red", "blue", "green"]
    if color_choice in ['1', '2', '3']:
        return colors[int(color_choice) - 1]
    else:
        print("Невірний вибір кольору. Виберіть номер зі списку.")
        return select_color()

def select_size():
    """Функція для вибору розміру ASCII-арту."""
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))
    return width, height

def select_characters():
    """Функція для вибору символів для ASCII-арту."""
    characters = input("Введіть символи, які ви хочете використовувати (наприклад, '@#$%'): ")
    return characters

def save_to_file(ascii_art):
    """Функція для збереження ASCII-арту у файл."""
    file_name = input("Введіть ім'я файлу для збереження (з розширенням .txt): ")

    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.dirname(current_directory)
    project_directory = os.path.dirname(parent_directory)
    data_directory = os.path.join(project_directory, 'Data')
    full_file_path = os.path.join(data_directory, file_name)

    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    try:
        with open(full_file_path, 'w', encoding='utf-8') as file:
            file.write(ascii_art)
        print(f"ASCII-арт збережено у файлі {full_file_path}")
    except FileNotFoundError as e:
        print(f"Файл не знайдено: {str(e)}")
    except PermissionError as e:
        print(f"Немає дозволу на запис у файл: {str(e)}")
    except Exception as e:
        print(f"Помилка при збереженні файлу: {str(e)}")





def format_output(ascii_art, width, height):
    """Функція для форматування виводу ASCII-арту."""
    lines = ascii_art.split('\n')
    formatted_art = []
    for line in lines:
        formatted_line = line.center(width)
        formatted_art.append(formatted_line)

    formatted_art = formatted_art[:height]

    return '\n'.join(formatted_art)

def preview_ascii_art(ascii_art):
    """Функція для попереднього перегляду ASCII-арту."""
    print("Попередній перегляд ASCII-арту:")
    print(ascii_art)

def run_lab3():
    """Основна функція для виконання завдань лабораторної роботи 3."""
    input_text = get_user_input()

    font = select_font()
    color = select_color()
    width, height = select_size()
    characters = select_characters()

    ascii_art = pyfiglet.figlet_format(input_text, font=font)

    for old_char, new_char in zip(ascii_art, characters):
        ascii_art = ascii_art.replace(old_char, new_char)

    formatted_ascii_art = format_output(ascii_art, width, height)

    colored_ascii_art = colored(formatted_ascii_art, color)

    preview_ascii_art(colored_ascii_art)

    save_choice = input("Зберегти ASCII-арт у файл? (так/ні): ")
    if save_choice.lower() == 'так':
        save_to_file(colored_ascii_art)

if __name__ == "__main__":
    run_lab3()