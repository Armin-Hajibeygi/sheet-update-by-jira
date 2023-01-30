from jira import JIRA
import os, datetime


username = "armin.hajibeygi"
password = "FaithBudgetWill137928!"

jira = JIRA (basic_auth=(username, password), options={'server':'https://dkjira.digikala.com'})
jql = "key = LG-3201"

os.system('clear')

for issue in jira.search_issues(jql, maxResults=500):
    print(issue.fields.customfield_10801)
    complete_date = issue.fields.customfield_10801
    year = int(complete_date[:4])
    month = int(complete_date[5:7])
    day = int(complete_date[8:10])
    hour = int(complete_date[11:13])
    minutes = int(complete_date[14:16])
    time = datetime.datetime(year, month, day, hour, minutes)
    second_time = datetime.datetime(2023, 1, 30, 19, 20)
    diff = second_time - time
    if (second_time < time):
        print("Yes")
    
