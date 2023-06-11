import workflow
import os
import csv
import const

username = const.USERNAME
password = const.PASSWORD

with open("sheet_id.csv") as f:
    sheet_ids = dict(csv.reader(f))

del_metric_id = int(sheet_ids.get("DEL_METRIC", 0))

os.system("clear")

print("-----------------------------------------------")
print("... Connecting Metrics ...")

# Update DEL_Metric
jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

sheet_connector = workflow.connect_sheet("DEL - Metrics - 02", del_metric_id)
print("G-Sheet Connected")
print("-----------------------------------------------")

print("Start Updating Metrics ...")
workflow.update_tickets(
    jira_connector,
    sheet_connector,
    "key",
    "developed_by",
    "estimate",
    "number_of_returns_from_review",
    "total_time_in_progress",
    "first_time_in_progress",
)
print("Metrics Updated ^^")
