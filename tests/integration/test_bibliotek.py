import pytest
from src.bibliotek.bibliotek import User, Bibliotek, Book


@pytest.mark.integration
def test_register_user():
    stadsbiblioteket = Bibliotek()

    titanic = Book(1, "Andersson", "Titanic", 10)
    stadsbiblioteket.add_book(titanic)

    lisa = User(1, "Lisa")  # Skapar en användare. Lisa.
    stadsbiblioteket.register_user(lisa)  # Registrerar Lisa på biblioteket.

    assert lisa in stadsbiblioteket.users


@pytest.mark.integration
def test_borrow_book():
    stadsbiblioteket = Bibliotek()
    titanic = Book(1, "Andersson", "Titanic", 10)
    stadsbiblioteket.add_book(titanic)
    lisa = User(1, "Lisa")  # Skapar en användare. Lisa.
    stadsbiblioteket.register_user(lisa)  # Registrerar Lisa på biblioteket.
    lisa.borrow_book(titanic)  # Lisa lånar en bok.
    b = 9  # Förväntat antal böcker tillgängliga

    assert titanic.quantity == b  # Kontrollerar att det finns
    # 9 Titanic-böcker kvar att låna.
    assert titanic in lisa.borrowed_books  # Kontrollera att Lisa
    # har lånat en kopia av Titanic.


@pytest.mark.integration
def test_return_book():
    stadsbiblioteket = Bibliotek()
    titanic = Book(1, "Andersson", "Titanic", 10)
    stadsbiblioteket.add_book(titanic)
    lisa = User(1, "Lisa")  # Skapar en användare. Lisa.
    stadsbiblioteket.register_user(lisa)  # Registrerar Lisa på biblioteket.
    lisa.borrow_book(titanic)  # Lisa lånar Titanic.
    lisa.return_book(titanic)  # Lisa returnerar Titanic.

    b = 10  # Förväntat antal böcker tillgängliga.

    assert titanic.quantity == b
    assert titanic not in lisa.borrowed_books
