from behave import given, when, then
from src.temperatur.omvandling import temperaturomvandling


@given(u'att jag har temperaturen 50 i enheten Fahrenheit')
def step_impl_omvandling_f_c_1(context):
    context.enhet_f = "f"
    context.temp_f = 50


@when(u'jag omvandlar temperaturen till Celsius')
def step_impl_omvandling_f_c_2(context):
    omvandling = temperaturomvandling(context.enhet_f, context.temp_f)
    context.result = omvandling


@then(u'ska resultatet vara 10.0 grader celsius')
def step_impl_omvandling_f_c_3(context):
    assert context.result == 10.0


@given(u'att jag har temperaturen 10 i enheten Celsius')
def step_impl_omvandling_c_f_1(context):
    context.enhet_c = "c"
    context.temp_c = 10


@when(u'jag omvandlar temperaturen till Fahrenheit')
def step_impl_omvandling_c_f_2(context):
    omvandling = temperaturomvandling(context.enhet_c, context.temp_c)
    context.result = omvandling


@then(u'ska resultatet vara 50.0 grader Fahrenheit')
def step_impl_omvandling_c_f_3(context):
    assert context.result == 50.0
