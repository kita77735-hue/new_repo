from book import Book

library = [
    Book("bible", "God"),
    Book("lotr", "tolkien"),
    Book("mao", "china")
    ]

for book in library:
    print(f"{book.title} - {book.autor}")