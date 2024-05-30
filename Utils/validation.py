import re
import json
class Validation:
    """ All the functions for signup validation. """
    @staticmethod
    def validate_phone(phone: str) -> bool:
        pattern = r"09\d{9}"
        return True if re.fullmatch(pattern, phone) else False

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9]+@(gmail|yahoo).com"
        return True if re.fullmatch(pattern, email) else False

    @staticmethod
    def validate_city(city: str) -> bool:
        cities = ["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Karaj", "Qom", "Ahvaz", "Kermanshah", "Urmia", "Yazd", "Bushehr", "Semnan"]
        return city.capitalize() in cities

    @staticmethod
    def validate_name(name: str) -> bool:
        pattern = r"^[A-Za-z]+(?:\s[a-zA-Z]+)*$"
        return True if re.fullmatch(pattern, name) else False

    @staticmethod
    def validate_username(username: str) -> bool:
        return username != ""

    @staticmethod
    def validate_password(password: str) -> bool:
        return True if (len(password) >= 6 and re.search(r"[a-z]",password) and re.search(r"[A-Z]",password) and re.search(r"\d",password) and re.search(r"[!@#$%^&*(),.?|<>]",password)) else False

    @staticmethod
    def validate_birthday(date) -> bool:
        return True
    
    @staticmethod
    def valid_login(username_le,password_le) -> bool:
        username=username_le.text()
        password=password_le.text()
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

    @staticmethod
    def valid_price(price : str) -> bool:
        pattern=r"[0-9]+"
        return True if re.search(pattern,price) and price.isnumeric() else False

    @staticmethod
    def valid_description(description) -> bool:
        return True if 0<=len(description)<=100 and isinstance(description,str) else False
    

    
    