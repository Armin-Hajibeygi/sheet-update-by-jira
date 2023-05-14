import os
import csv
import const
import googleSheet
from jira import JIRA
from gant_report import create_gantt

server_url = const.SERVER
password = const.PASSWORD
username = const.USERNAME

with open('sheet_id.csv') as f:
    sheet_ids = dict(csv.reader(f))

os.system('clear')

jira = JIRA(basic_auth=(username, password), options={
    'server': server_url})

# Connect sheet to get sprint tickets
sheet_connector = googleSheet.Sheet("[FC] Sprints - 02", int(sheet_ids["FC"]))
tickets, number_of_tickets = sheet_connector.get_sheet_tickets()
sheet_name = sheet_connector.get_sheet_name()

issues = list()
for ticket in tickets:
    jql = 'key = ' + ticket
    issues.append(jira.search_issues(jql)[0])

create_gantt(issues, sheet_name)
