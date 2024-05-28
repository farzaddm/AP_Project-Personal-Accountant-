from Utils.validation import Validation
from Models.user import User

class UserController():
    """ It's to connect ui to program logic. """
    def __init__(self, ui) -> None:
        self.ui = ui
        
    def sign_up(self) -> None:
        v = Validation()
        fname = self.ui.le_fname.text()
        lname = self.ui.le_lname.text() 
        phone = self.ui.le_phone.text()
        password = self.ui.le_password.text()
        email = self.ui.le_email.text()
        birthday = self.ui.le_birthday.text()
        city = self.ui.le_city.text()
        username = self.ui.le_username.text()
        security_q = self.ui.le_security_q.text()
        
        if not v.validate_name(fname):
            self.ui.le_fname.setStyleSheet("border: 1px solid red")
            self.ui.le_fname.textChanged.connect(self.change_styles_fname)
            self.ui.show_error("Invalid firstname. Only English letters are allowed.")
            return

        if not v.validate_name(lname):
            self.ui.le_lname.setStyleSheet("border: 1px solid red")
            self.ui.le_lname.textChanged.connect(self.change_styles_lname)
            self.ui.show_error("Invalid lastname. Only English letters are allowed.")
            return
        
        if not v.validate_phone(phone):
            self.ui.le_phone.setStyleSheet("border: 1px solid red")
            self.ui.le_phone.textChanged.connect(self.change_styles_phone)
            self.ui.show_error("Invalid phone number. It should start with 09 and be 11 digits long.")
            return

        if not v.validate_password(password):
            self.ui.le_password.setStyleSheet("border: 1px solid red")
            self.ui.le_password.textChanged.connect(self.change_styles_password)
            self.ui.show_error("Invalid password. It must be at least 6 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
            return

        if self.ui.le_password.text() != self.ui.le_repeat_password.text():
            self.ui.le_repeat_password.setStyleSheet("border: 1px solid red")
            self.ui.le_repeat_password.textChanged.connect(self.change_styles_repeat_password)
            self.ui.show_error("Passwords do not match.")
            return

        if not v.validate_email(email):
            self.ui.le_email.setStyleSheet("border: 1px solid red")
            self.ui.le_email.textChanged.connect(self.change_styles_email)
            self.ui.show_error("Invalid email format. Only gmail.com or yahoo.com domains are allowed.")
            return

        if not v.validate_birthday(birthday):
            self.ui.le_birthday.setStyleSheet("border: 1px solid red")
            self.ui.le_birthday.textChanged.connect(self.change_styles_birthday)
            self.ui.show_error("Invalid date of birth. Year must be between 1920 and 2005.")
            return
        
        
        if not v.validate_city(city):
            self.ui.le_city.setStyleSheet("border: 1px solid red")
            self.ui.le_city.textChanged.connect(self.change_styles_city)
            self.ui.show_error("Invalid city.")
            return
        
        user = User(fname, lname,username,phone,password,email,city,birthday,security_q)
        user.save()
    def login(self,username,password):
        login_v=Validation.valid_login(username,password)
        return login_v

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