from behave import *
from src.bibliotek.bibliotek import *
from src.bibliotek.bibliotek import Bibliotek


@given(u'att jag har ett bibliotek med minst en bok och en användare som heter Lisa')
def step_impl(context):
    anders_bibliotek = Bibliotek()
    context.bibliotek = anders_bibliotek

    anders_biografi = Book(1, "Anders", "Anders Biografi", 10)
    anders_bibliotek.add_book(anders_biografi)

    lisa = User(1, "Lisa")
    context.user = lisa


@when(u'jag registrerar henne på biblioteket')
def step_impl(context):
    context.bibliotek.register_user(context.user)
    context.result = context.bibliotek.users


@then(u'ska Lisa vara medlem på biblioteket')
def step_impl(context):
    assert context.user in context.result


@given(u'att det finns ett bibliotek med ett par böcker tillgängliga')
def step_impl(context):
    anders_bibliotek = Bibliotek()
    context.bibliotek = anders_bibliotek
    context.bok_1 = Book(1, "Anders", "Anders Biografi", 10)
    context.bok_2 = Book(2, "Andersson", "Titanic", 10)
    context.bibliotek.add_book(context.bok_1)
    context.bibliotek.add_book(context.bok_2)


@when(u'jag söker efter Titanic')
def step_impl(context):
    context.title = context.bok_2.title
    result = context.bibliotek.search_book_by_title(context.title)
    if result:
        for b in result:
            context.result = b.display_book_info()
    else:
        context.result = f"No books with title {context.title}"


@then(u'ska jag få information om boken finns tillgänglig')
def step_impl(context):
    assert context.result == "ID: 2, Title: Titanic, Author: Andersson, Available Quantity: 10"
