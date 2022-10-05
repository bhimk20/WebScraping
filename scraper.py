from msilib.schema import Condition
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:

    posted_status = 'Posted few days ago'
    posted_on = job.find('span', class_='sim-posted').text.strip()
    if posted_status not in posted_on:
        continue

    company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.strip()
    skills = job.find('span', class_='srp-skills').text.strip().replace('  ,',',')

    print(f'''Company name: {company_name} \nSkills required: {skills}
    ''')