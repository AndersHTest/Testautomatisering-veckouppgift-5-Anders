from behave import *

@given(u'att jag har temperaturen 50 i Fahrenheit')
def step_impl(context):
    context.enhet = "f"
    context.temp = 50


@when(u'jag omvandlar temperaturen till Celsius')
def step_impl(context):
    context.result = (context.temp - 32) * 5 / 9


@then(u'ska resultatet vara 10.0 grader celsius')
def step_impl(context):
    assert context.result == 10.0