import os
import csv
import const
import googleSheet
import workflow
from datetime import datetime
from jira import JIRA
from gant_report import create_gantt

# Define Consts
server_url = const.SERVER
password = const.PASSWORD
username = const.USERNAME
del_board_id = 12
fc_board_id = 11

# Get sheet ids
with open('sheet_id.csv') as f:
    sheet_ids = dict(csv.reader(f))

os.system('clear')

# Get squad
squad = int(
        input("Choose Squad: \n 1.FC \n 2.DEL \n"))

# Connect jira
jira = JIRA(basic_auth=(username, password), options={
    'server': server_url})

# Connect sheet to get sprint tickets
sheet_connector = googleSheet.Sheet("[FC] Sprints - 02", int(sheet_ids["FC"]))
tickets, number_of_tickets = sheet_connector.get_sheet_tickets()
sheet_name = sheet_connector.get_sheet_name()

# Get tickets
issues = list()
outbound_issues = list()
inbound_issues = list()

for ticket in tickets:
    if squad == 1:
        jql = 'key = ' + ticket
        issue = jira.search_issues(jql)[0]
        fc_area = workflow.get_fc_area(issue)

        if fc_area == 'Inbound':
            inbound_issues.append(issue)
        elif fc_area == 'Outbound':
            outbound_issues.append(issue)

    elif squad == 2:
        jql = 'key = ' + ticket
        issues.append(jira.search_issues(jql)[0])

os.system('clear')

# Handle time limitation
time_limitation = int(
    input("Choose Time Limitation: \n 1.2 Weeks \n 2.All Time \n"))
if time_limitation == 1:
    del_sprint_id = jira.sprints(del_board_id)[-1].id
    fc_sprint_id = jira.sprints(fc_board_id)[-1].id

    if squad == 1:
        sprint = jira.sprint(fc_sprint_id)
    elif squad == 2:
        sprint = jira.sprint(del_sprint_id)

    start_date = datetime.strptime(str(sprint.startDate)[:19], '%Y-%m-%dT%H:%M:%S')
    gantt_title = sheet_name + ' - 2 Weeks Report'

else:
    start_date = datetime.min
    gantt_title = sheet_name + ' - All Time Report'

# Create gantt charts
if squad == 1:
    create_gantt(inbound_issues, gantt_title + ' - Inbound', start_date)
    create_gantt(outbound_issues, gantt_title + ' - Outbound', start_date)
elif squad == 2:
    create_gantt(issues, gantt_title, start_date)
