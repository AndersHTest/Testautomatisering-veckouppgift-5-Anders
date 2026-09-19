from src.lager.storage_fail import Stock, StockItem
from behave import given, when, then


@given(u'det finns produkter att lägga till_fail')
def step_impl_kundvagn_1(context):
    context.hammare = StockItem("Hammare", 10)
    context.skruvmejsel = StockItem("Skruvmejsel", 20)
    context.stock = Stock()


@when(u'jag lägger till en produkt i kundvagnen_fail')
def step_impl_kundvagn_2(context):
    context.stock.add_product(context.hammare)
    context.stock.add_product(context.skruvmejsel)
    context.stock.add_product_to_cart(context.hammare, 2)
    context.stock.add_product_to_cart(context.skruvmejsel, 3)
    context.kundvagn = context.stock.get_cart_items()
    context.hammare_lager = (context.stock.get_product_amount
                             (context.hammare.name))
    context.skruvmejsel_lager = (context.stock.get_product_amount
                                 (context.skruvmejsel.name))
    context.result_kundvagn = "Hammare: 2 stSkruvmejsel: 3 st"
    context.result_hammare = 8
    context.result_skruvmejsel = 17


@then(u'ska kundvagnen uppdateras_fail')
def step_impl_kundvagn_3(context):
    # print(context.kundvagn)
    # print(context.result_kundvagn)
    assert context.kundvagn == context.result_kundvagn


@then(u'ska lagerhållningen uppdateras_fail')
def step_impl_lager_1(context):
    assert context.result_hammare == context.hammare_lager
    assert context.result_skruvmejsel == context.skruvmejsel_lager
    assert True is not False
