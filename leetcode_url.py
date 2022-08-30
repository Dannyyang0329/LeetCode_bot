import json
import random
import requests

session = requests.Session()
user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'

base_url = 'https://leetcode.com/problems/'

def get_problems():
    easy_problems = []
    medium_problems = []
    hard_problems = []

    url = "https://leetcode.com/api/problems/all/"

    headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
    resp = session.get(url, headers = headers, timeout = 10)
       
    question_list = json.loads(resp.content.decode('utf-8'))

    for question in question_list['stat_status_pairs']:
        if question['paid_only']:
            continue

        question_slug = question['stat']['question__title_slug']
        question_level = question['difficulty']['level']

        if question_level == 1:
            easy_problems.append(question_slug)
        elif question_level == 2:
            medium_problems.append(question_slug)
        elif question_level == 3:
            hard_problems.append(question_slug)

    return easy_problems, medium_problems, hard_problems

def get_problem_url(level = 0, problems = None):
    if problems == None:
        easy_problems, medium_problems, hard_problems = get_problems()
    else:
        easy_problems = problems[0]
        medium_problems = problems[1]
        hard_problems = problems[2]


    if level == 1:
        random_idx = random.randint(0, len(easy_problems)-1)
        question_name = easy_problems[random_idx]
        return question_name, (base_url + question_name)
    elif level == 2:
        random_idx = random.randint(0, len(medium_problems)-1)
        question_name = medium_problems[random_idx]
        return question_name, (base_url + question_name)
    elif level == 3:
        random_idx = random.randint(0, len(hard_problems)-1)
        question_name = medium_problems[random_idx]
        return question_name, (base_url + question_name)

    return get_problem_url(random.randint(1, 3), problems = [easy_problems, medium_problems, hard_problems])


