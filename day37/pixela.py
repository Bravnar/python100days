
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
USERNAME = getenv('USERNAME')
PIXELA_URL = "https://pixe.la/v1/users"

GREEN = "shibafu"
RED = "momiji"
BLUE = "sora"
YELLOW = "ichou"
PURPLE = "ajisai"
BLACK = "kuro"

class PixelaManager:
    def __init__(self, token: str = None, account: str = None):
        if (not token or not account):
            print("Token and Account not provided")
            self._token, self._account = self._get_credentials()
        else:
            self._token = token
            self._account = account
        
        # User
        self._user_ep = f"{PIXELA_URL}"
        # Graphs
        self._graph_ep = f"{PIXELA_URL}/{self._account}"
        self._headers = {"X-USER-TOKEN": self._account}
        
    def view_user_profile(self, username: str):
        r = requests.get(f"https://pixe.la/@{username}")
        return r.text
            
    def update_user_profile(self, username: str, **kwargs):
        parameters = kwargs
        with requests.put(f"pixe.la/@{username}", json=parameters, headers=headers) as r:
            return r.text
         
    def create_graph(self, id: str, name: str, unit: str, type: str, color: str, **kwargs):
        parameters = {
            "id": id,
            "name": name,
            "unit": unit,
            "type": type,
            "color": color,
            **kwargs
        }
        with requests.post(f"{self._graph_ep}/", json=parameters, headers=self._headers) as r:
            return r.text
        
    def update_graph(self, graphID: str,  **kwargs):
        r = requests.put(f"{self._graph_ep}/{graphID}", json=kwargs)
        return r.text
    
    def delete_graph(self, graphID: str):
        r = requests.delete(f"{self._graph_ep}/{graphID}")
        return r.text
    
    def post_pixel(self, graphID: str, date: str, quantity: str, **kwargs):
        params = {
            "date": date,
            "quantity": quantity,
            **kwargs
        }
        r = requests.post(f"{self._graph_ep}/{graphID}/", json=params, header=self._headers)
        return r.text
    
    
if __name__ == "__main__":
    pixManager = PixelaManager(TOKEN, USERNAME)
    r = pixManager.view_user_profile(USERNAME)
    print(r)