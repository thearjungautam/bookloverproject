from booklover.booklover import BookLover

bl = BookLover("Jim", "bob@email.com", "fiction")
bl.add_book("Dune", 5)

print(bl.name)              
print(bl.has_read("Dune"))
print(bl.book_list)
 