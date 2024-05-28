import json
import os


class User:
    def __init__(self, name: str, lastname: str, username: str, phone: int, password: str, email: str, city: str, birthday, question: str):
        self.first_name: str = name
        self.last_name: str = lastname
        self.username: str = username
        self.phone: int = phone
        self.password: str = password
        self.email: str = email
        self.city: str = city
        self.birthday = birthday
        self.question: str = question

        self.file_path = 'users_data.json'

    def save(self):
        new_user = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "phone": self.phone,
            "password": self.password,
            "email": self.email,
            "city": self.city,
            "birthday": self.birthday,
            "security_qustion": self.question
        }

        data = self.read_json_file()
        data["people"].append(new_user)
        self.write_json_file(data)

    def read_json_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as json_file:
                try:
                    return json.load(json_file)
                except:
                    return {"people": []}
        else:
            return {"people": []}

    def write_json_file(self, data):
        with open(self.file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
