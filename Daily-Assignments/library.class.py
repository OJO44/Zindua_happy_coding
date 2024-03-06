class P_Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False 

    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}")
    
My_Book = P_Book("Learn Python", " Joseph", 1999)
print(My_Book.title)
print(My_Book.author)
print(My_Book.ISBN)