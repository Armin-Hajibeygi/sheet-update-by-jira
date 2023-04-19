# Jira to Google Sheet Automation
This automation project is designed to retrieve data from Jira tickets and create corresponding reports in Google Sheets using Python. The Jira to Google Sheet automation enables users to efficiently track and manage project progress and share key metrics with stakeholders.
This automation uses the Jira REST API to retrieve data from Jira tickets and the Google Sheets API to create and update reports in Google Sheets. The automation script is designed to be easily customizable and can be adapted to meet specific project needs.


## Usage
The Jira to Google Sheet automation script is highly customizable and can be tailored to fit specific project needs. By default, the script retrieves data from Jira tickets and creates a report in Google Sheets with the following fields:

Users can modify the script to include additional fields or customize the report layout to meet their specific requirements.

## Prerequisites
```
Python 3.x
Jira account with API access
Google account with API access
Google Sheets API enabled
```

## How to use:
Create a ```const.py``` file then add your Jira configurations like below:
``` 
SERVER = 'Your Jira Server'
USERNAME = "Your Jira Username"
PASSWORD = "Your Jira Password"
```

### If you want to create reports, create a ```reports``` folder in your directory.
