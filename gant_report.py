import pandas as pd
from datetime import datetime
from jira import JIRA
import plotly.express as px
import os
import const


def create_gantt(issues, title='Gantt Chart', start_date=datetime.min):
    server_url = const.SERVER
    password = const.PASSWORD
    username = const.USERNAME
    jira = JIRA(basic_auth=(username, password), options={
        'server': server_url})
    
    first_step = "Analysis Backlog"
    ignored_steps = ['Done', 'Invalid']

    actions = []
    for issue in issues:
        changelog = jira.issue(str(issue.key), expand='changelog').changelog

        start_time = datetime.strptime(str(issue.fields.created)[:19], '%Y-%m-%dT%H:%M:%S')
        if start_time > start_date:
            action = {'issue': str(issue.key),
                      'start': datetime.strptime(str(issue.fields.created)[:19], '%Y-%m-%dT%H:%M:%S'),
                      'action_by': issue.fields.reporter.displayName,
                      'from': "",
                      'status': first_step}
            actions.append(action)

        for history in changelog.histories:
            for item in history.items:
                if item.field == 'status':
                    start_time = datetime.strptime(history.created[:19], '%Y-%m-%dT%H:%M:%S')
                    if start_time > start_date:
                        action = {'issue': str(issue.key),
                                  'start': datetime.strptime(history.created[:19], '%Y-%m-%dT%H:%M:%S'),
                                  'action_by': history.author.displayName,
                                  'from': item.fromString,
                                  'status': item.toString}
                        actions.append(action)

        if str(issue.fields.status) not in ignored_steps:
            start_time = datetime.now()
            if start_time > start_date:
                action = {'issue': str(issue.key),
                          'start': datetime.now(),
                          'action_by': issue.fields.reporter.displayName,
                          'from': "",
                          'status': str(issue.fields.status)}
                actions.append(action)

    df = pd.DataFrame(actions)

    # df['start'] = pd.to_datetime(df['start'], utc=True)
    df = df.sort_values(by=['issue', 'start'], ascending=[False, True]).reset_index(drop=True)

    for i in range(0, len(df) - 1):
        if df.loc[i, 'issue'] == df.loc[i + 1, 'issue']:
            df.loc[i, 'end'] = df.loc[i + 1, 'start']

    fig = px.timeline(df, x_start='start', x_end='end', y='issue', color='status', title=(
            title + ' - Total Number of Tickets:' + str(len(df['issue'].unique()))))

    title = title.replace(' ', '-')
    fig_address = title + '.html'
    report_dir = 'reports/'
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)

    fig.write_html(os.path.join(report_dir, fig_address), auto_open=True)
