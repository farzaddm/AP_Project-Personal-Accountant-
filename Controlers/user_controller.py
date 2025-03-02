from Utils.validation import Validation
from PyQt6 import QtCore, QtGui, QtWidgets
from Models.user import User
from Utils.email_sender import email_sender
from Database.database import database
from Utils.show import Show

class UserController():
    """ It's to connect ui to program logic. """

    def __init__(self, ui) -> None:
        """Make prerequisites like database and validation.

        Args:
            ui (QMainWindow): The ui that's calling controller.
        """
        self.ui = ui
        self.validation = Validation()
        self.db = database()        

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
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid firstname. Only English letters are allowed.","invalid firstname")
            return

        if not self.validation.validate_name(lname):
            self.ui.le_lname.setStyleSheet("border: 1px solid red")
            self.ui.le_lname.textChanged.connect(self.change_styles_lname)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid lastname. Only English letters are allowed.","invalid lastname")
            return

        if not self.validation.validate_phone(phone):
            self.ui.le_phone.setStyleSheet("border: 1px solid red")
            self.ui.le_phone.textChanged.connect(self.change_styles_phone)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid phone number. It should start with 09 and be 11 digits long.","invalid phone number")
            return

        if not self.validation.validate_password(password):
            self.ui.le_password.setStyleSheet("border: 1px solid red")
            self.ui.le_password.textChanged.connect(
                self.change_styles_password)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid password. It must be at least 6 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.","invalid password")
            return

        if self.ui.le_password.text() != self.ui.le_repeat_password.text():
            self.ui.le_repeat_password.setStyleSheet("border: 1px solid red")
            self.ui.le_repeat_password.textChanged.connect(
                self.change_styles_repeat_password)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Passwords do not match.","invalid password")
            return

        if not self.validation.validate_email(email):
            self.ui.le_email.setStyleSheet("border: 1px solid red")
            self.ui.le_email.textChanged.connect(self.change_styles_email)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid email format. Only gmail.com or yahoo.com domains are allowed.","invalid email")
            return

        if not self.validation.validate_birthday(birthday):
            self.ui.le_birthday.setStyleSheet("border: 1px solid red")
            self.ui.le_birthday.textChanged.connect(
                self.change_styles_birthday)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid date of birth. Year must be between 1920 and 2005.","invalid date")
            return

        if not self.validation.validate_city(city):
            self.ui.le_city.setStyleSheet("border: 1px solid red")
            self.ui.le_city.textChanged.connect(self.change_styles_city)
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid city.","invalid city")
            return

        # When it comes here all validations are checked so it save the user.
        user = User(fname, lname, username, phone, password,
                    email, city, birthday, security_q)
        user.save(self.ui)
        self.ui.open_login()
    def contact_us(self) -> None:
        fname = self.ui.firstname_le.text()
        lname = self.ui.lastname_le.text()
        phone = self.ui.phonenumber_le.text()
        email = self.ui.email_le.text()

        if not self.validation.validate_name(fname):
            self.ui.firstname_le.setStyleSheet("border: 1px solid red")
            self.ui.firstname_le.textChanged.connect(lambda : self.ui.firstname_le.setStyleSheet(""))
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid firstname. Only English letters are allowed.","invalid firstname")
            return False

        if not self.validation.validate_name(lname):
            self.ui.lastname_le.setStyleSheet("border: 1px solid red")
            self.ui.lastname_le.textChanged.connect(lambda : self.ui.lastname_le.setStyleSheet(""))
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid lastname. Only English letters are allowed.","invalid lastname")
            return False

        if not self.validation.validate_phone(phone):
            self.ui.phonenumber_le.setStyleSheet("border: 1px solid red")
            self.ui.phonenumber_le.textChanged.connect(lambda : self.ui.phonenumber_le.setStyleSheet(""))
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid phone number. It should start with 09 and be 11 digits long.","invalid phone number")
            return False
        
        if not self.validation.validate_email(email):
            self.ui.email_le.setStyleSheet("border: 1px solid red")
            self.ui.email_le.textChanged.connect(lambda : self.ui.email_le.setStyleSheet(""))
            Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid email format. Only gmail.com or yahoo.com domains are allowed.","invalid email")
            return False

        return True


    def login(self, username: str, password: str) -> bool:
        """Check if username and password match or not.

        Args:
            username (str): username
            password (str): password

        Returns:
            bool: True if it match and false if not.
        """
        return self.validation.validate_login(username, password)

    def forget_password(self, username: str, security_q: str) -> bool:
        """Check if username and security question match.  

        Args:
            username (str): username
            security_q (str): security question (what is your favorit color?)

        Returns:
            bool: True if it match and false if not.
        """
        return self.validation.validate_forget_password(username, security_q)

    def get_password(self, username: str) -> str:
        """Get user password from database.

        Args:
            username (str): username

        Returns:
            str: pasword
        """
        password = self.db.find_user_password(username)
        return password

    def send_email(self, email: str="naghinjadali@gmail.com",message:str=None) -> str:
        """Send temprary password to user email.

        Args:
            email (str): User email

        Returns:
            str: temprary password
        """
        email_send = email_sender(self.ui)
        password = email_send.send_message(email,message)
        return password

    def get_email(self, username: str) -> str:
        """Get user email from database

        Args:
            username (str): username

        Returns:
            str: email
        """
        email_database = database()
        user_email = email_database.find_user_email(username)
        return user_email
    
    def get_information(self, username: str):
        """Get all user info.

        Args:
            username (str): username

        Returns:
            List: user info
        """
        return self.db.get_information(username)
    
    def update_user(self, changes: dict, username: str) -> None:
        """Update user info in database.

        Args:
            changes (dict): parts that need to be update
            username (str): username
        """
        if "email" in changes:
            if not self.validation.validate_email(changes["email"]):
                self.ui.le_email.setStyleSheet("border: 1px solid red")
                Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid email format. Only gmail.com or yahoo.com domains are allowed.","invalid email")
                self.ui.le_email.textChanged.connect(self.change_styles_email)
                del changes["email"]
        
        if "phone" in changes:
            if not self.validation.validate_phone(changes["phone"]):
                self.ui.le_phone.setStyleSheet("border: 1px solid red")
                Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid phone number. It should start with 09 and be 11 digits long.","invalid phone number")
                self.ui.le_phone.textChanged.connect(self.change_styles_phone)
                del changes["phone"]
        
        if "first_name" in changes:
            if not self.validation.validate_name(changes["first_name"]):
                self.ui.le_fname.setStyleSheet("border: 1px solid red")
                Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid firstname. Only English letters are allowed.","invalid firstname")
                self.ui.le_fname.textChanged.connect(self.change_styles_fname)
                
                del changes["first_name"]
        
        if "last_name" in changes:
            if not self.validation.validate_name(changes["last_name"]):
                self.ui.le_lname.setStyleSheet("border: 1px solid red")
                Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid lastname. Only English letters are allowed.","invalid lastname")
                self.ui.le_lname.textChanged.connect(self.change_styles_lname)
                del changes["last_name"]
        
        if "password" in changes:
            if not self.validation.validate_password(changes["password"]):
                self.ui.le_password.setStyleSheet("border: 1px solid red")
                Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid password. It must be at least 6 characters long and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.","invalid password")
                self.ui.le_password.textChanged.connect(self.change_styles_password)
                del changes["password"]
       
        if "city" in changes:
            if not self.validation.validate_city(changes["city"]):
                self.ui.le_city.setStyleSheet("border: 1px solid red")
                Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid City.","invalid city")
                self.ui.le_city.textChanged.connect(self.change_styles_city)
                del changes["city"]
        
        if "birthday" in changes:
            if not self.validation.validate_birthday(changes["birthday"]):
                self.ui.dateTimeEdit.setStyleSheet("border: 1px solid red")
                Show(QtWidgets.QMessageBox.Icon.Critical,"Invalid date of birth. Year must be between 1920 and 2005.","invalid date")
                self.ui.le_birthday.textChanged.connect(self.change_styles_birthday)
                
                del changes["birthday"]
        
        if changes:
            self.db.update_user(changes, username)
    
    def delete_user(self, username: str) -> None:
        """Delete all user info in database

        Args:
            username (str): usrname
        """
        self.db.delete_user(username)
    
    def update_user_pic(self,username: str,file_name: str):
        self.db.update_user_pic(username,file_name)
    
    def get_pic(self,username):
        return self.db.get_pic(username)

    def export_to_json(self, username: str) -> None:
        """Save all user info to json file.

        Args:
            username (str): username
        """
        self.db.export_to_json(username)

    def delete_transacation_from_db(self,username: str) -> None:
        """Delete all user transcation from database.

        Args:
            username (str): username
        """
        self.db.delete_transacation(username)
        

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
