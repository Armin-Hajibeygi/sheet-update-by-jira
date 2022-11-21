from jira import JIRA
import os


username = "armin.hajibeygi"
password = "Ahb137928!"

jira = JIRA (basic_auth=(username, password), options={'server':'https://dkjira.digikala.com'})
jql = "key = LG-2880"

os.system('clear')

for issue in jira.search_issues(jql, maxResults=500):
    print(issue.fields.assignee.name)
    
