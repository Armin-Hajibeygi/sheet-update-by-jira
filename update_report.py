import workflow, os, csv, const

username = const.USERNAME
password = const.PASSWORD

# Load the sheet IDs from the CSV file into a dictionary
with open('sheet_id.csv') as f:
    sheet_ids = dict(csv.reader(f))

os.system('clear')

update_type = int(input("Please choose your update type \n 1.Complete \n 2.Fast \n"))

if (update_type == 1):
    #Update FC
    print("... Connecting FC ...")
    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[FC] Sprints - 01", sheet_ids["FC"])
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating FC ...")
    workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "fc_area","developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
    print("FC Updated ^^")

    #Update DEL
    print("-----------------------------------------------")
    print("... Connecting DEL ...")

    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[DEL] Sprints - All", sheet_ids["DEL"])
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating DEL ...")
    workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "del_area", "developed_by", "estimate", "unit_test_estimate", "review_by", "impact", "status")
    print("DEL Updated ^^")

    #Update Front
    print("-----------------------------------------------")
    print("... Connecting Front ...")

    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[OPS] Front Sprints - 01", sheet_ids["FRONT"])
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating Front ...")
    workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "side", "epic", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
    print("Front Updated ^^")

    #Update Inventory
    print("-----------------------------------------------")
    print("... Connecting Inventory ...")

    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("Inventory", sheet_ids["Inventory"])
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating Inventory ...")
    workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "side", "epic", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
    print("Inventory Updated ^^")

# elif (update_type == 2):
#     print("... Connecting FC ...")
#     #Update FC
#     jira_connector = workflow.connect_jira(username, password)
#     print("Jira Connected")

#     sheet_connector = workflow.connect_sheet("[FC] Sprints - 01", fc_id)
#     print("G-Sheet Connected")
#     print("-----------------------------------------------")

#     print("Start Updating FC ...")
#     print("Updating Status")
#     workflow.update_field(jira_connector, sheet_connector, 10, "status")
#     print("Updating Developer")
#     workflow.update_field(jira_connector, sheet_connector, 5, "developed_by")
#     print("Updating Reviewer")
#     workflow.update_field(jira_connector, sheet_connector, 7, "review_by")
#     print("Updating Unit Test Estimate")
#     workflow.update_field(jira_connector, sheet_connector, 8, "review_estimate")
#     print("Front Updated ^^")
#     print("FC Updated ^^")

#     #print("-----------------------------------------------")
#     #print("... Connecting DEL ...")

#     #Update DEL
#     #jira_connector = workflow.connect_jira(username, password)
#     #print("Jira Connected")

#     #sheet_connector = workflow.connect_sheet("[DEL] Sprints - All", del_id)
#     #print("G-Sheet Connected")
#     #print("-----------------------------------------------")

#     #print("Start Updating DEL ...")
#     #print("Updating Status")
#     #workflow.update_field(jira_connector, sheet_connector, 10, "status")
#     #print("Updating Developer")
#     #workflow.update_field(jira_connector, sheet_connector, 5, "developed_by")
#     #print("Updating Review")
#     #workflow.update_field(jira_connector, sheet_connector, 8, "review_by")
#     #print("Updating Unit Test Estimate")
#     #workflow.update_field(jira_connector, sheet_connector, 7, "unit_test_estimate")
#     #print("DEL Updated ^^")

#     #print("-----------------------------------------------")
#     #print("... Connecting Front ...")

#     #Update Front
#     jira_connector = workflow.connect_jira(username, password)
#     print("Jira Connected")

#     sheet_connector = workflow.connect_sheet("[OPS] Front Sprints - 01", front_id)
#     print("G-Sheet Connected")
#     print("-----------------------------------------------")

#     print("Start Updating Front ...")
#     print("Updating Status")
#     workflow.update_field(jira_connector, sheet_connector, 10, "status")
#     print("Updating Developer")
#     workflow.update_field(jira_connector, sheet_connector, 5, "developed_by")
#     print("Updating Reviewer")
#     workflow.update_field(jira_connector, sheet_connector, 5, "review_by")
#     print("Updating Unit Test Estimate")
#     workflow.update_field(jira_connector, sheet_connector, 6, "review_estimate")
#     print("Front Updated ^^")

#     # print("-----------------------------------------------")
#     # print("... Connecting Platform ...")
#     # #Update Platform
#     # jira_connector = workflow.connect_jira(username, password)
#     # print("Jira Connected")

#     # sheet_connector = workflow.connect_sheet("[Platform] Sprints", platform_id)
#     # print("G-Sheet Connected")
#     # print("-----------------------------------------------")

#     # print("Start Updating Platform ...")
#     # print("Updating Status")
#     # workflow.update_field(jira_connector, sheet_connector, 8, "status")
#     # print("Updating Developer")
#     # workflow.update_field(jira_connector, sheet_connector, 4, "assignee")
#     # print("Platform Updated ^^")

#     print("-----------------------------------------------")
#     print("... Connecting Inventory ...")
#     #Update Inventory
#     jira_connector = workflow.connect_jira(username, password)
#     print("Jira Connected")

#     sheet_connector = workflow.connect_sheet("Inventory", inventory_id)
#     print("G-Sheet Connected")
#     print("-----------------------------------------------")

#     print("Start Updating Inventory ...")
#     print("Updating Status")
#     workflow.update_field(jira_connector, sheet_connector, 10, "status")
#     print("Updating Developer")
#     workflow.update_field(jira_connector, sheet_connector, 5, "developed_by")
#     print("Inventory Updated ^^")
