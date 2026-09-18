Feature: Bankkonto

  Scenario: skapa ett nytt konto
    Given ett nytt bankkonto
    When ett konto har skapats så är saldot 0
    Then verifiera att saldot är 0


  Scenario: sätta in pengar
    Given ett nytt bankkonto
    When pengar sätts in på kontot
    Then uppdateras balansen


  Scenario: ta ut pengar
    Given ett bankkonto med tillräckligt med pengar
    When pengar tas ut från kontot
    Then uppdateras balansen


  Scenario: applicera 5% ränta
    Given ett bankkonto med 1000 kr
    When applicerar 5% ränta
    Then balansen ökar med 5%


  Scenario: överföra pengar mellan två konton
    Given två konton med balans 1000 kr vardera
    When överför pengar från ena kontot till det andra
    Then uppdateras balansen på bådas bankkonton