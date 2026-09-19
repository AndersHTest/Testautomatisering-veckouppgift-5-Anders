Feature: Inventory_fail

  Scenario: Lägg till produkt i kundvagnen
    Given det finns produkter att lägga till_fail
    When jag lägger till en produkt i kundvagnen_fail
    Then ska kundvagnen uppdateras_fail


  Scenario: Det går att minska antalet av en specifik produkt
    Given det finns produkter att lägga till_fail
    When jag lägger till en produkt i kundvagnen_fail
    Then ska lagerhållningen uppdateras_fail