stadsbiblioteket = Bibliotek()

titanic = Book(1, "Andersson", "Titanic", 10)
stadsbiblioteket.add_book(titanic)

lisa = User(1, "Lisa") #Skapar en
stadsbiblioteket.register_user(lisa) # Registrerar lisa på biblioteket.
lisa.borrow_book(titanic) # Lisa lånar en bok.
titanic.display_book_info() # Det finns 9 titanic-böcker kvar.



#lisa.view_borrowed_books()