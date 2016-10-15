from behave import given, when, then
import sys
sys.path.append("../../")

from Parser.AssessmentItems import AssessmentTask, DueDate

def assertEqual(actual, expected):
    assert actual == expected, "Expected: %s, Actual Val: %s" % (expected, actual)

@given('an assessment with the name "{AssessmentName}"')
def construct_assessment_data_item(context, AssessmentName):
    context.assessment_array = []
    context.assessment_name = str(AssessmentName)
    context.assessment_array.append(context.assessment_name)
    pass

@given('the assessment has a type of "{Type}"')
def add_type_to_data_item(context, Type):
    context.assessment_type = str(Type)
    context.assessment_array.append("Type: ")
    context.assessment_array.append(context.assessment_type)
    pass

@given('the assessment has a weighting of "{Weighting}"')
def add_weighting_to_data_item(context, Weighting):
    context.assessment_weighting = str(Weighting)
    context.assessment_array.append("Weight: ")
    context.assessment_array.append(context.assessment_weighting)
    pass

@given('the assessment has a due date of "{DueDate}"')
def add_weighting_to_data_item(context, DueDate):
    context.assessment_due_date = str(DueDate)
    context.assessment_array.append("Due: ")
    context.assessment_array.append(context.assessment_due_date)
    pass

@when('the assessment summariser sorts through the assessments')
def summarise_the_subject(context):
    context.program_start = '01 Aug'
    context.summary = AssessmentTask(context.assessment_array, 0, len(context.assessment_array), context.program_start)
    pass

@then('this assessment name will be populated')
def check_assessment_name(context):
    assertEqual(context.summary.TaskName, context.assessment_name)

@then('this assessment type will be populated')
def check_assessment_type(context):
    assertEqual(context.summary.TaskType, context.assessment_type)

@then('this assessment weighting will be populated')
def check_assessment_weighting(context):
    assertEqual(context.summary.Weighting, context.assessment_weighting)

@then('this assessment due date will be populated')
def check_assessment_due_date(context):
    DueDateTester = DueDate(context.assessment_array, 0, context.program_start)
    DueDateTester._is_time_format(context.assessment_due_date)
    _time_to_compare = DueDateTester._convert_date(context.assessment_due_date)
    assertEqual(context.summary.DueDate, _time_to_compare)