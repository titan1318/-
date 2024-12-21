from src.models import Library
from src.utils import delete_book_by_id, search_book, display_all_books, change_book_status, add_new_book


def main():
    library = Library()

    while True:
        print("Введите число для управления библиотекой:")
        print("1 - добавить книгу")
        print("2 - удалить книгу")
        print("3 - найти книгу")
        print("4 - показать все книги")
        print("5 - изменить статус книги")
        print("6 - выйти из программы")

        answer = input()

        if answer == '1':
            add_new_book(library)
        elif answer == '2':
            delete_book_by_id(library)
        elif answer == '3':
            search_book(library)
        elif answer == '4':
            display_all_books(library)
        elif answer == '5':
            change_book_status(library)
        elif answer == '6':
            break
        else:
            print('Такой опции нет, выберите один из предложенных вариантов')


if __name__ == "__main__":
    main()
