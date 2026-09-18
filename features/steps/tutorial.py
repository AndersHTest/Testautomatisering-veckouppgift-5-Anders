from behave import given, when, then


@given('we have behave installed')
def step_impl_tutorial_1(context):
    pass


@when('we implement a test')
def step_impl_tutorial_2(context):
    assert True is not False


@then('behave will test it for us!')
def step_impl_tutorial_3(context):
    assert context.failed is False
