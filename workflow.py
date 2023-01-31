import googleSheet
from jira import JIRA
import datetime


def connect_jira(username, password):
    jira_connector = JIRA (basic_auth=(username, password), options={'server':'https://dkjira.digikala.com'})
    return jira_connector


def connect_sheet(sheet_name, worksheet_id):
    return googleSheet.Sheet(sheet_name, worksheet_id)


def str_time_to_datetime(complete_date):
    year = int(complete_date[:4])
    month = int(complete_date[5:7])
    day = int(complete_date[8:10])
    hour = int(complete_date[11:13])
    minutes = int(complete_date[14:16])
    time = datetime.datetime(year, month, day, hour, minutes)
    
    return time


# def date_diff_in_working_hours(date1, date2):
#     diff = date2 - date1
#     working_days = 0
#     while diff >= datetime.timedelta(hours=8):
#         diff -= datetime.timedelta(days=1)
#         if (date1.weekday() < 5):
#             working_days += 1
#         date1 += datetime.timedelta(days=1)
#     working_hours = working_days * 8
#     return working_hours


def date_diff(start_date, end_date):
    diff = end_date - start_date
    return int(diff.total_seconds() // 60)


def get_ticket(jira, sheet_connector, jql, *args):
    
    index = 0
    remaining_tickets = 0
    for issue in jira.search_issues(jql, maxResults=500):
        remaining_tickets += 1

    print(f"Number of tickets: {remaining_tickets}")

    for issue in jira.search_issues(jql, maxResults=500):
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
            elif (args[attr] == "review_by"):
                ticket.append(get_reviewed_by(issue))
            elif (args[attr] == "review_estimate"):
                ticket.append(get_review_estimate(issue))
            elif (args[attr] == "side"):
                    ticket.append(get_side(issue))
            elif (args[attr] == "step"):
                    ticket.append(get_step(issue))
            elif (args[attr] == "assignee"):
                    ticket.append(get_assignee(issue))
            elif (args[attr] == "unit_test_estimate"):
                    ticket.append(get_unit_test_estimate(issue))
            elif (args[attr] == "number_of_returns_from_review"):
                    ticket.append(get_number_of_returns_from_review(issue))
            elif (args[attr] == "fc_area"):
                    ticket.append(get_fc_area(issue))
            elif (args[attr] == "del_area"):
                    ticket.append(get_del_area(issue))
            elif (args[attr] == "total_time_in_progress"):
                    ticket.append(get_total_time_in_progress(issue))
            elif (args[attr] == "first_time_in_progress"):
                    ticket.append(get_first_time_in_progress(issue))

        insert_issues(ticket, sheet_connector, index, 0)
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
                elif (args[attr] == "review_by"):
                    ticket.append(get_reviewed_by(issue))
                elif (args[attr] == "review_estimate"):
                    ticket.append(get_review_estimate(issue))
                elif (args[attr] == "side"):
                    ticket.append(get_side(issue))
                elif (args[attr] == "step"):
                    ticket.append(get_step(issue))
                elif (args[attr] == "assignee"):
                    ticket.append(get_assignee(issue))
                elif (args[attr] == "unit_test_estimate"):
                    ticket.append(get_unit_test_estimate(issue))
                elif (args[attr] == "number_of_returns_from_review"):
                    ticket.append(get_number_of_returns_from_review(issue))
                elif (args[attr] == "fc_area"):
                    ticket.append(get_fc_area(issue))
                elif (args[attr] == "del_area"):
                    ticket.append(get_del_area(issue))
                elif (args[attr] == "total_time_in_progress"):
                    ticket.append(get_total_time_in_progress(issue))
                elif (args[attr] == "first_time_in_progress"):
                    ticket.append(get_first_time_in_progress(issue))

        insert_issues(ticket[1:], sheet_connector, index, 1)
        index += 1


def update_field(jira, sheet_connector, column, field):
    sheet_tickets, remaining_tickets = sheet_connector.get_sheet_tickets()

    index = 0

    for ticket in sheet_tickets:
        jql = "key = " + ticket 

        remaining_tickets -= 1
        print(f"Remaining: {remaining_tickets}")

        for issue in jira.search_issues(jql):
            if (field == "key"):
                ticket_field = get_key(issue)
            elif (field == "summary"):
                ticket_field = get_summary(issue)
            elif (field == "epic"):
                ticket_field = get_epic(jira, issue)
            elif (field == "status"):
                ticket_field = get_status(issue)
            elif (field == "developed_by"):
                ticket_field = get_developed_by(issue)
            elif (field == "impact"):
                ticket_field = get_impact(issue)
            elif (field == "estimate"):
                ticket_field = get_estimate(issue)
            elif (field == "review_by"):
                ticket_field = get_reviewed_by(issue)
            elif (field == "review_estimate"):
                ticket_field = get_review_estimate(issue)
            elif (field == "side"):
                ticket_field = get_side(issue)
            elif (field == "step"):
                ticket_field = get_step(issue)
            elif (field == "assignee"):
                ticket_field = get_assignee(issue)
            elif (field == "unit_test_estimate"):
                ticket_field = get_unit_test_estimate(issue)
            elif (field == "number_of_returns_from_review"):
                ticket_field = get_number_of_returns_from_review(issue)
            elif (field == "fc_area"):
                    ticket.append(get_fc_area(issue))
            elif (field == "del_area"):
                    ticket.append(get_del_area(issue))
            elif (field == "total_time_in_progress"):
                    ticket.append(get_total_time_in_progress(issue))
            elif (field == "first_time_in_progress"):
                    ticket.append(get_first_time_in_progress(issue))
            

            sheet_connector.update_field(index+2, column, ticket_field)
        
        index += 1


def insert_issues(ticket_info, sheet_connector, index, skip):
    sheet_connector.insert_ticket(ticket_info, skip, index+2)


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
        epic_name = epic[0].fields.customfield_10104
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
        estimate = 0

    return estimate


def get_reviewed_by(issue):
    issue_reviewed_by = issue.fields.customfield_10508

    try:
        reviewed_by = issue_reviewed_by.name
    except:
        reviewed_by = "-"

    return reviewed_by


def get_review_estimate(issue):
    issue_review_estimate = issue.fields.customfield_10530

    try:
        review_estimate = int(issue_review_estimate)
    except:
        review_estimate = 0

    return review_estimate


def get_side(issue):
    ticket_key = get_key(issue)
    dash_place = ticket_key.rfind('-')
    side = ticket_key[:dash_place]
    return side


def get_step(issue):
    issue_side = issue.fields.customfield_10531.value
    
    return issue_side
    

def get_assignee(issue):
    try:
        assignee = issue.fields.assignee.name
    except:
        assignee = ""
    
    return assignee


def get_unit_test_estimate(issue):
    issue_unit_test_estimate = issue.fields.customfield_10751

    try:
        unit_test_estimate = int(issue_unit_test_estimate)
    except:
        unit_test_estimate = 0

    return unit_test_estimate


def get_number_of_returns_from_review(issue):
    try:
        return (int(issue.fields.customfield_10752))
    except:
        return 0
   
    
def get_fc_area(issue):
    try:
        fc_area = str(issue.fields.customfield_10770)
    except:
        fc_area = ""
        
    return fc_area


def get_del_area(issue):
    try:
        del_area = str(issue.fields.customfield_10773)
    except:
        del_area = ""
        
    return del_area


def get_total_time_in_progress(issue):
    try:
        start_date_str = issue.fields.customfield_10801
        start_date = str_time_to_datetime(start_date_str)
        
        end_date_str = issue.fields.customfield_10802
        end_date = str_time_to_datetime(end_date_str)
        
        if (end_date > start_date):
            diff = date_diff(start_date, end_date)
            print(diff)
            current_time = int(issue.fields.customfield_10803)
            new_time = int(current_time + diff)
            if (current_time == 0):
                issue.update(fields={'customfield_10804': new_time}) 
        else:
            new_time = int(issue.fields.customfield_10803)
        
        issue.update(fields={'customfield_10803': new_time})
        return new_time
    
    except:
        return 0


def get_first_time_in_progress(issue):
    try:
        return (int(issue.fields.customfield_10804))
    except:
        return 0