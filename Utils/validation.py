import re
from Database.database import database
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
        return True if (len(password) >= 6 and re.search(r"[a-z]",password) and re.search(r"[A-Z]",password) and re.search(r"\d",password) and re.search(r"[!@#$%^&-*(),.?|<>]",password)) else False

    @staticmethod
    def validate_birthday(date) -> bool:
        year = date.split("-")[0]
        return True if 1920 < int(year) <= 2005 else False
    
    @staticmethod
    def validate_login(username: str,password: str) -> bool:
        db = database()
        return db.check_user(username, password)
        
    
    