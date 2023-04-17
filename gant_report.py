from jira import JIRA
import os
import const
import pandas as pd
from datetime import datetime


username = const.USERNAME
password = const.PASSWORD

jira = JIRA(basic_auth=(username, password), options={
            'server': 'https://dkjira.digikala.com'})
jql = "key = DKFC-12289"

os.system('clear')

project = pd.DataFrame(columns=['issue', 'date', 'action_by', 'from', 'to'])

for issue in jira.search_issues(jql, maxResults=500):
    changelog = jira.issue(str(issue.key), expand='changelog').changelog
    action = {'issue': str(issue.key), 'date': datetime.strptime(
                    issue.fields.created[:10], '%Y-%M-%d').date(), 'action_by': issue.fields.reporter.displayName, 'from': "", 'to': ""}
    project = project.append(action, ignore_index=True)
    
    for history in changelog.histories:
        for item in history.items:
            if item.field == 'status':
                action = {'issue': str(issue.key), 'date': datetime.strptime(
                    history.created[:10], '%Y-%M-%d').date(), 'action_by': history.author, 'from': item.fromString, 'to': item.toString}
                project = project.append(action, ignore_index=True)

os.system('clear')
project = project.drop_duplicates(['issue', 'date'], keep='last').sort_values(
    by=['issue', 'date']).reset_index(drop=True)
print(project.head(5))
