
Feature: Add a project through settings

  Scenario: User can add a project through the settings
      Given Open the main page
      When Log in to the page
      And Click on the settings option
      And Click on Add a project
      Then Verify the Add Project page is displayed
      When Add some test information to the input fields
      Then Verify the right information is present in the input fields
      And Verify the “Send an application” button is available and clickable
