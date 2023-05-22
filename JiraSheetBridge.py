import googleSheet
import const
import fields
from jira import JIRA


class Connector:
    class_map = fields.class_map

    def __init__(self, sheet_name: str, worksheet_id: int) -> None:
        print("... Connecting ...")

        self.username = const.USERNAME
        self.password = const.PASSWORD
        self.server = const.SERVER
        self.fields = const.FIELDS
        self.jql = const.JQL
        self.sheet_name = sheet_name
        self.worksheet_id = worksheet_id
        self.issue_details = list()
        self.sheet_issues = None
        self.remaining_issues = None

        self.jira_connector = JIRA(basic_auth=(self.username, self.password), options={
            'server': self.server})
        print("Jira Connected!")

        self.google_sheet_connector = googleSheet.Sheet(self.sheet_name, self.worksheet_id)
        print("Google Sheet Connected!")

    def get_issues_from_sheet(self) -> None:
        self.sheet_issues, self.remaining_issues = self.google_sheet_connector.get_sheet_tickets()

    def update_report(self) -> None:
        self.get_issues_from_sheet()
        for index, ticket in enumerate(self.sheet_issues):
            jql = "key = " + ticket
            self.remaining_issues -= 1
            print(f"Remaining: {self.remaining_issues}")
            for issue in self.jira_connector.search_issues(jql):
                self.insert_issue(issue, index, 0)

    def create_report(self) -> None:
        issues = self.jira_connector.search_issues(self.jql, maxResults=500)
        print(f"Number of tickets: {len(issues)}")
        for index, issue in enumerate(issues):
            print(f"Remaining: {len(issues) - index}")
            self.insert_issue(issue, index, 0)

    def insert_issue(self, issue, index: int, skip: int) -> None:
        self.issue_details = list()
        for field_name in self.fields:
            field_class = Connector.class_map.get(field_name)
            self.issue_details.append(field_class(issue, self.jira_connector).get_field())
        self.google_sheet_connector.insert_ticket(self.issue_details, skip, index + 2)
