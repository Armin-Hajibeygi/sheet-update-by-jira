import jira_sheet_bridge
import pandas as pd

squad = int(input("Squad: 1.DEL 2.Plat \n"))
if squad == 1:
    sheet_name = "DEL - Sprints - 02 - All"
elif squad == 2:
    sheet_name = "[Platform] Sprints"

worksheet_id = int(input("Please Enter Sheet ID \n"))
df = pd.read_csv("sheet_id.csv")
df.loc[squad, "sheet_id"] = worksheet_id

# Save the updated DataFrame to the CSV file
df.to_csv("sheet_id.csv", index=False)

connector = jira_sheet_bridge.Connector(sheet_name, worksheet_id, squad - 1)
connector.create_report()
