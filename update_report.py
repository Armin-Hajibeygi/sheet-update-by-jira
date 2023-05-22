import JiraSheetBridge
import csv

# Load the sheet IDs from the CSV file into a dictionary
with open('sheet_id.csv') as f:
    sheet_ids = dict(csv.reader(f))

sheet_name = "DEL - Sprints - 02 - All"
worksheet_id = int(sheet_ids["DEL"])

connector = JiraSheetBridge.Connector(sheet_name, worksheet_id)
connector.update_report()
