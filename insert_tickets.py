import workflow
import os
import csv
import const
import pandas as pd

username = const.USERNAME
password = const.PASSWORD

os.system('clear')

# Create a dictionary to map squad numbers to row indexes
# FC:0, DEL:1, Front:3, Plat:4, Inventory:5
squad_dict = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}

# Get user inputs
squad = int(
    input("Choose Squad: \n 1.FC \n 2.DEL \n 3.Front \n 4.Plat \n 5.Inventory \n"))
sheet_id = int(input("Please Enter Sheet ID \n"))

# Load the CSV file into a DataFrame
df = pd.read_csv("sheet_id.csv")

# Update the DataFrame with the new sheet ID
df.loc[squad_dict[squad], 'sheet_id'] = sheet_id

# Save the updated DataFrame to the CSV file
df.to_csv("sheet_id.csv", index=False)

# Load the sheet IDs from the CSV file into a dictionary
with open('sheet_id.csv') as f:
    sheet_ids = dict(csv.reader(f))

jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

# Connect to Google Sheets and fetch data from Jira
if squad == 1:
    sheet_connector = workflow.connect_sheet(
        "[FC] Sprints - 01", int(sheet_ids["FC"]))
    jql = 'project = DKFC AND Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Back-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic", "fc_area",
                        "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
elif squad == 2:
    sheet_connector = workflow.connect_sheet(
        "DEL - Sprints - 02 - All", int(sheet_ids["DEL"]))
    print("G-Sheet Connected")
    jql = 'project = LG AND Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Back-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic", "del_area",
                        "developed_by", "estimate", "unit_test_estimate", "review_by", "impact", "status")
elif squad == 3:
    sheet_connector = workflow.connect_sheet(
        "[OPS] Front Sprints - 01", int(sheet_ids["Front"]))
    jql = '(project = DKFC OR project = Delivery) AND  Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Front-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "side",
                        "epic", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
elif squad == 4:
    sheet_connector = workflow.connect_sheet(
        "[Platform] Sprints", int(sheet_ids["Plat"]))
    jql = 'project =Platform AND status in ("DX Sprint Backlog", "SRE Sprint Backlog", "SN Sprint Backlog", "Infrastructure Sprint Backlog") AND Sprint in openSprints() ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector)

os.system('clear')
