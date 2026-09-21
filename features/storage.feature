#noinspection CucumberUndefinedStep
Feature: Inventory

  Scenario: Lägg till produkt
    Given det finns produkter att lägga till
    When jag lägger till en produkt
    Then ska namn och antal vara korrekt


  Scenario: Det går att minska antalet av en specifik produkt
    Given produkter är tillagda
    When jag tar bort x antal av en produkt
    Then ska lagerhållningen uppdateras