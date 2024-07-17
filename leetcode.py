import json
import random
import requests


class LeetcodeProblem:
    def __init__(self):
        self.session = requests.Session()
        self.user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        self.base_url = 'https://leetcode.com/problems/'
        self.problem_dict = self.get_problems()

    def get_problems(self):
        easy_problems = []
        medium_problems = []
        hard_problems = []
        url = "https://leetcode.com/api/problems/all/"
        headers = {'User-Agent': self.user_agent, 'Connection': 'keep-alive'}
        resp = self.session.get(url, headers = headers, timeout = 10)
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
        return {
            'easy': easy_problems,
            'medium': medium_problems,
            'hard': hard_problems
        }

    def get_problem_url(self, level=0):
        easy_problems, medium_problems, hard_problems = self.problem_dict['easy'], self.problem_dict['medium'], self.problem_dict['hard']

        if level == 1:
            random_idx = random.randint(0, len(easy_problems)-1)
            question_name = easy_problems[random_idx]
            return question_name, (self.base_url + question_name)
        elif level == 2:
            random_idx = random.randint(0, len(medium_problems)-1)
            question_name = medium_problems[random_idx]
            return question_name, (self.base_url + question_name)
        elif level == 3:
            random_idx = random.randint(0, len(hard_problems)-1)
            question_name = medium_problems[random_idx]
            return question_name, (self.base_url + question_name)
        
        # Random level
        random_difficulty = ['easy', 'medium', 'hard'][random.randint(0, 2)]
        random_idx = random.randint(0, len(self.problem_dict[random_difficulty])-1)
        question_name = self.problem_dict[random_difficulty][random_idx]
        return question_name, (self.base_url + question_name)


