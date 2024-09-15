import requests


# github.com/settings/tokens

token = "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"



class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'

    def getUser(self, username):
        response = requests.get(self.api_url+'/users/'+ username)
        return response.json()  # json.loads(response.text)

    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+ username+'/repos')
        return response.json()

    def createRepository(self, name):
        response = requests.post(self.api_url+'/user/repos?access_token='+ self.token, json={
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        return response.json()

github = Github()

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username= input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']}  follower : {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])    
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result) 
        else:
            print('yanlış seçim') 







