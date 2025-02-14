class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        """Display the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print()

book1 = Book("A Tale of Two Cities", "Charles Dickens", 1859)

book1.describe()

