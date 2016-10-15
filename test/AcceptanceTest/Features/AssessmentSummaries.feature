Feature: Assessment items

Background: Setup assessment
    Given an assessment with the name "Assessment task 1: Comms Lab"

Scenario: The summariser correctly picks up the assessment name
    When the assessment summariser sorts through the assessments
    Then this assessment name will be populated

Scenario: The summariser correctly picks up the assessment type
    Given the assessment has a type of "Lab"
    When the assessment summariser sorts through the assessments
    Then this assessment type will be populated

Scenario: The summariser correctly picks up the assessment weighting
    Given the assessment has a weighting of "40%"
    When the assessment summariser sorts through the assessments
    Then this assessment weighting will be populated

Scenario Outline: The summariser correctly picks up the assessment due date
    Given the assessment has a due date of "<due date>"
    When the assessment summariser sorts through the assessments
    Then this assessment due date will be populated

    Examples: Date Formats
    | due date               |
    | 24 Oct 16              |
    | Monday 24 October 2016 |
    | 24/10/16               |