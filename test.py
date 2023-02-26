from jira import JIRA
import os, datetime
import const


username = const.USERNAME
password = const.PASSWORD

jira = JIRA (basic_auth=(username, password), options={'server':'https://dkjira.digikala.com'})
jql = "key = LG-3213"

os.system('clear')

for issue in jira.search_issues(jql, maxResults=500):
    print(issue.fields.status)
