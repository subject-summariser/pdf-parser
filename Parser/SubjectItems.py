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

class SubjectName:
    Name = ""
    
    def __init__(self, text):
        self.Name = text[1]

class RequiredTexts:
    Texts = []
    
    def __init__(self, text):
        for i in range(0, len(text)):
            if text[i].lower().find('required texts') == 0:
                for j in range(i+1, len(text)):
                    if text[j] == "\n":
                        break
                    self.Texts.append(text[j])
                return

class SubjectTopics:
    Topics = []
    
    def __init__(self, text):
        for i in range(0, len(text)):
            if text[i].lower().find("content (topics)") == 0:
                for j in range(i+1, len(text)):
                    if text[j].replace("\n",'') == "Program" or len(text[j]) > 80:
                        return
                    if text[j] != "\n" and len(text[j].replace("\n",'')) > 3: 
                        self.Topics.append(text[j])

class SupplementaryTasks:
    Tasks = ""
    
    def __init__(self, text):
        for i in range(0, len(text)):
            if text[i].lower().find('supplementary assessment') == 0:
                for j in range(i+1, len(text)):
                    if text[j] == "\n" or text[j].lower().find("minimum requirements") == 0:
                        break
                    self.Tasks += text[j]
                return

class LatePenalty:
    Penalty = ""
    
    def __init__(self, text):
        for i in range(0, len(text)):
            line_num = -1
            if text[i].lower().find("late submission") != -1:
                penalty_index = -1
                if text[i].lower().find("%") != -1:
                    penalty_index = text[i].lower().find("%")
                    line_num = i
                elif text[i+1].lower().find("%") != -1:
                    penalty_index = text[i+1].lower().find("%")
                    line_num = i + 1

                if penalty_index == -1:
                    return

                self.Penalty = text[line_num][penalty_index-2:penalty_index+1]
                return
            

class PassCriteria:
    Criteria = ""
    
    def __init__(self, text):
        for i in range(0, len(text)):
            if text[i].lower().find("minimum requirements") == 0:
                for j in range(i+1, len(text)):
                    if text[j].lower().find("required texts") == 0 or j > i + 10:
                        return  
                    if text[j] != "\n":
                        self.Criteria += text[j]

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