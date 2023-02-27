import workflow, os, csv, const

username = const.USERNAME
password = const.PASSWORD

file = open('sheet_id.csv')
csvreader = csv.reader(file)
sheet_ids = dict()
for row in csvreader:
    sheet_ids[row[0]] = row[1]

fc_id = int(sheet_ids["FC"])
del_id = int(sheet_ids["DEL"])
front_id = int(sheet_ids["Front"])
platform_id = int(sheet_ids["Plat"])
dsh_id = int(sheet_ids["DSH"])
fc_metric_id = int(sheet_ids["FC_METRIC"])

file.close()

os.system('clear')

input("Please Update the Sheet ID")

#Update DEL
jira_connector = workflow.connect_jira(username, password)
print("Jira Connected")

sheet_connector = workflow.connect_sheet("[FC] Metrics", fc_metric_id)
print("G-Sheet Connected")
print("-----------------------------------------------")

print("Start Updating Metrics ...")
workflow.update_tickets(jira_connector, sheet_connector, "key", "developed_by", "estimate", "number_of_returns_from_review", "total_time_in_progress", "first_time_in_progress")
print("Metrics Updated ^^")