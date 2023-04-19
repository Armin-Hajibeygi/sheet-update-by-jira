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
                          'server': const.SERVER})

project_epic = 'DKFC-11516'
jql = '"Epic Link" = ' + project_epic

epic_jql = "key = " + project_epic
epic = jira.search_issues(epic_jql)
epic_name = epic[0].fields.customfield_10104

os.system('clear')

project = pd.DataFrame(
    columns=['issue', 'start', 'action_by', 'from', 'status'])

for issue in jira.search_issues(jql, maxResults=500):
    changelog = jira.issue(str(issue.key), expand='changelog').changelog
    action = {'issue': str(issue.key), 'start': datetime.strptime(
        str(issue.fields.created)[:19], '%Y-%m-%dT%H:%M:%S'), 'action_by': issue.fields.reporter.displayName, 'from': "", 'status': "Analysis Backlog"}
    project = project.append(action, ignore_index=True)

    for history in changelog.histories:
        for item in history.items:
            if item.field == 'status':
                action = {'issue': str(issue.key), 'start': datetime.strptime(
                    history.created[:19], '%Y-%m-%dT%H:%M:%S'), 'action_by': history.author, 'from': item.fromString, 'status': item.toString}
                project = project.append(action, ignore_index=True)

    if ((str(issue.fields.status) != 'Done') and (str(issue.fields.status) != 'Invalid')):
        action = {'issue': str(issue.key), 'start': datetime.now(
        ), 'action_by': issue.fields.reporter.displayName, 'from': "", 'status': str(issue.fields.status)}
        project = project.append(action, ignore_index=True)

os.system('clear')
# project = project.drop_duplicates(['issue', 'start'], keep='last')
project.sort_values(by=['issue', 'start']).reset_index(drop=True)

for i in range(0, len(project)-1):
    if (project.loc[i, 'issue'] == project.loc[i+1, 'issue']):
        project.loc[i, 'end'] = project.loc[i+1, 'start']

fig = px.timeline(project, x_start='start', x_end='end', y='issue', color='status', title=(
    epic_name + ' - Total Number of Tickets:' + str(len(project['issue'].unique()))))

# fig.update_yaxes(visible=False, showticklabels=False)

# show figure
epic_name = epic_name.replace(' ', '-')
fig_address = epic_name + '.html'
fig.write_html('reports/' + fig_address, auto_open=True)
