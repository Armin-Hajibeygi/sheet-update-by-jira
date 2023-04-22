import pandas as pd
from datetime import datetime
from jira import JIRA
import plotly.express as px
import os
import const

server_url = const.SERVER
password = const.PASSWORD
username = const.USERNAME
project_epic = 'LG-3093'

jira = JIRA(basic_auth=(username, password), options={
    'server': server_url})

epic_jql = "key = " + project_epic
epic = jira.search_issues(epic_jql)
epic_name = epic[0].fields.customfield_10104

jql = f'"Epic Link" = {project_epic}'
issues = jira.search_issues(jql, maxResults=500)

actions = []
for issue in issues:
    changelog = jira.issue(str(issue.key), expand='changelog').changelog

    action = {'issue': str(issue.key),
              'start': datetime.strptime(str(issue.fields.created)[:19], '%Y-%m-%dT%H:%M:%S'),
              'action_by': issue.fields.reporter.displayName,
              'from': "",
              'status': "Analysis Backlog"}
    actions.append(action)

    for history in changelog.histories:
        for item in history.items:
            if item.field == 'status':
                action = {'issue': str(issue.key),
                          'start': datetime.strptime(history.created[:19], '%Y-%m-%dT%H:%M:%S'),
                          'action_by': history.author.displayName,
                          'from': item.fromString,
                          'status': item.toString}
                actions.append(action)

    if str(issue.fields.status) not in ['Done', 'Invalid']:
        action = {'issue': str(issue.key),
                  'start': datetime.now(),
                  'action_by': issue.fields.reporter.displayName,
                  'from': "",
                  'status': str(issue.fields.status)}
        actions.append(action)

df = pd.DataFrame(actions)

#df['start'] = pd.to_datetime(df['start'], utc=True)
df = df.sort_values(by=['issue', 'start'], ascending=[False, True]).reset_index(drop=True)

for i in range(0, len(df)-1):
    if (df.loc[i, 'issue'] == df.loc[i+1, 'issue']):
        df.loc[i, 'end'] = df.loc[i+1, 'start']

fig = px.timeline(df, x_start='start', x_end='end', y='issue', color='status', title=(
    epic_name + ' - Total Number of Tickets:' + str(len(df['issue'].unique()))))

epic_name = epic_name.replace(' ', '-')
fig_address = epic_name + '.html'
report_dir = 'reports/'
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

fig.write_html(os.path.join(report_dir, fig_address), auto_open=True)
