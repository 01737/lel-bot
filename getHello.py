import requests, json
import base64
import sys, os

class HelloWorld():
    def make_request(self, url):
        token = os.getenv("GITTOKEN")

        key = {'Authorization':'token ' + token}
        resposta = requests.get(url, headers=key)

        if resposta.status_code == 200:
            return resposta.json()
        else:
            return resposta.status_code
    
    def print_hello(self, lang):
        response = self.make_request(f'https://api.github.com/search/code?q=repo:leachim6/hello-world+filename:{lang}')

        if type(response) is not int:
            for i in range(len(response["items"])):
                if lang in response["items"][i]["name"]:
                    file = self.make_request(response["items"][i]["url"])
                    fileName = file["name"]
                    contents = file["content"]

                    return [base64.b64decode(contents).decode(), fileName]
                    break
        else:
            return str(response)