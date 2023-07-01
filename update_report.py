import jira_sheet_bridge

sheets = [
    {"sheet_name": "[Platform] Sprints"},
]

for sheet_num, sheet in enumerate(sheets):
    connector = jira_sheet_bridge.Connector(sheet["sheet_name"], sheet_num)
    connector.update_report()
