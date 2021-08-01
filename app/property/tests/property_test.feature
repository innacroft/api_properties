Feature: Property endpoint test
    Test property endpoint for getting properties by year, city and state or avaliable if not filter is given

Scenario: Search properties by year
    Given I create property with year "2000" city "Bogota" state "cundinamarca"
    And I call service with year "2000"
    Then Response status code is "200"

Scenario: Search properties by city
    Given I create property with year "2000" city "Bogota" state "cundinamarca"
    And I call service with city "Bogota"
    Then Response status code is "200"

Scenario: Search properties by state
    Given I create property with year "2000" city "Bogota" state "cundinamarca"
    And I call service with state "cundinamarca"
    Then Response status code is "200"