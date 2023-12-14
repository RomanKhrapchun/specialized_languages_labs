import requests
import json
import pandas as pd
import logging
from prettytable import PrettyTable
import os

logging.basicConfig(filename='api_client.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


class FileStorage:
    @staticmethod
    def store_data(data, file_format):
        """
        Зберігає дані у вказаному форматі у папці Data на одному рівні з Core.

        Parameters:
            data (list): Дані для збереження.
            file_format (str): Формат збереження ('json', 'csv', 'txt').
        """
        # Отримуємо шлях до файлу, який виконується
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Виходимо на один рівень вгору, щоб потім зайти в папку Data
        base_dir = os.path.dirname(current_dir)
        data_dir = os.path.join(base_dir, 'Data')

        # Створюємо шлях до файлу у папці Data
        filename = f'saved_data.{file_format}'
        file_path = os.path.join(data_dir, filename)

        # Зберігаємо дані в зазначеному форматі
        if file_format == 'json':
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        elif file_format == 'csv':
            dataframe = pd.DataFrame(data)
            dataframe.to_csv(file_path, index=False)
        elif file_format == 'txt':
            with open(file_path, 'w') as file:
                file.write(str(data))
        print(f"Дані збережено у файлі: {file_path}")


class ApiClient:
    def __init__(self, api_url):
        """
        Ініціалізація об'єкта ApiClient.

        Parameters:
            api_url (str): URL API-провайдера.

        """
        self.api_url = api_url

    def make_request(self, endpoint, params=None):
        """
        Виконує HTTP GET-запит до API.

        Parameters:
            endpoint (str): Ім'я ендпоінта API.
            params (dict): Параметри запиту.

        Returns:
            dict or None: Результат запиту або None у випадку помилки.

        """
        try:
            headers = {'Accept': 'application/json'}
            response = requests.get(f'{self.api_url}/{endpoint}', headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            logging.error(f'Помилка виклику API: {err}')
            return None

    def add_todo(self, todo_data):
        """
        Додає новий елемент справи до API.

        Parameters:
            todo_data (dict): Дані нової справи.

        Returns:
            dict or None: Результат запиту або None у випадку помилки.

        """
        try:
            endpoint = 'todos'
            headers = {'Content-Type': 'application/json'}
            response = requests.post(f'{self.api_url}/{endpoint}', headers=headers, json=todo_data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as err:
            logging.error(f'Помилка виклику API: {err}')
            return None


class UserInterface:
    def __init__(self, api_client):
        """
        Ініціалізація об'єкта UserInterface.

        Parameters:
            api_client (ApiClient): Об'єкт для взаємодії з API.

        """
        self.api_client = api_client
        self.history = []

    def display_data(self, data):
        """
        Виводить дані у форматі PrettyTable.

        Parameters:
            data (list): Список об'єктів для виведення.

        """
        if data:
            headers = data[0].keys()
            rows = [d.values() for d in data]
            table = PrettyTable()
            table.field_names = headers
            table.add_rows(rows)
            print(table)
        else:
            print('Немає даних для відображення.')

    def display_menu(self):
        """
        Виводить меню та отримує вибір користувача.

        Returns:
            str: Вибір користувача.

        """
        print("Виберіть опцію:")
        print("1. Переглянути список справ")
        print("2. Зберегти дані")
        print("3. Додати нову справу")
        print("exit. Вийти з програми")

        user_input = input('Введіть свій вибір: ')
        return user_input

    def process_command(self, command):
        """
        Обробляє команди користувача.

        Parameters:
            command (str): Команда користувача.

        """
        try:
            if command == '1':
                endpoint = 'todos'
                params = None
                api_response = self.api_client.make_request(endpoint, params)
                self.history.append({'command': command, 'data': api_response})
                self.display_data(api_response)
            elif command == '2':
                if self.history:
                    last_response = self.history[-1]['data']
                    self.save_data(last_response, 'json')
                    self.save_data(last_response, 'csv')
                    self.save_data(last_response, 'txt')
                    print("Дані успішно збережено.")
                else:
                    print("Немає даних для збереження.")
            elif command == '3':
                self.add_new_todo()
            elif command.lower() == 'exit':
                print("Вихід з програми.")
            else:
                print('Невірна команда. Будь ласка, введіть правильний номер опції або "exit".')
        except Exception as e:
            logging.error(f'Помилка обробки команди {command}: {e}')

    def add_new_todo(self):
        """
        Додає нову справу.

        """
        title = input('Введіть назву нової справи: ')
        completed = input('Чи завершена справа? (True/False): ').lower() == 'true'

        new_todo = {'userId': 1, 'title': title, 'completed': completed}
        self.history.append({'command': 'add_todo', 'data': new_todo})
        print('Нову справу успішно додано.')

    def save_data(self, data, file_format):
        """
        Зберігає дані у вказаному форматі.

        Parameters:
            data (list): Дані для збереження.
            file_format (str): Формат збереження ('json', 'csv', 'txt').

        """
        FileStorage.store_data(data, file_format)

    def run(self):
        """
        Запускає інтерфейс користувача.

        """
        while True:
            command = self.display_menu()
            if command.lower() == 'exit':
                break
            self.process_command(command)


def run_lab7():
    api_url = 'https://jsonplaceholder.typicode.com'
    api_client = ApiClient(api_url)
    interface = UserInterface(api_client)
    interface.run()


if __name__ == '__main__':
    run_lab7()
