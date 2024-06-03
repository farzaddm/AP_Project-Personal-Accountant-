import smtplib
import string
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, dotenv_values
from Database.database import database
import os


class email_sender:
    #? should pass the ui to it.....
    def __init__(self, ui) -> None:
        load_dotenv()
        
        self.my_email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")
        
        self.ui = ui

        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()
        self.connection.login(user=self.my_email, password=self.password)

    def random_password_generator(self) -> str:
        password = random.choices(string.ascii_lowercase, k=2)+random.choices(
            string.ascii_uppercase, k=2)+random.choices(string.digits, k=3)
        random.shuffle(password)
        return "".join(str(i) for i in password)

    def send_password(self, email: str):
        #! we put our email instead of user email for debug
        self.random_password=self.random_password_generator()
        try:
            self.connection.sendmail(from_addr=self.my_email, to_addrs="farzad.d.m84@gmail.com",
                                 msg=f"Subject: Personal Accountant App\n\nHello,\nYour temporary password: {self.random_password}")
            return self.random_password
        except smtplib.SMTPRecipientsRefused:
            self.ui.show_error("The recipient email adress is invalid.")
        finally:
            self.connection.close()

            

