import requests
from bs4 import BeautifulSoup


class GetContent:

    def __init__(self):
        self.url = 'https://www.geeksforgeeks.org/fundamentals-of-algorithms/'
        req = requests.get(self.url)
        self.soup = BeautifulSoup(req.text, 'html.parser')
        self.links = ['Analysis of Algorithms', 'Searching and Sorting', 'Greedy Algorithms', 'Dynamic Programming',
                      'Pattern Searching',
                      'Other String Algorithms', 'Backtracking', 'Divide and Conquer', 'Geometric Algorithms',
                      'Mathematical Algorithms', 'Bit Algorithms', 'Introduction, DFS and BFS', 'Minimum Spanning Tree',
                      'Shortest Paths', 'Connectivity', 'Hard Problems',
                      'Maximum Flow', 'Misc']
        self.list_string = ''
        for i, link in enumerate(self.links):
            self.list_string = self.list_string + f'{str(i + 1)}. {link} \n'
        self.lists = self.soup.find_all('ol')[:-4]

    @staticmethod
    def get_lists(list_string):
        print(list_string)
        return list_string

    @staticmethod
    def get_individual_links(ol):
        a_tags = ol.find_all('a')
        message = ''
        for i, tag in enumerate(a_tags):
            message = message + f'{str(i+1)}. {tag.text} \n'
        print('message')
        return message

    @staticmethod
    def get_final_message(link):
        new_req = requests.get(link)
        soup = BeautifulSoup(new_req.text, 'html.parser')
        code = soup.find_all('table')
        python_code = ''
        cpp_code = ''
        for c in code:
            if 'c++' in c.text.lower():
                cpp_code = c.text
                cpp_code = cpp_code.strip()
            if 'python' in c.text.lower():
                python_code = c.text
                python_code = python_code.strip()
        article = soup.find('article')
        title = article.find(class_='title').text
        title = '**' + title + '**'
        p_tags = article.find_all(['p', 'strong'])
        text = ''
        if python_code:
            code = python_code
        else:
            code = cpp_code
        for tag in p_tags[:-2]:
            t = tag.text.strip()
            if ' ' in t:
                text = text + t+'\n'
        message = title + '\n' + text
        return message, code
