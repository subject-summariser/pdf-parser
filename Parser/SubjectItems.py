class Contact:
    TutorName = ""
    Email = ""
    Room = ""
    Phone = ""

    def __init__(self, text):
        raise NotImplementedError

class ContactInfo:
    TutorContacts = []      
    
    def __init__(self, text):
        raise NotImplementedError

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