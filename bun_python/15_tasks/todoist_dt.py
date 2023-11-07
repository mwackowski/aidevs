class IDue:
    def __init__(self, date_, timezone_, string_, lang, datetime_, is_recurring=False):
        self.date = date_
        self.timezone = timezone_
        self.string = string_
        self.lang = lang
        self.is_recurring = is_recurring
        self.datetime = datetime_


class ITaskModify:
    def __init__(self, idx, content, due_string, is_completed=False):
        self.idx = idx
        self.content = content
        self.due_string = due_string
        self.is_completed = is_completed


class ITaskClose:
    def __init__(self, idx):
        self.idx = idx


class ITask:
    def __init__(
        self,
        idx,
        due,
        assigner_id=None,
        assignee_id=None,
        project_id="",
        section_id=None,
        parent_id=None,
        order=0,
        content="",
        description="",
        is_completed=False,
        labels=[],
        priority=0,
        comment_count=0,
        creator_id="",
        created_at="",
        url="",
        duration=None,
    ):
        self.idx = idx
        self.assigner_id = assigner_id
        self.assignee_id = assignee_id
        self.project_id = project_id
        self.section_id = section_id
        self.parent_id = parent_id
        self.order = order
        self.content = content
        self.description = description
        self.is_completed = is_completed
        self.labels = labels
        self.priority = priority
        self.comment_count = comment_count
        self.creator_id = creator_id
        self.created_at = created_at
        self.due = due
        self.url = url
        self.duration = duration
