from behave import *
from src.temperatur.omvandling import temperaturomvandling


@given(u'att jag har temperaturen 50 i enheten Fahrenheit')
def step_impl(context):
    context.enhet_f = "f"
    context.temp_f = 50


@when(u'jag omvandlar temperaturen till Celsius')
def step_impl(context):
    omvandling = temperaturomvandling(context.enhet_f, context.temp_f)
    context.result = omvandling


@then(u'ska resultatet vara 10.0 grader celsius')
def step_impl(context):
    assert context.result == 10.0


@given(u'att jag har temperaturen 10 i enheten Celsius')
def step_impl(context):
    context.enhet_c = "c"
    context.temp_c = 10


@when(u'jag omvandlar temperaturen till Fahrenheit')
def step_impl(context):
    omvandling = temperaturomvandling(context.enhet_c, context.temp_c)
    context.result = omvandling


@then(u'ska resultatet vara 50.0 grader Fahrenheit')
def step_impl(context):
    assert context.result == 50.0
