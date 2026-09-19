from behave import given, when, then
from src.lager.storage import Stock, StockItem


@given (u'det finns produkter att lägga till')
def step_impl_add_products_1(context):
    stock = Stock()
    context.stock = stock
    context.hammare = StockItem("Hammare", 20)
    context.skruvmejsel = StockItem("Skruvmejsel", 30)


@when(u'jag lägger till en produkt')
def step_impl_add_products_2(context):
    context.stock.add_product(context.hammare)
    context.stock.add_product(context.skruvmejsel)


@then(u'ska namn och antal vara korrekt')
def step_impl_add_products_3(context):
    context.result = "[Hammare: 20, Skruvmejsel: 30]"
    assert context.result == str(context.stock.get_items())
    #print(f"result = {context.result}, get = {str(context.stock.get_items())}")


@given(u'produkter är tillagda')
def step_impl_remove_products_1(context):
    stock = Stock()
    context.stock = stock
    context.hammare = StockItem("Hammare", 20)
    context.skruvmejsel = StockItem("Skruvmejsel", 30)
    context.stock.add_product(context.hammare)
    context.stock.add_product(context.skruvmejsel)


@when(u'jag tar bort x antal av en produkt')
def step_impl_remove_products_2(context):
    context.stock.remove_product(context.hammare, 4)
    context.result = "[Hammare: 16, Skruvmejsel: 30]"


@then(u'ska lagerhållningen uppdateras')
def step_impl_add_products_3(context):
    print(f"get = {context.stock.get_items()}")
    assert context.result == str(context.stock.get_items())
