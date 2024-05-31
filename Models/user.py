from Database.database import database
from Utils.save import ISave

class User(ISave):
    def __init__(self, name: str, lastname: str, username: str, phone: str, password: str, email: str, city: str, birthday: str, question: str):
        super().__init__()
        self.first_name: str = name
        self.last_name: str = lastname
        self.username: str = username
        self.phone: str = phone
        self.password: str = password
        self.email: str = email
        self.city: str = city
        self.birthday: str = birthday
        self.question: str = question

        self.db = database()

    def save(self, ui):
        super().save()
        """ Save user informations to database. """
        new_user = [self.first_name, self.last_name, self.username, self.phone,
                    self.password, self.email, self.city, self.birthday, self.question]
        self.db.save_new_user(new_user, ui)
