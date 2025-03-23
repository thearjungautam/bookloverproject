import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book_lover = BookLover("Bob", "bob@email.com", "fiction")
        book_lover.add_book("The Giver", 4)
        self.assertTrue("The Giver" in book_lover.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book_lover = BookLover("Bob", "bob@email.com", "fiction")
        book_lover.add_book("The Giver", 7)
        book_lover.add_book("The Giver", 7)
        count = book_lover.book_list['book_name'].tolist().count("The Giver")
        self.assertEqual(count,1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_lover = BookLover("Bob", "bob@email.com", "fiction")
        book_lover.add_book("Dracula", 5)
        self.assertTrue(book_lover.has_read("Dracula"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_lover = BookLover("Bob", "bob@email.com", "fiction")
        self.assertFalse(book_lover.has_read("Divergent"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book_lover = BookLover("Bob", "bob@email.com", "fiction")
        book_lover.add_book("The Giver", 3)
        book_lover.add_book("Dracula", 4)
        book_lover.add_book("Othello", 5)
        self.assertEqual(book_lover.num_books_read(), 3)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book_lover = BookLover("Bob", "bob@email.com", "fiction")
        book_lover.add_book("The Giver", 4)
        book_lover.add_book("Dracula", 5)
        book_lover.add_book("Othello", 2)
        fav_books = book_lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
        
if __name__ == '__main__':
    unittest.main(verbosity=3)