import googleSheet
from tickets import Ticket
import pandas as pd
from jira import JIRA


def connect_jira(username, password):
    jira_connector = JIRA (basic_auth=(username, password), options={'server':'https://dkjira.digikala.com'})
    return jira_connector


def connect_sheet(sheet_name, worksheet_id):
    return googleSheet.Sheet(sheet_name, worksheet_id)


def get_ticket(jira, sheet_connector, jql, *args):
    
    index = 0
    remaining_tickets = 0
    for issue in jira.search_issues(jql):
        remaining_tickets += 1

    print(f"Number of tickets: {remaining_tickets}")

    for issue in jira.search_issues(jql):
        print(f"Remaining: {remaining_tickets}")
        remaining_tickets -= 1

        ticket = list()
        for attr in range(len(args)):
            if (args[attr] == "key"):
                ticket.append(get_key(issue))
            elif (args[attr] == "summary"):
                ticket.append(get_summary(issue))
            elif (args[attr] == "epic"):
                ticket.append(get_epic(jira, issue))
            elif (args[attr] == "status"):
                ticket.append(get_status(issue))
            elif (args[attr] == "developed_by"):
                ticket.append(get_developed_by(issue))
            elif (args[attr] == "impact"):
                ticket.append(get_impact(issue))
            elif (args[attr] == "estimate"):
                ticket.append(get_estimate(issue))

        insert_issues(ticket, sheet_connector, index)
        index += 1


def update_tickets(jira, sheet_connector, *args):
    sheet_tickets, remaining_tickets = sheet_connector.get_sheet_tickets()

    index = 0

    for ticket in sheet_tickets:
        jql = "key = " + ticket 

        remaining_tickets -= 1
        print(f"Remaining: {remaining_tickets}")

        for issue in jira.search_issues(jql):
            ticket = list()
            for attr in range(len(args)):
                if (args[attr] == "key"):
                    ticket.append(get_key(issue))
                elif (args[attr] == "summary"):
                    ticket.append(get_summary(issue))
                elif (args[attr] == "epic"):
                    ticket.append(get_epic(jira, issue))
                elif (args[attr] == "status"):
                    ticket.append(get_status(issue))
                elif (args[attr] == "developed_by"):
                    ticket.append(get_developed_by(issue))
                elif (args[attr] == "impact"):
                    ticket.append(get_impact(issue))
                elif (args[attr] == "estimate"):
                    ticket.append(get_estimate(issue))

        insert_issues(ticket, sheet_connector, index)
        index += 1



def insert_issues(ticket_info, sheet_connector, index):
    sheet_connector.insert_ticket(ticket_info, index+2)


def get_key(issue):
    key = issue.key
    return key


def get_summary(issue):
    summary = issue.fields.summary
    return summary


#TODO remove jira or add a search function
def get_epic(jira, issue):
    epic_jql = "key = " + str(issue.fields.customfield_10102)
    try:
        epic = jira.search_issues(epic_jql)
        epic_name = epic[0].fields.summary
    except:
        epic_name = ""
    
    return epic_name


def get_status(issue):
    status = str(issue.fields.status)
    return status


def get_developed_by(issue):
    issue_developed_by = issue.fields.customfield_10202
    try:
        developed_by = issue_developed_by.name
    except:
        developed_by = ""

    return developed_by


def get_impact(issue):
    issue_priority = issue.fields.priority
    issue_impact = issue.fields.customfield_10201

    if (issue_priority.name == "High") or (issue_priority.name == "Highest"):
        impact = issue_priority.name
    else:
        try:
            impact = issue_impact.value
        except:
            impact = "0"

    return impact


def get_estimate(issue):
    issue_estimate = issue.fields.customfield_10106

    try:
        estimate = int(issue_estimate)
    except:
        estimate = ""

    return estimate