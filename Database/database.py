import sqlite3
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import json
from Utils.show import Show



class database:
    """ This class is for coonecting to database.db. """

    def __init__(self) -> None:
        self.conn = sqlite3.connect("Database/database.db")
        self.cur = self.conn.cursor()

    def save_new_user(self, user_data: list[str], ui) -> None:
        """ Save user information in db file. """
        # create table if it's not already created.
        self.cur.execute("CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, first_name TEXT NOT NULL,last_name TEXT NOT NULL,email TEXT NOT NULL,password TEXT NOT NULL,phone TEXT NOT NULL,city TEXT NOT NULL,birthday TEXT NOT NULL,security_q TEXT NOT NULL,pic TEXT,PRIMARY KEY(username));")
        try:
            self.cur.execute(
                "INSERT INTO user(first_name, last_name, username, phone, password, email, city, birthday, security_q) VALUES (?,?,?,?,?,?,?,?,?);", user_data,)
        except sqlite3.IntegrityError:
            # show error message because username is our PRIMARY KEY and should be unique.
            Show(QtWidgets.QMessageBox.Icon.Critical,"This username is already chosen.","invalid username")
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
            return True
        else:
            return False

    def get_source_of_price(self, username):
        self.cur.execute(
            "SELECT category From category WHERE username=?;", (username,))
        result = self.cur.fetchall()
        return result

    def search(self, search_text: str, filter_search: dict, username: str) -> list:
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

        query = f"SELECT * FROM 'transaction' WHERE username='{username}' AND price BETWEEN {min1} AND {max1}"
        conditions = []
        
        if "group" in filter_search:
            conditions.append(f'{filter_search["group"]}="{search_text}"')
        elif search_text:
            conditions.append(f'(description LIKE "%{search_text}%" OR source_of_price="{search_text}")')

        if "type" in filter_search:
            conditions.append(f'type="{filter_search["type"]}"')

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

    def reporting(self,filter_search: dict,username: str):
        parameters=[]
        empty_part = []
        for i in filter_search:
            if filter_search[i] == "" or filter_search[i] == []:
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
                            
        query = f"SELECT * FROM 'transaction' WHERE username=? AND price BETWEEN ? AND ?"
        parameters.append(username)
        parameters.append(min1)
        parameters.append(max1)

        if "source-of-price" in filter_search:
            query+=f" AND source_of_price=?"
            parameters.append(filter_search["source-of-price"])

        if "type_price" in filter_search:
            query+=" AND (" + " OR ".join(["type_of_price = ?" for item in filter_search["type_price"]])+")"
            parameters.extend(filter_search["type_price"])
        
        result = self.cur.execute(query,parameters)
        filtered_result=[]
        if not "time" in filter_search:
            if "first_time" in filter_search:
                first_year,first_month,first_day=filter_search["first_time"].split("-")
                first_date=datetime.datetime(int(first_year), int(first_month), int(first_day))
                end_year,end_month,end_day=filter_search["end_time"].split("-")
                end_date=datetime.datetime(int(end_year), int(end_month), int(end_day))
                for row in result:
                    date=row[3]
                    year, month, day = date.split("-")
                    date = datetime.datetime(int(year), int(month), int(day))
                    if first_date.strftime("%Y-%m-%d") <= date.strftime("%Y-%m-%d") <= end_date.strftime("%Y-%m-%d"):
                        filtered_result.append(row)
                limitation={
                    "source_of_income":[],
                    "source_of_cost":[],
                    "income_price":{},
                    "cost_price":{}
                    }
                for row in filtered_result:
                    if row[1] == "income":
                        if row[4] not in limitation["source_of_income"]:
                            limitation["source_of_income"].append(row[4])
                            limitation["income_price"][row[4]]=row[2]
                        else:
                            limitation["income_price"][row[4]]+=row[2]
                    else:
                        if row[4] not in limitation["source_of_cost"]:
                            limitation["source_of_cost"].append(row[4])
                            limitation["cost_price"][row[4]]=row[2]
                        else:
                            limitation["cost_price"][row[4]]+=row[2]
                return limitation
            else:
                return False
        else:
            filtered_result=result.fetchall()

            if filter_search["time"][0] == "yearly":
                limitation={
                "source_of_income":[],
                "source_of_cost":[],
                "income_price":{},
                "cost_price":{}
                }
                
                for row in filtered_result:
                    date=row[3]
                    if int(date.split("-")[0]) == int(filter_search["time"][1]):
                        if row[1] == "income":
                            if row[4] not in limitation["source_of_income"]:
                                limitation["source_of_income"].append(row[4])
                                limitation["income_price"][row[4]]=row[2]
                            else:
                                limitation["income_price"][row[4]]+=row[2]
                        else:
                            if row[4] not in limitation["source_of_cost"]:
                                limitation["source_of_cost"].append(row[4])
                                limitation["cost_price"][row[4]]=row[2]
                            else:
                                limitation["cost_price"][row[4]]+=row[2]
            if filter_search["time"][0] == "monthly":
                limitation={
                "source_of_income":[],
                "source_of_cost":[],
                "income_price":{},
                "cost_price":{}
                }
                for row in filtered_result:
                    date=row[3]
                    now=datetime.datetime.now()
                    if int(date.split("-")[1]) == int(filter_search["time"][1]) and int(date.split("-")[0]) == now.year:
                        if row[1] == "income":
                            if row[4] not in limitation["source_of_income"]:
                                limitation["source_of_income"].append(row[4])
                                limitation["income_price"][row[4]]=row[2]
                            else:
                                limitation["income_price"][row[4]]+=row[2]
                        else:
                            if row[4] not in limitation["source_of_cost"]:
                                limitation["source_of_cost"].append(row[4])
                                limitation["cost_price"][row[4]]=row[2]
                            else:
                                limitation["cost_price"][row[4]]+=row[2]
            if filter_search["time"][0] == "daily":
                limitation={
                "source_of_income":[],
                "source_of_cost":[],
                "income_price":{},
                "cost_price":{}
                }
                for row in filtered_result:
                    date=row[3].split("-")
                    year=date[0]
                    month=date[1]
                    day=date[2]
                    now=datetime.datetime.now()
                    if int(year)==now.year and int(month) == now.month and int(day) == int(filter_search["time"][1]):
                        if row[1] == "income":
                            if row[4] not in limitation["source_of_income"]:
                                limitation["source_of_income"].append(row[4])
                                limitation["income_price"][row[4]]=row[2]
                            else:
                                limitation["income_price"][row[4]]+=row[2]
                        else:
                            if row[4] not in limitation["source_of_cost"]:
                                limitation["source_of_cost"].append(row[4])
                                limitation["cost_price"][row[4]]=row[2]
                            else:
                                limitation["cost_price"][row[4]]+=row[2]
            return limitation
    
    def get_information(self, username: str) -> tuple:
        self.cur.execute(f"SELECT * FROM user WHERE username='{username}';")
        result = self.cur.fetchone()
        return result

    def update_user(self, changes: dict, username: str) -> None:
        query = "UPDATE user SET "
        for item in changes:
            query += f"{item}='{changes[item]}', "
        query = query[:-2]
        query += f" WHERE username='{username}';"
        
        self.cur.execute(query)
        self.conn.commit()
    
    def delete_user(self, username: str) -> None:
        self.cur.execute(f"DELETE FROM user WHERE username='{username}';")
        self.conn.commit()
    
    def update_user_pic(self,username,file_name):
        result=self.cur.execute(f"UPDATE user SET pic='{file_name}' WHERE username='{username}';")
        self.conn.commit()

    def get_pic(self,username):
        result=self.cur.execute(f"SELECT pic FROM user WHERE username='{username}';")
        self.conn.commit
        return result.fetchone()

    def export_to_json(self, username: str) -> None:
        result = {}
        self.cur.execute(f"SELECT * FROM user WHERE username='{username}';")
        temp = self.cur.fetchone()
        result["info"] = {
            "username": temp[0],
            "first_name": temp[1],
            "last_name": temp[2],
            "email": temp[3],
            "password": temp[4],
            "phone": temp[5],
            "city": temp[6],
            "birthday": temp[7],
            "security_question": temp[7],
        }
        
        self.cur.execute(f"SELECT * FROM category WHERE username='{username}';")
        temp = self.cur.fetchall()
        result["category"] = []
        for i in temp:
            result["category"].append(i[1])
        
        self.cur.execute(f"SELECT * FROM 'transaction' WHERE username='{username}';")
        temp = self.cur.fetchall()
        result["transaction"] = []
        for row in temp:
            data = {
                "type": row[1],
                "price": row[2],
                "date": row[3],
                "source_of_price": row[4],
                "description": row[5],
                "type-of_price": row[6],
            }
            result["transaction"].append(data)
        
        with open(f"Backups/backup_{username}.json", "w") as file:
            json.dump(result, file)
    
    def delete_transacation(self,username):
        self.cur.execute(f"DELETE FROM 'transaction' WHERE username='{username}'")
        self.conn.commit()
        
        
        

 
                            
                            
                    

            



        
            
       
                


        




