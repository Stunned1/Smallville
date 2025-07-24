import requests
import json


class modelLogic:

    def __init__(self,
                 name: str = "User",  # Make sure to give it a name!
                 model: str = "deepseek-r1:32b"
                 ):

        self.name = name

        self.system_role = f"""test"""

        self.model = model

        self.data = {
            "model": self.model,
            "messages": [
                {"role": "SYSTEM", "content": self.system_role}
            ],
            "stream": False
        }
        self.url = "http://localhost:11434/api/chat"

        self.headers = {
            "Content-Type": "application/json"
        }

    def send_prompt(self, user_input):
        self.data["messages"].append({"role": "user", "content": user_input})
        output = requests.post(self.url, headers=self.headers, data=json.dumps(self.data))
        try:
            response_json = output.json()
            assistant_response = response_json["message"]["content"]
            self.data["messages"].append({"role": self.name, "content": assistant_response})
            assistant_json = json.loads(assistant_response)
            output = assistant_json["Content"]
        except:
            return output.status_code, output.text
