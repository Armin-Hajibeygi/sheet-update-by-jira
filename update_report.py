import workflow, os, csv

username = "armin.hajibeygi"
password = "Ahb137928!"

file = open('sheet_id.csv')
csvreader = csv.reader(file)
sheet_ids = dict()
for row in csvreader:
    sheet_ids[row[0]] = row[1]

fc_id = int(sheet_ids["FC"])
del_id = int(sheet_ids["DEL"])
dsh_id = int(sheet_ids["DSH"])

file.close()

os.system('clear')

print("... Connecting FC ...")
#Update FC
jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

sheet_connector = workflow.connect_sheet("[FC] Sprints - 01", fc_id)
print("G-Sheet Connected")
print("-----------------------------------------------")

print("Start Updating FC ...")
workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "developed_by", "estimate", "impact", "status")
print("FC Updated ^^")

print("-----------------------------------------------")
print("... Connecting DEL ...")

#Update DEL
jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

sheet_connector = workflow.connect_sheet("[DEL] Sprints - 01", del_id)
print("G-Sheet Connected")
print("-----------------------------------------------")

print("Start Updating DEL ...")
workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
print("DEL Updated ^^")

print("-----------------------------------------------")
print("... Connecting DSH ...")

#Update DSH Status
jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

sheet_connector = workflow.connect_sheet("DSH - Report", dsh_id)
print("G-Sheet Connected")
print("-----------------------------------------------")

print("Start Updating DSH ...")
workflow.update_field(jira_connector, sheet_connector, 5, "status")
print("DEL Updated ^^")