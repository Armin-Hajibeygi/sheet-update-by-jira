from jira import JIRA
import os
import const
import pandas as pd
from datetime import datetime
import plotly.express as px
import pandas as pd

username = const.USERNAME
password = const.PASSWORD

jira = JIRA(basic_auth=(username, password), options={
            'server': 'https://dkjira.digikala.com'})
jql = 'project = LG AND "Epic Link" = LG-3093'

os.system('clear')

project = pd.DataFrame(columns=['issue', 'start', 'action_by', 'from', 'to'])

for issue in jira.search_issues(jql, maxResults=500):
    changelog = jira.issue(str(issue.key), expand='changelog').changelog
    action = {'issue': str(issue.key), 'start': datetime.strptime(
                    issue.fields.created[:10], '%Y-%M-%d').date(), 'action_by': issue.fields.reporter.displayName, 'from': "", 'to': "Created"}
    project = project.append(action, ignore_index=True)
    
    for history in changelog.histories:
        for item in history.items:
            if item.field == 'status':
                action = {'issue': str(issue.key), 'start': datetime.strptime(
                    history.created[:19], '%Y-%m-%dT%H:%M:%S'), 'action_by': history.author, 'from': item.fromString, 'to': item.toString}
                project = project.append(action, ignore_index=True)

os.system('clear')
#project = project.drop_duplicates(['issue', 'start'], keep='last')
project.sort_values(by=['issue', 'start']).reset_index(drop=True)

for i in range(0, len(project)-1):
    project.loc[i, 'end'] = project.loc[i+1, 'start']

fig = px.timeline(project, x_start='start', x_end='end', y='issue', color='to' ,title='Gantt Chart')

# show figure
fig.write_html('gantt-chart.html', auto_open=True)
