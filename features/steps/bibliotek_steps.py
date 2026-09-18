from behave import given, when, then
from src.bibliotek.bibliotek import Bibliotek, User, Book


# register user
@given(u'att jag har ett bibliotek med minst'
       u' en bok och en användare som heter Lisa')
def step_impl_bibliotek_register_user_1(context):
    anders_bibliotek = Bibliotek()
    context.bibliotek = anders_bibliotek

    anders_biografi = Book(1, "Anders", "Anders Biografi", 10)
    context.bok_1 = anders_biografi
    anders_bibliotek.add_book(context.bok_1)

    lisa = User(1, "Lisa")
    context.user = lisa


@when(u'jag registrerar henne på biblioteket')
def step_impl_bibliotek_register_user_2(context):
    context.bibliotek.register_user(context.user)
    context.result = context.bibliotek.users


@then(u'ska Lisa vara medlem på biblioteket')
def step_impl_bibliotek_register_user_3(context):
    assert context.user in context.result


# search book by title
@given(u'att det finns ett bibliotek med ett par böcker tillgängliga')
def step_impl_bibliotek_search_by_title_1(context):
    anders_bibliotek = Bibliotek()
    context.bibliotek = anders_bibliotek
    context.bok_1 = Book(1, "Anders", "Anders Biografi", 10)
    context.bok_2 = Book(2, "Andersson", "Titanic", 10)
    context.bibliotek.add_book(context.bok_1)
    context.bibliotek.add_book(context.bok_2)


@when(u'jag söker efter Titanic')
def step_impl_bibliotek_search_by_title_2(context):
    context.title = context.bok_2.title
    result = context.bibliotek.search_book_by_title(context.title)
    if result:
        for b in result:
            context.result = b.display_book_info()


@then(u'ska jag få information om boken finns tillgänglig')
def step_impl_bibliotek_search_by_title_3(context):
    assert context.result == ("ID: 2, Title: Titanic, "
                              "Author: Andersson, Available Quantity: 10")


# search book by author
@when(u'jag söker efter Andersson')
def step_impl_bibliotek_search_by_author_1(context):
    context.author = context.bok_2.author
    result = context.bibliotek.search_book_by_author(context.author)
    if result:
        for a in result:
            context.result = a.display_book_info()


# låna en bok
@when(u'jag registrerar henne på biblioteket och lånar en bok')
def step_impl_bibliotek_lana_en_bok_1(context):
    context.bibliotek.register_user(context.user)
    context.user.borrow_book(context.bok_1)
    context.borrowed_book = context.user.view_borrowed_books()


@then(u'blir boken registrerad på henne och lagerhållningen uppdateras')
def step_impl_bibliotek_lana_en_bok_2(context):
    assert context.bok_1.title in context.borrowed_book
    # Boken är registrerad på Lisa
    assert len(context.borrowed_book) == 1
    # Lisa har lånat 1 bok
    assert context.bok_1.quantity == 9
    # Lagerhållning uppdateras från 10 till 9.


# lämna tillbaka en bok
@given(u'att jag har ett bibliotek med minst en '
       u'bok och en registrerad användare som heter Lisa')
def step_impl_bibliotek_lamna_tillbaka_en_bok_1(context):
    anders_bibliotek = Bibliotek()
    context.bibliotek = anders_bibliotek

    anders_biografi = Book(1, "Anders", "Anders Biografi", 10)
    context.bok_1 = anders_biografi
    anders_bibliotek.add_book(context.bok_1)

    lisa = User(1, "Lisa")
    context.user = lisa

    context.bibliotek.register_user(context.user)
    context.user.borrow_book(context.bok_1)


@when(u'Lisa lämnar tillbaka boken')
def step_impl_bibliotek_lamna_tillbaka_en_bok_2(context):
    context.user.return_book(context.bok_1)
    context.borrowed_book = context.user.view_borrowed_books()


@then(u'Lisa har 0 böcker lånade och lagerhållningen är uppdaterad')
def step_impl_bibliotek_lana_en_bok_3(context):
    assert context.bok_1.title not in context.borrowed_book
    assert len(context.borrowed_book) == 0
    assert context.bok_1.quantity == 10
