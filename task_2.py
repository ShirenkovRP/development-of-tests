# Проверим правильность работы Яндекс.Диск REST API. Написать тесты,
# проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и
# возможные отрицательные тесты на ответы с ошибкой

import unittest
import api_yandex as ay


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_requests_put(self):
        print("создание папки")
        if ay.result.status_code != 409:
            self.assertEqual(ay.result.status_code, 201)
        else:
            self.assertEqual(ay.result.status_code, 409)
            print("папка с таким именем существует")

    def test_add_folder(self):
        print("папка появилась в списке файлов")
        self.assertEqual(ay.result_get.status_code, 200)


if __name__ == '__main__':
    unittest.main()
