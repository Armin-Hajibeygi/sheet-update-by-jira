import workflow, os, csv

username = "armin.hajibeygi"
password = "FaithBudgetWill137928!"

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

file.close()

os.system('clear')

update_type = int(input("Please choose your update type \n 1.Complete \n 2.Fast \n"))

if (update_type == 1):
    print("... Connecting FC ...")
    #Update FC
    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[FC] Sprints - 01", fc_id)
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating FC ...")
    workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "fc_area","developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
    print("FC Updated ^^")

    print("-----------------------------------------------")
    print("... Connecting DEL ...")

    #Update DEL
    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[DEL] Sprints - All", del_id)
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating DEL ...")
    workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "epic", "del_area", "developed_by", "estimate", "unit_test_estimate", "review_by", "impact", "status")
    print("DEL Updated ^^")

    print("-----------------------------------------------")
    print("... Connecting Front ...")

    #Update Front
    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[OPS] Front Sprints - 01", front_id)
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating Front ...")
    workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "side", "epic", "developed_by", "estimate", "review_by", "review_estimate", "impact", "status")
    print("Front Updated ^^")


    # print("-----------------------------------------------")
    # print("... Connecting Platform ...")
    # #Update Platform
    # jira_connector = workflow.connect_jira(username, password)
    # print("Jira Connected")

    # sheet_connector = workflow.connect_sheet("[Platform] Sprints", platform_id)
    # print("G-Sheet Connected")
    # print("-----------------------------------------------")

    # print("Start Updating Platform ...")
    # workflow.update_tickets(jira_connector, sheet_connector, "key", "summary", "step", "assignee","epic", "estimate", "impact", "status")
    # print("Platform Updated ^^")


elif (update_type == 2):
    print("... Connecting FC ...")
    #Update FC
    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[FC] Sprints - 01", fc_id)
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating FC ...")
    print("Updating Status")
    workflow.update_field(jira_connector, sheet_connector, 9, "status")
    print("Updating Developer")
    workflow.update_field(jira_connector, sheet_connector, 5, "developed_by")
    print("FC Updated ^^")

    print("-----------------------------------------------")
    print("... Connecting DEL ...")

    #Update DEL
    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[DEL] Sprints - All", del_id)
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating DEL ...")
    print("Updating Status")
    workflow.update_field(jira_connector, sheet_connector, 10, "status")
    print("Updating Developer")
    workflow.update_field(jira_connector, sheet_connector, 5, "developed_by")
    print("Updating Review")
    workflow.update_field(jira_connector, sheet_connector, 8, "review_by")
    print("Updating Unit Test Estimate")
    workflow.update_field(jira_connector, sheet_connector, 7, "unit_test_estimate")
    print("DEL Updated ^^")

    print("-----------------------------------------------")
    print("... Connecting Front ...")

    #Update Front
    jira_connector = workflow.connect_jira(username, password)
    print("Jira Connected")

    sheet_connector = workflow.connect_sheet("[OPS] Front Sprints - 01", front_id)
    print("G-Sheet Connected")
    print("-----------------------------------------------")

    print("Start Updating Front ...")
    print("Updating Status")
    workflow.update_field(jira_connector, sheet_connector, 9, "status")
    print("Updating Developer")
    workflow.update_field(jira_connector, sheet_connector, 4, "developed_by")
    print("Front Updated ^^")

    # print("-----------------------------------------------")
    # print("... Connecting Platform ...")
    # #Update Platform
    # jira_connector = workflow.connect_jira(username, password)
    # print("Jira Connected")

    # sheet_connector = workflow.connect_sheet("[Platform] Sprints", platform_id)
    # print("G-Sheet Connected")
    # print("-----------------------------------------------")

    # print("Start Updating Platform ...")
    # print("Updating Status")
    # workflow.update_field(jira_connector, sheet_connector, 8, "status")
    # print("Updating Developer")
    # workflow.update_field(jira_connector, sheet_connector, 4, "assignee")
    # print("Platform Updated ^^")
