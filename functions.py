import random
from datetime import datetime
import mysql.connector as ms
db = ms.connect(host = "localhost",user ="root",passwd = "Kavas@123",database = "bank")
db_object = db.cursor()
# db_object.execute("""create table Account(
#                 Account_No bigint primary key,
#                 customer_id varchar(100) not null,
#                 balance DECIMAL(15, 2) DEFAULT 0.00,
#                 opened_date DATE,
#                 FOREIGN KEY (customer_id) REFERENCES Customer(customerid)
#             )""")

class InvalidAge(Exception):
    def __init__(self,message):
        self.message = message
class InvalidNunber(Exception):
    def __init__(self,message):
        self.message = message
def Otp_Generator():
    otp_gen = random.randint(00000,99999)
    return otp_gen
def Login():
    Account_num = int(input("enter the account number"))
    
    
    query  =f"""select a.Account_no,c.customerid,c.password,c.Email
                from customer c
                join account a
                on c.customerid = a.customer_id
                where a.Account_no ={Account_num} ;"""
    db_object.execute(query)
    auth_details= db_object.fetchall()
    try:
        fetch_user_id = auth_details[0][1]
        fetch_pass_word = auth_details[0][2]
    except IndexError as IE:
        print(f"This because your Account_NO {Account_num} not found")
    else:
        userid = input("enter the userid : ")
        password = input("enter the password")
        if userid == fetch_user_id and password == fetch_pass_word:
            gen_otp = 23456
            print(f"you otp is {gen_otp}")
            otp = int(input("enter the otp : "))
            if gen_otp == otp :
                deposit(Account_num)
            else:
                print("incorrect")
        elif userid != a or password != b:
            print("userid and password are not matching")
def AccountCreate():
    DOB = input("enter your date of birth dd-mm-yyyy : ")
    try:
        date = datetime.strptime(DOB,"%d-%m-%Y")
        date_format = date.strftime("%Y-%m-%d")

    except ValueError as vA:
        print("you need to enter date as DD-MM-YYYY")
    try:
        age = datetime.now().year - datetime.strptime(DOB,"%d-%m-%Y").year
        if age < 18:
            raise InvalidAge("age is less than 18")
    except InvalidAge as a:
        print(a)
    else:
        First_name  = input("Enter your first name as per your ID : ")
        Last_name  = input("Enter your last name as per your ID : ")
        Email = input("enter tour mail : ")
        address =input("enter your branch district : ")
        while True:
            try: 
                Phone_number = int(input("enter your mobile number : "))
                if len(str(Phone_number)) !=10:
                    raise InvalidNumber("Please Enter 10 Digit Phone number")
            except InvalidNumber as num:
                print(num)
            else:
                break
        userid = input("""enter the userid "note" - this is needed to your future login so create that uniquely :  """)
        password = input("""enter the password "note" - this is needed to your future login so create that uniquely :  """)
        created_date = str(datetime.now().date())
        Account_No = random.randint(10000000,99999999)
        initial_deposit = float(input("enter the amount for account opening" ))
        query = "insert into customer (customerid,First_name,Last_name,DOB,age,Email,address,Phone_number,password,created_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        query2 = "insert into Account (Account_no,customer_id,balance,opened_date) values (%s,%s,%s,%s)"
        customer_details = (userid,First_name,Last_name,date_format,age,Email,address,Phone_number,password,created_date)
        acc_details = (Account_No,userid,initial_deposit,created_date)
        db_object.execute(query,customer_details)
        db_object.execute(query2,acc_details)
def deposit(Account_num):
    balance_query = f"select balance from account where Account_no = {Account_num}"
    db_object.execute(balance_query)
    acc_balance = db_object.fetchall()
    balance_amt = float(acc_balance[0][0])
    print(f"Account Balance is {balance_amt}")
    deposit_amt = float(input("Enter the Amount : "))
    balance_amt+=deposit_amt
    update_balance_query = f""" update account 
                                set balance = {balance_amt}
                                where Account_no = {Account_num}
                            """
    db_object.execute(update_balance_query)


    





def WelcomeUser():
    print("WELCOME TO THE BANK")
    print("    ACTION\n1 - login\n2 - new user\n3 - Exit")
    action = int(input("Enter the action : "))
    if action == 1:
        Login()
    elif action == 2:
        AccountCreate()
    else:
        print(exit)

WelcomeUser()
db.commit()
print("added the details")

