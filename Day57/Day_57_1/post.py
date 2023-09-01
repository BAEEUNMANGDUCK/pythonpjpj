import requests
class Post:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url).json()


    def get_posts(self):
        return self.response


    def get_each_post(self, id):
        return self.response[id-1]

