"""
This module contains integrating Jira with Google sheet.
"""

from jira import JIRA
from jira.resources import Issue
import googleSheet
import const
import fields


class Connector:
    """
    This class connects Jira to a Google sheet.
    Get sheet_name from outside the class and define others with const.py

    Public Methods:
        create_report()
        update_report()
    """

    class_map = fields.class_map

    def __init__(self, sheet_name: str, sheet_num: int) -> None:
        """
        Parameters
        ----------
        sheet_name
        """
        print("... Connecting ...")

        self._username = const.USERNAME
        self._password = const.PASSWORD
        self._server = const.SERVER
        self._jql = const.JQL[sheet_num]
        self._fields = const.FIELDS[sheet_num]
        self._sheet_name = sheet_name
        self._issue_details = []
        self._sheet_issues = None
        self._remaining_issues = None

        self._jira_connector = JIRA(
            basic_auth=(self._username, self._password),
            options={"server": self._server},
        )
        print("Jira Connected!")

        self._google_sheet_connector = googleSheet.Sheet(self._sheet_name)
        print("Google Sheet Connected!")

    def _get_issues_from_sheet(self) -> None:
        """
        Get issue keys from Google sheet.
        """
        (
            self._sheet_issues,
            self._remaining_issues,
        ) = self._google_sheet_connector.get_sheet_tickets()

    def update_report(self) -> None:
        """
        Update Google sheet reports.
        """
        self._get_issues_from_sheet()
        for index, ticket in enumerate(self._sheet_issues):
            jql = "key = " + ticket
            self._remaining_issues -= 1
            print(f"Remaining: {self._remaining_issues}")
            for issue in self._jira_connector.search_issues(jql):
                self._insert_issue(issue, index, 0)

    def create_report(self) -> None:
        """
        Create Google sheet reports based on JQL.
        """
        issues = self._jira_connector.search_issues(self._jql, maxResults=500)
        print(f"Number of tickets: {len(issues)}")
        for index, issue in enumerate(issues):
            print(f"Remaining: {len(issues) - index}")
            self._insert_issue(issue, index, 0)

    def _insert_issue(self, issue: Issue, index: int, skip: int) -> None:
        """
        Insert issues to the Google sheet using googleSheet module.

        Parameters
        ----------
        issue
        index
        skip
        """
        self._issue_details = []
        for field_name in self._fields:
            field_class = Connector.class_map.get(field_name)
            if field_name == "epic":
                self._issue_details.append(
                    field_class(issue, self._jira_connector).get_field()
                )
            else:
                self._issue_details.append(field_class(issue).get_field())
        self._google_sheet_connector.insert_ticket(self._issue_details, skip, index + 2)
