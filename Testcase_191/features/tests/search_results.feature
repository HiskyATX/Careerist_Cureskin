
Feature: Verify correct search results are shown
  # Enter feature description here

  Scenario: Verify that 23 products are returned for Cure search

    Given Open page at Cure keyword
    Then Verify search has 23 item(s)

