Feature: enkel temperaturomvandlare

  Scenario: Omvandla temperatur från F till C
    Given att jag har temperaturen 50 i enheten Fahrenheit
    When jag omvandlar temperaturen till Celsius
    Then ska resultatet vara 10.0 grader celsius


  Scenario: Omvandla temperatur från C till F
    Given att jag har temperaturen 10 i enheten Celsius
    When jag omvandlar temperaturen till Fahrenheit
    Then ska resultatet vara 50.0 grader Fahrenheit
