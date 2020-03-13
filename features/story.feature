Feature: showing off behave

Scenario: Run a simple test
    Given I am in Youtube home page
    When I want to search for "Ivan Tay Selenium Automation"
    and Select the second search video
    Then The selected video will play on
