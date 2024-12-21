from src.models import Library


def add_new_book(library: Library):
    """Функция для ввода данных для добавления новой книги"""

    title = input('Введите название книги: ')
    author = input('Введите автора книги: ').title()
    try:
        year = int(input('Введите год издания книги: '))
        library.add_book(title=title, author=author, year=year)
    except ValueError:
        print('Введен некорректный год. Введите число')
    print()


def delete_book_by_id(library: Library):
    """Функция для удаления книги по ID"""
    try:
        book_id = int(input('Введите ID книги, которую хотите удалить: '))
        library.delete_book(book_id=int(book_id))
    except ValueError:
        print('Введен некорректный ID. Введите число')


def search_book(library):
    """Функция для поиска книги по названию, автору или году издания"""

    print('По какому параметру вы хотели бы начать поиск:')
    print('1 - по названию книги')
    print('2 - по автору')
    print('3 - по году издания')

    search_parameter = input()

    if search_parameter == '1':
        title = input('Введите название книги: ').title()
        found_books = library.search_by_title(title)
        if found_books:
            print('Книги, найденные по вашему запросу:')
            for book in found_books:
                status = "в наличии" if book['status'] else "выдана"
                print(
                    f"Название - {book['title']}, автор - {book['author']}, год издания - {book['year']}, "
                    f"статус - {status}, ID книги - {book['book_id']}.")
        else:
            print('По вашему запросу книг не найдено')
    elif search_parameter == '2':
        author = input('Введите автора книги: ').title()
        found_books = library.search_by_title(author)
        if found_books:
            print('Книги, найденные по вашему запросу:')
            for book in found_books:
                status = "в наличии" if book['status'] else "выдана"
                print(
                    f"Автор - {book['author']}, название - {book['title']}, год издания - {book['year']}, "
                    f"статус - {status}, ID книги - {book['book_id']}.")
        else:
            print('По вашему запросу книг не найдено')
    elif search_parameter == '3':
        try:
            year = int(input('Введите год издания книги: '))
            found_books = library.search_by_title(year)
            if found_books:
                print('Книги, найденные по вашему запросу:')
                for book in found_books:
                    status = "в наличии" if book['status'] else "выдана"
                    print(
                        f"ID книги - {book['book_id']}, название - {book['title']}, автор - {book['author']}, "
                        f"год издания - {book['year']}, статус - {status}.")
            else:
                print('По вашему запросу книг не найдено')
        except ValueError:
            print('Введен некорректный год. Введите число')
    else:
        print('Нет такого параметра. Попробуйте ещё раз')
    print()


def display_all_books(library: Library):
    """Функция для вывода всех книг"""

    if library.get_all_books():
        print('Список всех книг:')
        for book in library.get_all_books():
            status = "в наличии" if book['status'] else "выдана"
            print(f"ID книги - {book['book_id']}, название - {book['title']}, автор - {book['author']}, "
                  f"год издания - {book['year']}, статус - {status}.")
    else:
        print('Книг в библиотеке не найдено')
    print()


def change_book_status(library):
    """Функция для изменения статуса книги"""

    try:
        book_id = int(input('Введите ID книги: '))
        new_status = input('Введите новый статус книги (выдана/в наличии): ')

        if new_status == 'выдана':
            new_status = False
            library.change_status(int(book_id), new_status)
        elif new_status == 'в наличии':
            new_status = True
            library.change_status(int(book_id), new_status)
        else:
            print('Нет такого статуса. Попробуйте ещё раз.')
    except ValueError:
        print('Введен некорректный ID. Введите число')
    print()
