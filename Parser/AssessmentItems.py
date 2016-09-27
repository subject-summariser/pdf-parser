class SubjectAssessments:
    Assessments = []

    def __init__(self, text):
        start_index = 0
        start_index = self._find_next_assessment(text, start_index)
        while start_index+1 < len(text):
            next_index = self._find_next_assessment(text, start_index+1)
            self.Assessments.append(AssessmentTask(text, start_index, next_index))
            start_index = next_index

    def _find_next_assessment(self, text, start_index):
        current_index = 0
        for i in range(start_index, len(text)):
            current_index = i
            if self._check_task_name(text[i]):
                return i
            if i+1 == len(text):
                return i

    def _check_task_name(self, line):
        for number in range(1,9):
            if line.find("Assessment task %s" % number) == 0:
                return True

class AssessmentTask:
    TaskName = ""
    DueDate = ""
    Weighting = ""
    TaskType = ""
    GroupWork = ""
    TaskDescription = ""

    def __init__(self, text, start, end):
        self._text = text
        self._current_index = 0

        for i in range(start, end):
            self._current_index = i
            self._find_assessment_items()

        if self.TaskType == "":
            self._extract_type_from_name()

    def _find_assessment_items(self):
        if self._check_task_name(self._text[self._current_index]):
            self.TaskName = TaskName(self._text[self._current_index]).Name
            return
        
        if self._check_due_date(self._text[self._current_index]):
            self.DueDate = DueDate(self._text[self._current_index]).Date
            return

        if self._check_weight(self._text[self._current_index]):
            self.Weighting = Weighting(self._text[self._current_index]).Weight
            return

        if self._check_task_type(self._text[self._current_index]):
            self.TaskType = TaskType(self._text, self._current_index).Type
            return

        if self._check_group_work(self._text[self._current_index]):
            self.GroupWork = GroupWork(self._text[self._current_index]).GroupType
            return
        
        if self._check_task_description(self._text[self._current_index]):
            self.TaskDescription = TaskDescription(self._text[self._current_index]).Description
            return

    def _check_task_name(self, line):
        for number in ['1','2','3','4','5','6','7','8','9']:
            if line.find("Assessment task %s" % number) == 0:
                return True
    
        return False
        
    def _check_due_date(self, line):
        return False

    def _check_weight(self, line):
        return False

    def _check_task_type(self, line):
        if line.find('Type:') == 0:
            return True

    def _check_group_work(self, line):
        return False
        
    def _check_task_description(self, line):
        return False

    def _extract_type_from_name(self):
        _type_index = self.TaskName.find(":") + 2
        self.TaskType = "Type: " + self.TaskName[_type_index:]

class TaskName:
    Name = ""

    def __init__(self, line):
        self.Name = line

class DueDate:
    Date = ""

    def __init__(self, line):
        raise NotImplementedError

class Weighting:
    Weight = ""

    def __init__(self, line):
        raise NotImplementedError

class TaskType:
    Type = ""

    def __init__(self, text, index):
        self.Type = text[index] + " " + text[index+2]

class GroupWork:
    GroupType = ""

    def __init__(self, line):
        raise NotImplementedError

class TaskDescription:
    Description = ""

    def __init__(self, line):
        raise NotImplementedError