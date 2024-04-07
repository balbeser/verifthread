class MenuKeyboard:
    list_books: str = "📋 Список книг"
    search_book: str = "🔍 Поиск книги"
    add_book: str = "➕ Добавить книгу"

    back = "⬅️ Назад"
    add_custom = "➕ Добавить свой"

    adjust = [2]


class StartText:
    welcome_message = "Привет!"


class AddBookText:
    enter_book_name = (
        "Введите название книги:\n\n(Дубли отключены, есть проверка на них)"
    )
    enter_book_author = "Введите автора книги:"
    enter_book_description = "Введите описание книги:"
    select_genre_or_create_new = "Выберите жанр книги или создайте новый:"


class AddBookExceptions:
    error_book_alredy_exists = "Ошибка! Такая книга уже существует!"


class AddGenreText:
    enter_custom_genre = "Введите свой жанр:"


class BookInfoText:
    book_info_format = "Информация о книге:\n\nНазвание: {name}\n\nЖанр: {genre}\nАвтор: {author}\nОписание: {description}"


class BookDeleteText:
    book_delete_format = "Книга: {name} успешно удалена!"


class ListBooksText:
    list_books = "Список книг:"
    list_books_by_genre = "Книги с жанром: {genre}"


class SearchBooksText:
    select_search_type = "Выберите тип поиска:"
    enter_search_phrase = "Напишите фразу для поиска:"
    enter_search_genre = "Выберите жанр для поиска:"
