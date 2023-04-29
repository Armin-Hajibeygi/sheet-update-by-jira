import workflow
import os
import csv
import const

username = const.USERNAME
password = const.PASSWORD

# Load the sheet IDs from the CSV file into a dictionary
with open('sheet_id.csv') as f:
    sheet_ids = dict(csv.reader(f))

os.system('clear')

# Update FC
# print("... Connecting FC ...")
# jira_connector = workflow.connect_jira(username, password)
# print("Jira Connected")

# sheet_connector = workflow.connect_sheet(
#     "[FC] Sprints - 02", int(sheet_ids["FC"]))
# print("G-Sheet Connected")
# print("-----------------------------------------------")

# print("Start Updating FC ...")
# workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "fc_area",
#                         "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
# print("FC Updated ^^")

# Update DEL
print("-----------------------------------------------")
print("... Connecting DEL ...")

jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

sheet_connector = workflow.connect_sheet(
    "DEL - Sprints - 02 - All", int(sheet_ids["DEL"]))
print("G-Sheet Connected")
print("-----------------------------------------------")

print("Start Updating DEL ...")
workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "del_area",
                        "developed_by", "estimate", "unit_test_estimate", "review_by", "impact", "status")
print("DEL Updated ^^")

# # Update Front
# print("-----------------------------------------------")
# print("... Connecting Front ...")

# jira_connector = workflow.connect_jira(username, password)
# print("Jira Connected")

# sheet_connector = workflow.connect_sheet(
#     "[OPS] Front Sprints - 01", int(sheet_ids["FRONT"]))
# print("G-Sheet Connected")
# print("-----------------------------------------------")

# print("Start Updating Front ...")
# workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "side", "epic",
#                         "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
# print("Front Updated ^^")

# # Update Inventory
# print("-----------------------------------------------")
# print("... Connecting Inventory ...")

# jira_connector = workflow.connect_jira(username, password)
# print("Jira Connected")

# sheet_connector = workflow.connect_sheet(
#     "Inventory", int(sheet_ids["Inventory"]))
# print("G-Sheet Connected")
# print("-----------------------------------------------")

# print("Start Updating Inventory ...")
# workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "side", "epic",
#                         "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
# print("Inventory Updated ^^")
