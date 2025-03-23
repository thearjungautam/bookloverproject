import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books = 0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating':[]})
        
    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].values:
            return False
        
        new_book= pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1
        return True
        
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == '__main__':
    test_object = BookLover("Joe", "joe@email.com", "fiction")
    test_object.add_book("Hunger Games", 4)
    test_object.add_book("Frankenstein", 5)
    test_object.add_book("Animal Farm", 3)
    print(test_object.book_list)