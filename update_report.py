import jira_sheet_bridge

sheets = [
    {"sheet_name": "[Platform] Sprints"},
]

for sheet in sheets:
    connector = jira_sheet_bridge.Connector(sheet["sheet_name"])
    connector.update_report()
