import jira_sheet_bridge

squad = int(input("Squad: 1.DEL 2.Plat \n"))
if squad == 1:
    sheet_name = "DEL - Sprints - 02 - All"
elif squad == 2:
    sheet_name = "[Platform] Sprints"

connector = jira_sheet_bridge.Connector(sheet_name, squad - 1)
connector.create_report()
