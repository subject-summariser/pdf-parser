import argparse
import sys, os
from Parser.Summary import Summary

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

def PrintSubItem(Type, Value):
    if Value == "":
        print Type + ": " + "Could not find field"
        return
    print Type + ": " + Value

def PrintSummary(NewSummary):
    PrintSubItem("Subject", NewSummary.subject_name)

    for assessment in NewSummary.assessments:
        PrintSubItem("Task", assessment.TaskName)
        PrintSubItem("Type", assessment.TaskType)
        PrintSubItem("Weight", assessment.Weighting)
        PrintSubItem("Due", assessment.DueDate)
        PrintSubItem("Group", assessment.GroupWork)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "File Path")
    parser.add_argument("--path")
    ExitCodes = enum('OK', 'UNDEFINED', 'MISSING_PATH', 'PATH_NOT_FOUND', 'GENERATION_FAILED', 'NOT_IMPLEMENTED', 'PARSE_ERROR', 'ARGUMENT_ERROR')

    exit_code = ExitCodes.UNDEFINED
    
    try:
        args = parser.parse_args()
    except:
        exit_code = ExitCodes.ARGUMENT_ERROR

    if args.path:
        if not os.path.exists(args.path):
            exit_code = ExitCodes.PATH_NOT_FOUND
        else:
            print args.path
            
            try:
                NewSummary = Summary(args.path)
                PrintSummary(NewSummary)
                exit_code = ExitCodes.OK
            except Exception as e:
                if (isinstance(e, NotImplementedError)):
                    exit_code = ExitCodes.NOT_IMPLEMENTED
                elif "Parse" in e.message:
                    exit_code = ExitCodes.PARSE_ERROR
                else:
                    print e.message
                    exit_code = ExitCodes.GENERATION_FAILED
    else:
        exit_code = ExitCodes.MISSING_PATH

    print(exit_code)
    sys.exit(exit_code)
