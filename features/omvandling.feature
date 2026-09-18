Feature: enkel temperaturomvandlare

  Scenario: Omvandla temperatur från F till C
    Given att jag har temperaturen 50 i Fahrenheit
    When jag omvandlar temperaturen till Celsius
    Then ska resultatet vara 10.0 grader celsius
