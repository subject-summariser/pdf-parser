import time
from datetime import datetime, timedelta

class SubjectAssessments:
    Assessments = []

    def __init__(self, text, program_start):
        start_index = 0
        start_index = self._find_next_assessment(text, start_index)
        while start_index+1 < len(text):
            next_index = self._find_next_assessment(text, start_index+1)
            self.Assessments.append(AssessmentTask(text, start_index, next_index, program_start))
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

    def __init__(self, text, start, end, program_start):
        self._text = text
        self._current_index = 0
        self._program_start = program_start

        for i in range(start, end):
            self._current_index = i
            self._find_assessment_items()

        if "not found" in self.TaskType.lower():
            self._extract_type_from_name()

    def _find_assessment_items(self):
        _current_line = self._text[self._current_index]
        
        if self._check_task_name(_current_line):
            self.TaskName = TaskName(_current_line).Name
            if '' == self.TaskName or None == self.TaskName:
                self.TaskName = "Task Name not found"
            return
        
        if self._check_due_date(_current_line):
            self.DueDate = DueDate(self._text, self._current_index, self._program_start).Date
            if '' == self.DueDate or None == self.DueDate:
                self.DueDate = "Due date not found"
            return

        if self._check_weight(_current_line):
            self.Weighting = Weighting(self._text, self._current_index).Weight
            if '' == self.Weighting or None == self.Weighting:
                self.Weighting = "Weighting not found"
            return

        if self._check_task_type(_current_line):
            self.TaskType = TaskType(self._text, self._current_index).Type
            if '' == self.TaskType or None == self.TaskType:
                self.TaskType = "Task type not found"
            return

        if self._check_group_work(_current_line):
            self.GroupWork = GroupWork(self._text, self._current_index).GroupType
            if '' == self.GroupWork or None == self.GroupWork:
                self.GroupWork = "Group work type not found"
            return
        
        if self._check_task_description(_current_line):
            self.TaskDescription = TaskDescription(_current_line).Description
            if '' == self.TaskDescription or None == self.TaskDescription:
                self.TaskDescription = "Task Description not found"
            return

    def _check_task_name(self, line):
        for number in ['1','2','3','4','5','6','7','8','9']:
            if line.find("Assessment task %s" % number) == 0:
                return True
    
        return False
        
    def _check_due_date(self, line):
        return line.find("Due:") == 0

    def _check_weight(self, line):
        return line.find("Weight:") == 0

    def _check_task_type(self, line):
        return line.find('Type:') == 0

    def _check_group_work(self, line):
        return line.find('Group:') == 0 or line.find('Groupwork:') == 0
        
    def _check_task_description(self, line):
        return False

    def _extract_type_from_name(self):
        _type_index = self.TaskName.find(":") + 2
        self.TaskType = self.TaskName[_type_index:]

class TaskName:
    Name = ""

    def __init__(self, line):
        self.Name = line

class DueDate:
    Date = ""

    def __init__(self, text, start_index, program_start):
        for i in range(start_index, len(text)):
            if self._is_time_format(text[i]):
                self.Date = self._convert_date(text[i])
                return
            
            if "week " in text[i].lower():
                _tmp_date = self._get_date_from_week(text[i], program_start)
                if _tmp_date:
                    self.Date = "Week of " + _tmp_date
                return

            if "refer to" in text[i].lower():
                self.Date = text[i]

            if text[i].find("Assessment") == 0:
                break

    def _is_time_format(self, input):
        formats = ["%d/%m/%y", "%d %b %y", "%A %d %B %Y", "%d/%m/%Y", "%d %m %y"]
    
        for format in formats:
            if self._try_time_format(input, format):
                self._time_format = format
                return True

        return False

    def _try_time_format(self, input, format):
        try:
            time.strptime(input, format)
            return True
        except:
            return False

    def _get_date_from_week(self, week, program_start):
        _week_numbers = ['18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1']
        for week_num in _week_numbers:
            if week.find("Week " + week_num) != -1:
                return self._convert_week(week_num, program_start)

    def _convert_week(self, week_num, program_start):
        try:
            dt = datetime.strptime(program_start + " 16", "%d %b %y")
            dt += timedelta(weeks=int(week_num))
            return str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year)   
        except:
            return None

    def _convert_date(self, date):
        dt = datetime.strptime(date, self._time_format)
        return str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year)

class Weighting:
    Weight = ""

    def __init__(self, text, index):
        for i in range(index, len(text)):
            if "%" in text[i]:
                self.Weight = text[i]
                return

            if text[i].find("Assessment") == 0:
                break

class TaskType:
    Type = ""

    def __init__(self, text, index):
        if text[index+1] != '':
            self.Type = text[index+1]
        else:
            self.Type = text[index+2]

class GroupWork:
    GroupType = ""

    def __init__(self, text, index):
        _title_end_index = text[index].find(':')
        if len(text[index]) > _title_end_index+1:
            self.GroupType = line[_title_end_index+2:]
        else:
            self.GroupType = text[index+1]

class TaskDescription:
    Description = ""

    def __init__(self, line):
        raise NotImplementedError