import json
import os.path


class Book:
    """Класс для представления книг"""

    book_id: int
    title: str
    author: str
    year: int
    status: bool

    def __init__(self, book_id: int, title: str, author: str, year: int):
        """Инициализатор для экземпляра класса Book"""

        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = True


class Library:
    """Класс для управления библиотекой книг"""

    books: list
    file: str

    def __init__(self, file_for_data: str = 'books.json'):
        """Инициализатор для экземпляра класса Library"""

        self.file_for_data = file_for_data
        self.books = self.load_data()

    def generate_book_id(self) -> int:
        """Метод, генерирующий уникальный идентификатор книги"""

        return max((book['book_id'] for book in self.books), default=0) + 1

    def add_book(self, title: str, author: str, year: int):
        """Метод для создания и добавления книги"""

        book_id = self.generate_book_id()
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book.__dict__)
        self.save_data()

        print(f'Книга - "{new_book.title}", автор - {new_book.author} добавлена в библиотеку c ID {new_book.book_id}.')

    def get_all_books(self):
        """Метод для вывода всех книг"""

        return self.books

    def delete_book(self, book_id: int):
        """Метод для удаления книги по ID"""

        book_to_delete = next((book for book in self.books if book['book_id'] == book_id), None)
        if book_to_delete:
            self.books.remove(book_to_delete)
            print(f'Книга "{book_to_delete["title"]}" с ID {book_id} удалена из библиотеки')
            self.save_data()
        else:
            print(f'Книга с ID {book_id} не найдена')
        print()

    def change_status(self, book_id: int, new_status: bool):
        """Метод для смены статуса книги по ID"""

        book_to_change_status = next((book for book in self.books if book['book_id'] == book_id), None)
        if book_to_change_status:
            if book_to_change_status['status'] == new_status:
                print('Статус книги соответствовал новому статусу')
                print()
            else:
                book_to_change_status['status'] = new_status
                status = "в наличии" if book_to_change_status['status'] else "выдана"
                print(f'Статус книги "{book_to_change_status["title"]}" изменен на "{status}".')
                print()
            self.save_data()
        else:
            print(f'Книга с ID {book_id} не найдена')
            print()

    def search_by_title(self, title: str):
        """Метод, осуществляющий поиск книг по названию"""

        books_by_title = [book for book in self.books if book['title'] == title]
        return books_by_title

    def search_by_author(self, author: str):
        """Метод, осуществляющий поиск книг по автору"""

        books_by_author = [book for book in self.books if book['author'] == author]
        return books_by_author

    def search_by_year(self, year: int):
        """Метод, осуществляющий поиск книг по году"""

        books_by_year = [book for book in self.books if book['year'] == year]
        return books_by_year

    def save_data(self):
        """Метод, записывающий данные в json-файл"""

        with open(self.file_for_data, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, ensure_ascii=False)

    def load_data(self, ):
        """Метод, считывающий данные из json-файла"""

        if os.path.exists(self.file_for_data):
            with open(self.file_for_data, 'r', encoding='utf-8') as file:
                load_books = json.load(file)
            return load_books
        else:
            return []
