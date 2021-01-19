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
        links = []
        message = ''
        for i, tag in enumerate(a_tags):
            message = message + f'{str(i+1)}. {tag.text} \n'
        print('message')
        return message

    @staticmethod
    def get_final_message(link):
        print(link)

        new_req = requests.get(link)
        soup = BeautifulSoup(new_req.text,'html.parser')
        return soup.find('article').text


