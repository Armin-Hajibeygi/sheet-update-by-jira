import workflow, os, csv, const
import pandas as pd

username = const.USERNAME
password = const.PASSWORD

os.system('clear')

# Create a dictionary to map squad numbers to row indexes
#FC:0, DEL:1, Front:3, Plat:4, Inventory:5
squad_dict = {1:0, 2:1, 3:2, 4:3, 5:4}

# Get user inputs
squad = int(input("Choose Squad: \n 1.FC \n 2.DEL \n 3.Front \n 4.Plat \n 5.Inventory \n"))
sheet_id = int(input("Please Enter Sheet ID \n"))

# Load the CSV file into a DataFrame
df = pd.read_csv("sheet_id.csv")

# Update the DataFrame with the new sheet ID
df.loc[squad_dict[squad], 'sheet_id'] = sheet_id

# Save the updated DataFrame to the CSV file
df.to_csv("sheet_id.csv", index=False)

file = open('sheet_id.csv')
csvreader = csv.reader(file)
sheet_ids = dict()
for row in csvreader:
    sheet_ids[row[0]] = row[1]

fc_id = int(sheet_ids["FC"])
del_id = int(sheet_ids["DEL"])
front_id = int(sheet_ids["Front"])
platform_id = int(sheet_ids["Plat"])
inventory_id = int(sheet_ids["Inventory"])

file.close()

jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

if squad == 1:
    sheet_connector = workflow.connect_sheet("[FC] Sprints - 01", fc_id)
    jql = 'project = DKFC AND Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Back-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic","fc_area", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
elif squad == 2:
    sheet_connector = workflow.connect_sheet("[DEL] Sprints - All", del_id)
    print("G-Sheet Connected")
    jql = 'project = LG AND Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Back-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic", "del_area", "developed_by", "estimate", "unit_test_estimate", "review_by", "impact", "status") 
elif squad == 3:
    sheet_connector = workflow.connect_sheet("[OPS] Front Sprints - 01", front_id)
    jql = '(project = DKFC OR project = Delivery) AND  Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Front-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "side", "epic", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status") 
elif squad == 4:
    sheet_connector = workflow.connect_sheet("[Platform] Sprints", platform_id)
    jql = 'project =Platform AND status in ("DX Sprint Backlog", "SRE Sprint Backlog", "SN Sprint Backlog", "Infrastructure Sprint Backlog") AND Sprint in openSprints() ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "step", "assignee","epic", "estimate", "impact", "status") 
elif squad == 5:
    sheet_connector = workflow.connect_sheet(" Inventory", inventory_id)
    jql = 'project = DKFC AND Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Back-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic","fc_area", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")

os.system('clear')
