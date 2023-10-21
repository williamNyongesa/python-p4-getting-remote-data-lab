import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    # def load_json(self):
    #     python_list = []
    #     second_response = json.loads(self.get_response_body())
    #     for n in second_response:
    #         python_list.append(n["agency"])
    #     return python_list
    

    def load_json(self):
        python_list = []
        second_response = json.loads(self.get_response_body())
        if isinstance(second_response, list):
            for item in second_response:
                if isinstance(item, dict) and "agency" in item:
                    python_list.append(item["agency"])
        return python_list


