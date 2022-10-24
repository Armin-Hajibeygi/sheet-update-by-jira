import workflow, os, csv
import pandas as pd

username = "armin.hajibeygi"
password = "Ahb137928!"

os.system('clear')

squad = int(input("Choose Squad: \n 1.DEL \n 2.FC \n 3.Front \n 4.Plat \n"))
sheet_id = int(input("Please Enter Sheet ID \n"))

df = pd.read_csv("sheet_id.csv")
if squad == 1:  
    df.loc[1, 'sheet_id'] = sheet_id
elif squad == 2:
    df.loc[0, 'sheet_id'] = sheet_id
elif squad == 3:
    df.loc[2, 'sheet_id'] = sheet_id
elif squad == 4:
    df.loc[3, 'sheet_id'] = sheet_id

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

file.close()

jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

if squad == 1:
    sheet_connector = workflow.connect_sheet("[DEL] Sprints - 01", del_id)
    print("G-Sheet Connected")
    jql = 'project = LG AND Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Back-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic", "developed_by", "estimate", "impact", "status") 
elif squad == 2:
    sheet_connector = workflow.connect_sheet("[FC] Sprints - 01", fc_id)
    jql = 'project = DKFC AND Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Back-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic", "developed_by", "estimate", "impact", "status")
elif squad == 3:
    sheet_connector = workflow.connect_sheet("[OPS] Front Sprints - 01", front_id)
    jql = '(project = DKFC OR project = Delivery) AND  Sprint in openSprints() AND  (status = "Sprint Backlog" OR status = In-Progress) AND Side = Front-End ORDER BY priority DESC, cf[10201] ASC'
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "side", "epic", "developed_by", "estimate", "impact", "status") 
elif squad == 4:
    sheet_connector = workflow.connect_sheet("[Platform] Sprints", platform_id)
    jql = ''
    workflow.get_ticket(jira_connector, sheet_connector, jql, "key", "summary", "epic", "estimate", "status") 

os.system('clear')
