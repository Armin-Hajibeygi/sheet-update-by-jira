from gant_report import create_gantt
import const
from jira import JIRA

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

create_gantt(issues, epic_name)
