import jira_sheet_bridge
import csv

# Load the sheet IDs from the CSV file into a dictionary
with open("sheet_id.csv") as f:
    sheet_ids = dict(csv.reader(f))


sheets = [
    {"sheet_name": "[Platform] Sprints", "worksheet_id": int(sheet_ids["Plat"])},
]

for sheet_num, sheet in enumerate(sheets):
    connector = jira_sheet_bridge.Connector(
        sheet["sheet_name"], sheet["worksheet_id"], sheet_num
    )
    connector.update_report()
