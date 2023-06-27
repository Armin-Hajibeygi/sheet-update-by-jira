import csv
import logging
from fastapi import FastAPI
from jira_sheet_bridge import Connector

app = FastAPI()


@app.get("/update")
def update_report():
    with open("sheet_id.csv") as f:
        sheet_ids = dict(csv.reader(f))

    sheet_name = "DEL - Sprints - 02 - All"
    worksheet_id = int(sheet_ids["DEL"])

    connector = Connector(sheet_name, worksheet_id)
    logging.info("Hello")
    connector.update_report()
