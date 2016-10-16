Feature: Assessment items

Scenario: The summariser correctly picks up the assessment name
    Given an assessment with the name "Assessment task 1: Comms Lab"
    When the assessment summariser sorts through the assessments
    Then this assessment name will be populated

Scenario: The summariser correctly picks up the assessment type
    Given an assessment with the name "Assessment task 1: Comms Lab"
    And the assessment has a type of "Lab"
    When the assessment summariser sorts through the assessments
    Then this assessment type will be populated

Scenario: The summariser correctly picks up the assessment weighting
    Given an assessment with the name "Assessment task 1: Comms Lab"
    And the assessment has a weighting of "40%"
    When the assessment summariser sorts through the assessments
    Then this assessment weighting will be populated

Scenario Outline: The summariser correctly picks up the assessment due date
    Given an assessment with the name "Assessment task 1: Comms Lab"
    And the assessment has a due date of "<due date>"
    When the assessment summariser sorts through the assessments
    Then this assessment due date will be populated

    Examples: Date Formats
    | due date               |
    | 24 Oct 16              |
    | Monday 24 October 2016 |
    | 24/10/16               |

Scenario: Assessment item in full
    Given an assessment with the name "Assessment task 2: Individual Project"
    And the assessment has a type of "Project"
    And the assessment has a weighting of "60%"
    And the assessment has a due date of "31 Oct 16"
    When the assessment summariser sorts through the assessments
    Then this assessment name will be populated
    And this assessment type will be populated
    And this assessment weighting will be populated
    And this assessment due date will be populated