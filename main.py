from bs4 import BeautifulSoup
import requests
import time
import os

print('Put skill you are not familiar with: ')
unfamiliar_skill = input('>').strip().lower()
print(f'You are not familiar with "{unfamiliar_skill}"')

os.makedirs('posts', exist_ok=True)  # Make sure folder exists

def find_jobs(unfamiliar_skill):
    html_text = requests.get(
        'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation='
    ).text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li')

    for index, job in enumerate(jobs):
        posting_time_tag = job.find('span', class_='posting-time')
        if not posting_time_tag:
            continue
        posting_time = posting_time_tag.text.strip()

        if 'few' in posting_time.lower() or 'today' in posting_time.lower():
            continue

        company_tag = job.find('span', class_='srp-comp-name')
        if not company_tag:
            continue
        company_name = company_tag.text.strip()

        more_info = job.div.a['href']

        skills_tags = job.select('div.srp-keyskills a')
        skills = [tag.text.strip() for tag in skills_tags]

        exp_tag = job.find('div', class_='srp-exp')
        experience = exp_tag.text.strip() if exp_tag else 'Not specified'

        # Filter out unfamiliar skill
        if not any(unfamiliar_skill in skill.lower() for skill in skills):
            with open(f'posts/{index}.txt', 'w', encoding='utf-8') as f:
                f.write(f'''
                    company: {company_name}
                    skills: {', '.join(skills)}
                    experience: {experience}
                    posting time: {posting_time}
                    more info: {more_info}
                    ''')
            print(f'Job post saved to posts/{index}.txt')

if __name__ == '__main__':
    while True:
        find_jobs(unfamiliar_skill)
        time_wait = 10
        print(f'Waiting for {time_wait} minutes before the next search...')
        time.sleep(time_wait * 60)
