import random
import datetime
import mysql.connector as ms




def Otp_Generator():
    otp_gen = random.randint(00000,99999)
    return otp_gen
def Login():
    a = "kavas2002"
    b = "Kavas@123"
    userid = input("enter the userid : ")
    password = input("enter the password")
    if userid == a and password == b:
        gen_otp = Otp_Generator()
        print(f"you otp is {gen_otp}")
        otp = int(input("enter the otp : "))
        if gen_otp == otp :
            print(" you can access account")
        else:
            print("incorrect")
    elif userid != a or password != b:
        print("userid and password are not matching")
def AccountCreate():
    acc_info = []
    First_name  = input("Enter your name as per your ID")
    Last_name  = input("Enter your name as per your ID")
    DOB = input("enter your date of birth dd-mm-yyyy")
    age = datetime.now().year - datetime.strptime(DOB, "%d-%m-%Y").year
    Email = input("enter tour mail : ")
    address = input("enter your branch district: ")
    Phone_number = int(input("enter your mobile numeber"))
    userid = input("""enter the userid "note" - this is needed to your future login so create that uniquely """)
    password = input("""enter the password "note" - this is needed to your future login so create that uniquely """)
    created_time = str(datetime.now().date())
    acc_info.append([First_name,Last_name,DOB,age,Email,address,Phone_number,userid,password,created_time])






def WelcomeUser():
    print("WELCOME TO THE BANK")
    print("    ACTION\n1 - login\n2 - new user\n3 - Exit")
    action = int(input("Enter the action : "))
    if action == 1:
        Login()
    elif action == 2:
        print("newuser")
    else:
        print(exit)

WelcomeUser()

db = ms.connect(host = "locahhost",user ="root",passwd = "Kavas@123",database = "bank")
db_object = db.cursor()