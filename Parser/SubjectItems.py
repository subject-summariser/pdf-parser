import time
from datetime import datetime, timedelta

class Contact:
    TutorName = ""
    Email = ""
    Room = ""
    Phone = ""

    def __init__(self, text, index):
        for i in range(index+1, len(text)):
            if text[i] != '\n':
                if self.TutorName == "":
                    self.TutorName = text[i]
                else:
                    if "@" in text[i].lower():
                        self.Email = text[i]
                    elif "room" in text[i].lower():
                        self.Room = text[i]
                    elif "phone" in text[i].lower() or "ph:" in text[i].lower():
                        self.Phone = text[i]
            if self.TutorName and self.Email and self.Room and self.Phone:
                return

class ContactInfo:
    TutorContacts = []      
    
    def __init__(self, text):
        for i in range(0, len(text)):
            if text[i].lower().find("subject coordinator") == 0:
                self.TutorContacts.append(Contact(text, i))
                return

class Date:
    Day = ""
    Month = ""
    Year = ""
    
    def __init__(self, text):
        raise NotImplementedError

class TaskType:
    Type = ""
    
    def __init__(self, text):
        raise NotImplementedError

class SubjectName:
    Name = ""
    
    def __init__(self, text):
        self.Name = text[1]

class RequiredTexts:
    Texts = []
    
    def __init__(self, text):
        raise NotImplementedError

class SubjectTopics:
    Topics = []
    
    def __init__(self, text):
        raise NotImplementedError

class SupplementaryTasks:
    Tasks = ""
    
    def __init__(self, text):
        raise NotImplementedError

class LatePenalty:
    Penalty = ""
    
    def __init__(self, text):
        raise NotImplementedError

class PassCriteria:
    Criteria = ""
    
    def __init__(self, text):
        raise NotImplementedError

class ProgramStartDate:
    StartDate = ""

    def __init__(self, text):
        for i in range(0, len(text)):
            if text[i].lower().replace('\n','') == "program":
                self._extract_program_start_date(text, i)
                return

    def _extract_program_start_date(self, text, index):
        for i in range(index, len(text)):
            text[i].replace('\n','')
            if text[i][0] == '1' and len(text[i]) < 4:
                self.StartDate = self._find_next_date(text, i)
                if self.StartDate == "" or self.StartDate == None:
                    self.StartDate = self._find_dates(text, index)
                return

    def _find_dates(self, text, index):
        for i in range(index, len(text)):
            if self._is_time_format(text[i]):
                if "orientation" not in text[i-1].lower() and "prep" not in text[i-1].lower():
                    return self._find_monday(text[i])
                    
    def _find_next_date(self, text, index):
        for i in range(index, len(text)):
            if self._is_time_format(text[i]):
                return self._find_monday(text[i])

    def _is_time_format(self, input):
        input = input.replace('\n','')
        try:
            time.strptime(input, '%d %b')
            return True
        except:
            return False

    def _find_monday(self, input):
        dt = datetime.strptime(input + " 16", "%d %b %y")
        dt = dt - timedelta(days=dt.weekday())
        return dt.strftime("%d %b")