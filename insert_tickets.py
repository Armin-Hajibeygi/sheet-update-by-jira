import jira_sheet_bridge

sheet_name = "[Platform] Sprints"

connector = jira_sheet_bridge.Connector(sheet_name)
connector.create_report()
