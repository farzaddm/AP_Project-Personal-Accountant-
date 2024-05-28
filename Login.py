import PyQt6.QtWidgets as qtw
import json

class Login:
    def __init__(self):
        self.username=""
        self.password=""
    def valid(self,user_le,pass_le):
        username=user_le.text()
        password=pass_le.text()
        with open("user.json","r") as file:
            data=json.load(file)
            if username in data:
                if password == data[username]["password"]:
                    return True
                else:
                    return False
            else:
                return False



