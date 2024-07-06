import smtplib
import string
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Database.database import database
# from dotenv import load_dotenv, dotenv_values
from Database.database import database
import os


class email_sender:
    """This class is for forget password it send a temprary password to user email and then show him his password."""
    def __init__(self, ui) -> None:
        """Make the prerequisite for sending email.

        Args:
            ui (QMainWindow): it's forget password ui
        """
        load_dotenv()
        
        self.my_email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")
        
        self.ui = ui

        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(user=self.my_email, password=self.password)

    def random_password_generator(self) -> str:
        """generate a temprary password.

        Returns:
            str: password
        """
        password = random.choices(string.ascii_lowercase, k=2)+random.choices(
            string.ascii_uppercase, k=2)+random.choices(string.digits, k=3)
        random.shuffle(password)
        return "".join(str(i) for i in password)

    def send_message(self, email: str,message:str):
        """Send password to user email.

        Args:
            email (str): user email.

        Returns:
            str: temrary password to check with user input
        """
        if message == None:
        #! we put our email instead of user email for debug
            self.random_password=self.random_password_generator()
            try:
                self.connection.sendmail(from_addr=self.my_email, to_addrs=email,
                                    msg=f"Subject: Personal Accountant App\n\nHello,\nYour temporary password: {self.random_password}")
                return self.random_password
            except smtplib.SMTPRecipientsRefused:
                self.ui.show_error("The recipient email adress is invalid.")
            finally:
                self.connection.close()
        else:
            self.random_password=self.random_password_generator()
            try:
                self.connection.sendmail(from_addr=self.my_email, to_addrs=email,
                                    msg=message)
            except smtplib.SMTPRecipientsRefused:
                self.ui.show_error("The recipient email adress is invalid.")
            finally:
                self.connection.close()

            

