import os
from jira import JIRA
import const

server_url = const.SERVER
password = const.PASSWORD
username = const.USERNAME

jira = JIRA(basic_auth=(username, password), options={"server": server_url})

os.system("clear")

# TODO: Check if QA test scenario is needed?

# Transition IDs
to_analysis = '11'
analysis_backlog_to_analysis = '231'
analysis_backlog_to_ready = '461'
analysis_to_ready = '411'

# Make Unassigned tickets on the ready or sprint backlog, move to analysis
jql = 'project = LG AND Sprint in openSprints() AND status in ("Sprint Backlog", Ready) AND assignee is EMPTY AND Side = Back-End AND priority = Medium'

issues = jira.search_issues(jql, maxResults=500)

print(len(issues))

# TODO: move to analysis backlog?
for issue in issues:
    print(f"{issue.key} moved to analysis")
    jira.transition_issue(issue, to_analysis)


# Get new sprint tickets
num_tickets = int(input("Input your DSH number of tickets: \n"))

del_tickets = dict()

for i in range(num_tickets):
    ticket_id = input()
    ticket_key = "LG-" + ticket_id
    del_tickets[ticket_key] = i + 1


# Create new sprint
del_board_id = 12

del_sprint_id = jira.sprints(del_board_id)[-1].id
del_sprint_name = jira.sprints(del_board_id)[-1].name

for ticket_key in del_tickets.keys():
    print("--------------------------------")
    print(ticket_key)
    try:
        # Set new sprint
        jira.add_issues_to_sprint(
            sprint_id=del_sprint_id, issue_keys=[ticket_key])
        print(f"Sprint Set to {del_sprint_name}")

        # Create ticket JQL
        issue_jql = "key = " + ticket_key
        issues = jira.search_issues(jql_str=issue_jql)

        for issue in issues:
            # Update impact
            issue.update(
                fields={"customfield_10201": {
                    "value": str(del_tickets[ticket_key])}}
            )
            print(f"Impact Updated to {del_tickets[ticket_key]}")

            # Update status
            if issue.fields.status.name == "Analysis Backlog":
                jira.transition_issue(issue, analysis_backlog_to_ready)
                print(f"Moved to Ready")
            if issue.fields.status.name == "Analysis":
                jira.transition_issue(issue, analysis_to_ready)
                print(f"Moved to Ready")

    except:
        print("Ticket Passed")
