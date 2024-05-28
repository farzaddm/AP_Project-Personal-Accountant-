import PyQt6.QtWidgets as qtw
import json

class Login:
    def __init__(self):
        self.username=""
        self.password=""
    def valid(self,user_le,pass_le):
        username=user_le.text()
        password=pass_le.text()
        with open("users_data.json","r") as file:
            data=json.load(file)
            for users in data["people"]:
                if users["username"] == username:
                    if users["password"]==password:
                        return True
                    else:
                        return False
                else:
                    return False



