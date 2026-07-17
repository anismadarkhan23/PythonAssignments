class BookStore:
    no_of_books = 0

    def __init__(self, name, author):
        self.book_name = name
        self.book_author = author
        BookStore.no_of_books += 1

    def display_book_details(self):
        print(f"{self.book_name} by {self.book_author}. No. of Books: {BookStore.no_of_books}")

bs_obj1 = BookStore("Linux System Programming", "Robert Love")
bs_obj1.display_book_details()

bs_obj2 = BookStore("C Programming", "Dennis Ritchie")
bs_obj2.display_book_details()

bs_obj3 = BookStore("Automate the Boring Stuff with Python", "Al Sweigart")
bs_obj3.display_book_details()

bs_obj4 = BookStore("The Clean Code", "Robert C. Martin")
bs_obj4.display_book_details()

bs_obj5 = BookStore("Python Essentials", "Shawn Peters")
bs_obj5.display_book_details()