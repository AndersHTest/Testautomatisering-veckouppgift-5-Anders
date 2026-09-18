from behave import given, when, then
from src.bank.bankkonto import BankKonto, Logger, Transaction


@given(u'ett nytt bankkonto')
def step_impl_skapa_bankkonto_1(context):
    context.logger = Logger()
    anders_konto = BankKonto(context.logger)
    context.konto = anders_konto


@when(u'ett konto har skapats så är saldot 0')
def step_impl_skapa_bankkonto_2(context):
    context.result = context.konto.balance


@then(u'verifiera att saldot är 0')
def step_impl_skapa_bankkonto_3(context):
    assert context.result == 0


@when(u'pengar sätts in på kontot')
def step_impl_deposit_1(context):
    context.amount = 500
    context.konto.deposit(context.amount)
    context.result = context.konto.balance


@then(u'uppdateras balansen')
def step_impl_deposit_2(context):
    assert context.result == context.amount


@given(u'ett bankkonto med tillräckligt med pengar')
def step_impl_withdraw_1(context):
    context.logger = Logger()
    anders_konto = BankKonto(context.logger)
    context.konto = anders_konto
    context.amount = 500
    context.konto.deposit(context.amount)
    context.x = context.konto.balance


@when(u'pengar tas ut från kontot')
def step_impl_withdraw_2(context):
    context.konto.withdraw(context.amount)
    context.amount = context.x - context.amount
    context.result = context.konto.balance


@given(u'ett bankkonto med 1000 kr')
def step_impl_add_interest_1(context):
    context.logger = Logger()
    anders_konto = BankKonto(context.logger)
    context.konto = anders_konto
    context.amount = 1000
    context.konto.deposit(context.amount)
    context.x = context.konto.balance  # sparar nuvarande balans i en variabel


@when(u'applicerar 5% ränta')
def step_impl_add_interest_2(context):
    context.konto.interest()
    # applicerar 5% ränta
    context.result = context.x * 1.05
    # ökar den tidigare balansen med 5%


@then(u'balansen ökar med 5%')
def step_impl_add_interest_3(context):
    assert context.result == context.konto.balance
    # Verifierar att kontot har samma belopp som context.x


@given(u'två konton med balans 1000 kr vardera')
def step_impl_transaction_1(context):
    context.logger = Logger()
    anders_konto = BankKonto(context.logger)
    lisas_konto = BankKonto(context.logger)
    context.konto_1 = anders_konto
    context.konto_2 = lisas_konto
    context.amount_1 = 1000
    context.amount_2 = 500
    context.konto_1.deposit(context.amount_1)
    context.konto_2.deposit(context.amount_1)
    context.x_1 = context.konto_1.balance
    context.x_2 = context.konto_2.balance
    # vi sparar den ursprungliga balansen i en variabel


@when(u'överför pengar från ena kontot till det andra')
def step_impl_transaction_2(context):
    t = Transaction()
    t.transfer(context.amount_2, context.konto_1, context.konto_2)
    context.result_1 = context.konto_1.balance
    context.result_2 = context.konto_2.balance
    # vi sparar balansen efter transaktionen i en variabel


@then(u'uppdateras balansen på bådas bankkonton')
def step_impl_transaction_3(context):
    assert context.result_1 == context.x_1 - context.amount_2
    assert context.result_2 == context.x_2 + context.amount_2
    # vi jämför balansen före och efter transaktionen
