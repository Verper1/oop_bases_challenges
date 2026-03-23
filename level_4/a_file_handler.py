"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json
from pprint import pprint


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r') as file:
            return json.load(file)


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)


if __name__ == '__main__':
    file_handler = FileHandler("data\\text.txt")
    print("FileHandler")
    print(file_handler.read(), "\n", "-----")

    json_handler = JSONHandler("data\\recipes.json")
    (print("JSONHandler"))
    print(json.dumps(json_handler.read(), indent=4, ensure_ascii=False), "\n", "-----")

    csv_handler = CSVHandler("data\\user_info.csv")
    (print("CSVHandler"))
    pprint(csv_handler.read())
