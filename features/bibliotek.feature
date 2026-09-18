Feature: Bibliotek

  Scenario: Registrera användare på biblioteket
    Given att jag har ett bibliotek med minst en bok och en användare som heter Lisa
    When jag registrerar henne på biblioteket
    Then ska Lisa vara medlem på biblioteket


  Scenario: söka efter böcker baserat på titel
    Given att det finns ett bibliotek med ett par böcker tillgängliga
    When jag söker efter Titanic
    Then ska jag få information om boken finns tillgänglig


  Scenario: söka efter böcker baserat på författare
    Given att det finns ett bibliotek med ett par böcker tillgängliga
    When jag söker efter Andersson
    Then ska jag få information om boken finns tillgänglig