import unittest
from unittest.mock import patch
from unittest.mock import MagicMock, patch
from main import ApiClient
from io import StringIO
from main import ApiClient, UserInterface

class TestApiClient(unittest.TestCase):
    @patch('main.requests.get')
    def test_make_request_failure(self, mock_get):
        # Створення об'єкта MagicMock, який імітує властивість raise_for_status
        response_mock = MagicMock()
        response_mock.raise_for_status.side_effect = Exception("API error")

        # Налаштування поведінки MagicMock для об'єкта requests.get
        mock_get.return_value = response_mock

        # Створення об'єкта ApiClient та виклик методу, який викликає requests.get
        api_client = ApiClient(api_url='https://example.com')
        with self.assertRaises(Exception, msg="API error"):
            api_client.make_request('todos')

class TestUserInterface(unittest.TestCase):
    def test_add_new_todo(self):
        api_url = 'https://jsonplaceholder.typicode.com'
        api_client = ApiClient(api_url)
        interface = UserInterface(api_client)
        
        # Ми використовуємо unittest.mock.patch, щоб вказати введені дані для тестування.
        with patch('builtins.input', side_effect=['Test Todo', 'true']):
            # Викликаємо add_new_todo.
            interface.add_new_todo()
            
            # Перевіряємо, чи є нова справа у списку історії.
            self.assertEqual(interface.history[-1]['data']['title'], 'Test Todo')
            self.assertEqual(interface.history[-1]['data']['completed'], True)

    def test_display_menu(self):
        api_url = 'https://jsonplaceholder.typicode.com'
        api_client = ApiClient(api_url)
        interface = UserInterface(api_client)
        
        # Використовуємо unittest.mock.patch для тестування введення з клавіатури.
        with patch('builtins.input', return_value='1'):
            # Викликаємо display_menu та перевіряємо, чи виведено правильне меню.
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                interface.display_menu()
                self.assertEqual(mock_stdout.getvalue().strip(), 'Виберіть опцію:\n1. Переглянути список справ\n2. Зберегти дані\n3. Додати нову справу\nexit. Вийти з програми')

if __name__ == '__main__':
    unittest.main(exit=False)
