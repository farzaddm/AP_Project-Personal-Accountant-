from Utils.validation import Validation
from Models.user import User
from Utils.email_sender import email_sender
from Database.database import database


class Record:
    def __init__(self, type: str, ui):
        self.type: str = type
        self.ui = ui

    def record(self, username, le_price, le_description, combo_price_type, combo_price_source):
        username: str = username
        record_v = Validation()
        price: str = le_price.text()
        description: str = le_description.text()
        type_of_price: str = combo_price_type.currentText()
        source_of_price: str = combo_price_source.currentText()

        if not record_v.validate_price(price):
            le_price.setStyleSheet("border: 1px solid red")
            le_price.textChanged.connect(
                lambda: self.change_styles_price(le_price))
            self.ui.show_error("Invalid cost . It should be Postive Number.")
            return

        if not record_v.validate_description(description):
            self.ui.le_discription.setStyleSheet("border: 1px solid red")
            self.ui.le_discription.textChanged.connect(
                self.change_styles_description)
            self.ui.show_error(
                "Invalid income . It should be lesser than 100.")
            return
        
        if not record_v.validate_type_of_price(type_of_price):
            self.ui.show_error(
                "Invalid income . Choose one of the type of income")
            return
        
        if not record_v.validate_source_of_price(source_of_price):
            self.ui.show_error(
                "Invalid income . Choose one of the source of income")
            return

        return True

    def change_styles_price(self, le_price):
        le_price.setStyleSheet("")


class UserController():
    """ It's to connect ui to program logic. """

    def __init__(self, ui) -> None:
        self.ui = ui
        self.validation = Validation()

    def sign_up(self) -> None:
        """ Check the validations of inputs and if every thing is ok save it to database. """
        fname = self.ui.le_fname.text()
        lname = self.ui.le_lname.text()
        phone = self.ui.le_phone.text()
        password = self.ui.le_password.text()
        email = self.ui.le_email.text()
        birthday = self.ui.le_birthday.text()
        city = self.ui.le_city.text()
        username = self.ui.le_username.text()
        security_q = self.ui.le_security_q.text()

        if not self.validation.validate_name(fname):
            self.ui.le_fname.setStyleSheet("border: 1px solid red")
            self.ui.le_fname.textChanged.connect(self.change_styles_fname)
            self.ui.show_error(
                "Invalid firstname. Only English letters are allowed.")
            return

        if not self.validation.validate_name(lname):
            self.ui.le_lname.setStyleSheet("border: 1px solid red")
            self.ui.le_lname.textChanged.connect(self.change_styles_lname)
            self.ui.show_error(
                "Invalid lastname. Only English letters are allowed.")
            return

        if not self.validation.validate_phone(phone):
            self.ui.le_phone.setStyleSheet("border: 1px solid red")
            self.ui.le_phone.textChanged.connect(self.change_styles_phone)
            self.ui.show_error(
                "Invalid phone number. It should start with 09 and be 11 digits long.")
            return

        if not self.validation.validate_password(password):
            self.ui.le_password.setStyleSheet("border: 1px solid red")
            self.ui.le_password.textChanged.connect(
                self.change_styles_password)
            self.ui.show_error(
                "Invalid password. It must be at least 6 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
            return

        if self.ui.le_password.text() != self.ui.le_repeat_password.text():
            self.ui.le_repeat_password.setStyleSheet("border: 1px solid red")
            self.ui.le_repeat_password.textChanged.connect(
                self.change_styles_repeat_password)
            self.ui.show_error("Passwords do not match.")
            return

        if not self.validation.validate_email(email):
            self.ui.le_email.setStyleSheet("border: 1px solid red")
            self.ui.le_email.textChanged.connect(self.change_styles_email)
            self.ui.show_error(
                "Invalid email format. Only gmail.com or yahoo.com domains are allowed.")
            return

        if not self.validation.validate_birthday(birthday):
            self.ui.le_birthday.setStyleSheet("border: 1px solid red")
            self.ui.le_birthday.textChanged.connect(
                self.change_styles_birthday)
            self.ui.show_error(
                "Invalid date of birth. Year must be between 1920 and 2005.")
            return

        if not self.validation.validate_city(city):
            self.ui.le_city.setStyleSheet("border: 1px solid red")
            self.ui.le_city.textChanged.connect(self.change_styles_city)
            self.ui.show_error("Invalid city.")
            return

        user = User(fname, lname, username, phone, password,
                    email, city, birthday, security_q)
        user.save(self.ui)
        self.ui.open_login()

    def login(self, username, password):
        return self.validation.validate_login(username, password)

    def forget_password(self, username, security_q):
        return self.validation.validate_forget_password(username, security_q)

    def get_password(self, username):
        db = database()
        password = db.find_user_password(username)
        return password

    def send_email(self, email):
        email_send = email_sender(self.ui)
        password = email_send.send_password(email)
        return password

    def get_email(self, username):
        email_database = database()
        user_email = email_database.find_user_email(username)
        return user_email

    def record_cost(self):
        Record("cost", self.ui).record(self.ui.le_cost, self.ui.le_discription,
                                       self.ui.combo_cost_type, self.ui.combo_source)

    # ---------change style ---------------

    def change_styles_fname(self):
        self.ui.le_fname.setStyleSheet("")

    def change_styles_lname(self):
        self.ui.le_lname.setStyleSheet("")

    def change_styles_phone(self):
        self.ui.le_phone.setStyleSheet("")

    def change_styles_password(self):
        self.ui.le_password.setStyleSheet("")

    def change_styles_repeat_password(self):
        self.ui.le_repeat_password.setStyleSheet("")

    def change_styles_email(self):
        self.ui.le_email.setStyleSheet("")

    def change_styles_birthday(self):
        self.ui.le_birthday.setStyleSheet("")

    def change_styles_city(self):
        self.ui.le_city.setStyleSheet("")

    def change_styles_description(self):
        self.ui.le_discription.setStyleSheet("")
