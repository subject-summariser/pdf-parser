from SubjectItems import *
from AssessmentItems import *
import subprocess, os

def convert(file_path):
    subprocess.call('python C:\\Python27\\Scripts\\pdf2txt.py -o Temp.txt "%s"' % file_path)

    text = []

    with open("Temp.txt") as openfile:
        for line in openfile:
            for invalid_char in ['\x0c']:
                line = line.replace(invalid_char,'')
            if line != '':
                text.append(line)

    os.remove("Temp.txt")
    
    return text

class Summary:
    def __init__(self, pdf_path):
        __subject_outline_as_text = convert(pdf_path)

        if len(__subject_outline_as_text) == 0:
            raise Exception('Failed to Parse PDF')

        self.subject_name = SubjectName(__subject_outline_as_text).Name
        self.program_start_date = ProgramStartDate(__subject_outline_as_text).StartDate
        self.contact_info = ContactInfo(__subject_outline_as_text).TutorContacts
        #self.topics = SubjectTopics().Topics
        self.assessments = SubjectAssessments(__subject_outline_as_text, self.program_start_date).Assessments
        #self.required_texts = RequiredTexts().Texts
        #self.supplementary_tasks = SupplementaryTasks().Tasks
        #self.late_penalty = LatePenalty().Penalty
        #self.pass_criteria = PassCriteria().Criteria