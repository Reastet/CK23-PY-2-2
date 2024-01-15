BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, **arguments):
        if 'id_' in arguments.keys():
            self.id = arguments['id_'];
        if 'name' in arguments.keys():
            self.name = arguments['name'];
        if 'pages' in arguments.keys():
            self.pages = arguments['pages'];

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self)->str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    list_of_books = []
    def __init__(self, **arg):
        if 'books' in arg.keys():
            for i in arg['books']:
                self.list_of_books.append(i)

    @classmethod
    def get_next_book_id(cls):
        a = len(cls.list_of_books)
        if a == 0:
            return 1
        return cls.list_of_books[a-1].id+1

    @classmethod
    def get_index_by_book_id(cls,id):
        for i in range(len(cls.list_of_books)):
            if cls.list_of_books[i].id==id:
                return i
        ValueError("Книга с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
