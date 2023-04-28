Feature: Verify correct search results are shown when sliding filters

  Scenario: CAP224 - When sliding filters correct number of products are shown
    Given Open Cureskin page
    When Clicking on Shop All section
    And Adjusting the Price Filter
    Then Verify that products displayed are within the Price filter