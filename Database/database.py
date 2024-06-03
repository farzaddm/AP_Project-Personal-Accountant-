import sqlite3
import datetime
from dateutil.relativedelta import relativedelta



class database:
    """ This class is for coonecting to database.db. """

    def __init__(self) -> None:
        self.conn = sqlite3.connect("Database/database.db")
        self.cur = self.conn.cursor()

    def save_new_user(self, user_data: list[str], ui) -> None:
        """ Save user information in db file. """
        # create table if it's not already created.
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, first_name TEXT NOT NULL,last_name TEXT NOT NULL,email TEXT NOT NULL,password TEXT NOT NULL,phone TEXT NOT NULL,city TEXT NOT NULL,birthday TEXT NOT NULL,security_q TEXT NOT NULL,PRIMARY KEY(username));")
        try:
            self.cur.execute(
                "INSERT INTO user(first_name, last_name, username, phone, password, email, city, birthday, security_q) VALUES (?,?,?,?,?,?,?,?,?);", user_data,)
        except sqlite3.IntegrityError:
            # show error message because username is our PRIMARY KEY and should be unique.
            ui.show_error("This username is already chosen.")
        self.conn.commit()

    def save_new_transaction(self, transaction_data: list) -> None:
        """ Save user information in db file. """
        # create table if it's not already created.
        self.cur.execute("""
CREATE TABLE IF NOT EXISTS 'transaction'(
    username TEXT NOT NULL,
    type TEXT NOT NULL,
    price INTEGER NOT NULL,
    date TEXT NOT NULL,
    source_of_price TEXT NOT NULL,
    description TEXT NOT NULL,
    type_of_price TEXT NOT NULL,
    FOREIGN KEY(username) REFERENCES user(username)
);
""")
        self.cur.execute(
            "INSERT INTO 'transaction'(username, type, price, date, source_of_price, description, type_of_price) VALUES (?,?,?,?,?,?,?);", transaction_data,)
        self.conn.commit()

    def check_user(self, username: str, password: str) -> bool:
        self.cur.execute(
            "SELECT * From user WHERE username=? AND password=?;", (username, password))
        result = self.cur.fetchone()

        return True if result else False

    def check_security_question(self, username: str, security_q: str) -> bool:
        self.cur.execute(
            "SELECT * From user WHERE username=? AND security_q=?;", (username, security_q))
        result = self.cur.fetchone()

        return True if result else False

    def find_user_email(self, username: str) -> str:
        self.cur.execute("SELECT * From user WHERE username=?;", (username,))
        result = self.cur.fetchone()
        user_email = result[3]
        return user_email

    def find_user_password(self, username: str) -> str:
        self.cur.execute("SELECT * From user WHERE username=?;", (username,))
        result = self.cur.fetchone()
        password = result[4]
        return password

    def check_category_duplicate(self, username: str, category: str) -> bool:
        self.cur.execute(
            "SELECT * FROM category WHERE username=? AND category=?", (username, category))
        result = self.cur.fetchone()
        return False if result else True

    def add_category(self, username: str, category: str):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS category(username TEXT NOT NULL, category TEXT NOT NULL);")
        if self.check_category_duplicate(username, category):
            self.cur.execute(
                "INSERT INTO category(username, category) VALUES (?,?);", (username, category))
            self.conn.commit()
            print(1)
        else:
            print(0)

    def get_source_of_price(self, username):
        self.cur.execute(
            "SELECT category From category WHERE username=?;", (username,))
        result = self.cur.fetchall()
        return result

    def search(self, search_text: str, filter_search: str) -> list:
        empty_part = []
        for i in filter_search:
            if filter_search[i] == "":
                empty_part.append(i)

        for i in empty_part:
            del filter_search[i]

        if "min_amount" in filter_search:
            min1 = filter_search["min_amount"]
            del filter_search["min_amount"]
        else:
            min1 = 0

        if "max_amount" in filter_search:
            max1 = filter_search["max_amount"]
            del filter_search["max_amount"]
        else:
            max1 = 9999999999

        query = f"SELECT * FROM 'transaction' WHERE price BETWEEN {min1} AND {max1}"
        conditions = []

        if "type" in filter_search:
            conditions.append(f'type="{filter_search["type"]}"')

        if "group" in filter_search:
            conditions.append(f'{filter_search["group"]}="{search_text}"')

        if "type_price" in filter_search:
            conditions.append(f'type_of_price="{filter_search["type_price"]}"')

        if conditions:
            query += ' AND ' + ' AND '.join(conditions)
        query += ";"

        self.cur.execute(query)
        result = self.cur.fetchall()

        filtered_result = []
        if "time" in filter_search:
            today = datetime.datetime.today()
            
            for row in result:
                date = row[3]
                year, month, day = date.split("-")
                date = datetime.datetime(int(year), int(month), int(day))
                if filter_search["time"] == "yearly":
                    date2 = today - relativedelta(years=1)
                    if date2.strftime("%Y-%m-%d") <= date.strftime("%Y-%m-%d") <= today.strftime("%Y-%m-%d"):
                        filtered_result.append(row)
                if filter_search["time"] == "monthly":
                    date2 = today - relativedelta(months=1)
                    if date2.strftime("%Y-%m-%d") <= date.strftime("%Y-%m-%d") <= today.strftime("%Y-%m-%d"):
                        filtered_result.append(row)
                if filter_search["time"] == "daily":
                    date2 = today - relativedelta(days=1)
                    if date2.strftime("%Y-%m-%d") <= date.strftime("%Y-%m-%d") <= today.strftime("%Y-%m-%d"):
                        filtered_result.append(row)
        
        return filtered_result if "time" in filter_search else result

                            


