import JiraSheetBridge
import pandas as pd

squad = 1
sheet_name = "DEL - Sprints - 02 - All"
worksheet_id = int(input("Please Enter Sheet ID \n"))

df = pd.read_csv("sheet_id.csv")
df.loc[squad, 'sheet_id'] = worksheet_id

# Save the updated DataFrame to the CSV file
df.to_csv("sheet_id.csv", index=False)

connector = JiraSheetBridge.Connector(sheet_name, worksheet_id)
connector.create_report()
