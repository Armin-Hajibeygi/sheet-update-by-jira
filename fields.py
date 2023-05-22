from abc import ABC, abstractmethod
from jira import JIRA, JIRAError


class Field(ABC):
    @abstractmethod
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.jira_connector = jira_connector

    @abstractmethod
    def get_field(self):
        pass


class Key(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        self.value = self.issue.key
        return self.value


class Summary(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        self.value = self.issue.fields.summary
        return self.value


# TODO
class Epic(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self):
        epic_jql = "key = " + str(self.issue.fields.customfield_10102)
        try:
            epic = self.jira_connector.search_issues(epic_jql)
            self.value = epic[0].fields.customfield_10104
        except JIRAError:
            self.value = ""

        return self.value


class Status(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        self.value = str(self.issue.fields.status)
        return self.value


class DevelopedBy(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        try:
            issue_developed_by = self.issue.fields.customfield_10202
            self.value = issue_developed_by.name
        except AttributeError:
            self.value = ""

        return self.value


class Impact(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        issue_priority = self.issue.fields.priority
        issue_impact = self.issue.fields.customfield_10201

        if (issue_priority.name == "High") or (issue_priority.name == "Highest"):
            self.value = issue_priority.name
        else:
            try:
                self.value = issue_impact.value
            except AttributeError:
                self.value = "0"
        return self.value


class Estimate(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = 0
        self.jira_connector = jira_connector

    def get_field(self) -> int:
        issue_estimate = self.issue.fields.customfield_10106

        try:
            self.value = int(issue_estimate)
        except (AttributeError, ValueError):
            self.value = 0
        return self.value


class ReviewBy(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        try:
            self.value = self.issue.fields.customfield_10508.name
        except AttributeError:
            self.value = "-"
        return self.value


class ReviewEstimate(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = 0
        self.jira_connector = jira_connector

    def get_field(self) -> int:
        issue_review_estimate = self.issue.fields.customfield_10530

        try:
            self.value = int(issue_review_estimate)
        except (AttributeError, TypeError):
            self.value = 0
        return self.value


class Side(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        ticket_key = self.issue.key
        dash_place = ticket_key.rfind('-')
        self.value = ticket_key[:dash_place]
        return self.value


class Assignee(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        try:
            self.value = self.issue.fields.assignee.name
        except AttributeError:
            self.value = ""
        return self.value


class UnitTestEstimate(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = 0
        self.jira_connector = jira_connector

    def get_field(self) -> int:
        issue_unit_test_estimate = self.issue.fields.customfield_10751

        try:
            self.value = int(issue_unit_test_estimate)
        except (AttributeError, TypeError):
            self.value = 0
        return self.value


class ReturnsFromReview(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = 0
        self.jira_connector = jira_connector

    def get_field(self) -> int:
        try:
            self.value = int(self.issue.fields.customfield_10752)
        except (AttributeError, TypeError):
            self.value = 0
        return self.value


class FcArea(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        try:
            self.value = str(self.issue.fields.customfield_10770)
        except (AttributeError, TypeError):
            self.value = ""
        return self.value


class DelArea(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        try:
            self.value = str(self.issue.fields.customfield_10773)
        except (AttributeError, TypeError):
            self.value = ""

        return self.value


# TODO
class TotalTimeInProgress(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        self.value = self.issue.fields.summary
        return self.value


# TODO
class FirstTimeInProgress(Field):
    def __init__(self, issue, jira_connector) -> None:
        self.issue = issue
        self.value = ""
        self.jira_connector = jira_connector

    def get_field(self) -> str:
        self.value = self.issue.fields.summary
        return self.value


class_map = {
    "key": Key,
    "summary": Summary,
    "epic": Epic,
    "status": Status,
    "developed_by": DevelopedBy,
    "impact": Impact,
    "estimate": Estimate,
    "review_by": ReviewBy,
    "review_estimate": ReviewEstimate,
    "side": Side,
    "assignee": Assignee,
    "unit_test_estimate": UnitTestEstimate,
    "returns_from_review": ReturnsFromReview,
    "fc_area": FcArea,
    "del_area": DelArea
}
