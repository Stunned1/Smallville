import requests
import json



#This class covers the Interface of the LLM and how we will get inputs and outputs to and from the LLM
class ModelLogic:

    def __init__(self,
                 context, #make this a formatted string please
                 name: str = "User",  # Make sure to give it a name!
                 model: str = "deepseek-r1:32b"
                 ):

        self.name = name #name of the agent

        self.context = context #the characters initial background

        self.model = model

        self.data = { #data structured in JSON that will be sent to the localhost Ollama API.
            "model": self.model,
            "messages": [
                {"role": "SYSTEM", "content": self.context}
            ],
            "stream": False
        }
        self.url = "http://localhost:11434/api/chat"

        self.headers = {
            "Content-Type": "application/json"
        }

    #Sends prompt to LLM (needs changes)
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
