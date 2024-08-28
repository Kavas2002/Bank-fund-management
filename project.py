import random as r
class RBI:
    def __init__(self):
        self.rbi_amt = 10000
        self.rbi_ac = 0
class SBI(RBI):
    def __init__(self):
        self.sbi_amt = 5000
        self.sbi_ac = 0
        super().__init__()
class TN(SBI):
    def __init__(self):
        self.tn_amt = 3000
        self.tn_ac = 0
        super().__init__()
class CHE(TN):
    def __init__(self):
        self.che_amt = 1000
        self.che_ac = 0
        super().__init__()
        self.acc_details = {}
        self.acc_bal = {}
    def acc_opening(self):
        self.acc_num = r.randint(100000,999999)
        self.name = input("enter the name for acc : ")
        self.age = int(input("enter age: "))
        if self.age < 18 :
            print("not eligible")
        elif self.age >=100:
            print("age limt is 100")
        else:
            self.min_amt = int(input("first depsit? "))
            self.acc_details.update({self.acc_num:[self.name,self.age]})
            self.acc_bal.update({self.acc_num :self.min_amt})
            print(self.acc_details)
            print(self.acc_bal)
            self.che_ac += 1
            self.tn_ac += 1
            self.sbi_ac += 1
            self.rbi_ac += 1
            self.che_amt += self.min_amt
            self.tn_amt += self.min_amt
            self.sbi_amt += self.min_amt
            self.rbi_amt += self.min_amt
            print(f""" "Your account is created" "AC_NO -  {self.acc_num}" """)
    def m_credit(self):
        self.acc_num = int(input("Enter 6 Digit  Account Number: "))
        self.dep_amt = int(input("Deposit amt: "))
        self.acc_bal[self.acc_num] +=self.dep_amt
        print(f"Ac_bal ={self.acc_bal[self.acc_num]}")
        self.che_amt += self.dep_amt
        self.tn_amt +=  self.dep_amt
        self.sbi_amt +=  self.dep_amt
        self.rbi_amt +=  self.dep_amt
    def m_debit(self):
        self.withdrawl_purpose = int(input("""Withdrawl for account closing - 1
        normal Withdrawl - 2"""))
        if self.withdrawl_purpose == 1:
            self.acc_num = int(input("Enter 6 digit Account Number: "))
            print(f"{self.acc_num} - Account has ₹{self.acc_bal[self.acc_num]}")
            self.withdrawl_amt = int(input("Enter the withdrawl amount : "))
            self.acc_bal[self.acc_num] -= self.withdrawl_amt
            print(f"your Ac_bal is = ₹{self.acc_bal[self.acc_num]}")
            self.che_amt -= self.withdrawl_amt
            self.tn_amt -= self.withdrawl_amt
            self.sbi_amt -= self.withdrawl_amt
            self.rbi_amt -= self.withdrawl_amt
        elif self.withdrawl_purpose == 2:
            self.min_bal = 100
            self.acc_num = int(input("Enter 6 digit Account Number: "))
            print(f"{self.acc_num} - Account has ₹{self.acc_bal[self.acc_num]}")
            self.withdrawl_amt = int(input("Enter the withdrawl amount : "))
            if self.min_bal > self.acc_bal[self.acc_num] - self.withdrawl_amt:
                print(f"you can withdrawl{self.min_bal-self.acc_bal[self.acc_num]} ")
            elif self.acc_bal[self.acc_num] == 0:
                print("""account is zero 
                         first deposit some amount""")
            else:
                self.acc_bal[self.acc_num] -= self.withdrawl_amt
                print(f"your Ac_bal is = ₹{self.acc_bal[self.acc_num]}")
                self.che_amt -= self.withdrawl_amt
                self.tn_amt -=self.withdrawl_amt
                self.sbi_amt -=self.withdrawl_amt
                self.rbi_amt -= self.withdrawl_amt
    def acc_closing(self):
        self.acc_num = int(input("Enter your account number : "))
        if self.acc_bal[self.acc_num] !=0:
            print(f"your account has ₹{self.acc_bal[self.acc_num]}first withdrawl it")
        else:
            self.acc_details.pop(self.acc_num)
            self.acc_bal.pop(self.acc_num)
            self.che_ac -= 1
            self.tn_ac -= 1
            self.sbi_ac -= 1
            self.rbi_ac -= 1
r1 = open(r"files.Acc_details.txt","r")
r2 = open(r"files.Acc_bal.txt","r")
r3 = open(r"files.chennai branch .txt","r")
y1 = eval(r1.read())
y2 = eval(r2.read())
y3 = eval(r3.read())
print(y1)
print(y2)
print(y3)
x = CHE()
x.acc_details = y1
x.acc_bal = y2
x.che_ac = int(y3[0])
x.che_amt = int(y3[1])
x.tn_ac = int(y3[2])
x.tn_amt = int(y3[3])
x.sbi_ac = int(y3[4])
x.sbi_amt = int(y3[5])
x.rbi_ac =int(y3[6])
x.rbi_amt =int(y3[7])
while True:
    p = int(input("enter 1-acc_open,2-acc_close,3-m_credit,4-m_debit,0 - TO EXit"))
    if p == 1:
        x.acc_opening()
    elif p == 2:
        x.acc_closing()
    elif p == 3:
        x.m_credit()
    elif p == 4:
        x.m_debit()
    elif p==0:
        print("leaving the bank")
        break
    else:
        print("invalid input")
w1 = open(r"files.Acc_details.txt","w")
w2 = open(r"files.Acc_bal.txt",'w')
w3 = open(r"files.chennai branch .txt","w")
l1 = str(x.acc_details)
l2 = str(x.acc_bal)
l3 = [str(x.che_ac),str(x.che_amt),str(x.che_ac),str(x.che_amt),str(x.che_ac),str(x.sbi_amt),str(x.che_ac),str(x.rbi_amt)]
w1.write(str(l1))
w2.write(str(l2))
w3.write(str(l3))
print(x.che_ac)
print(x.che_amt)
print(x.tn_ac)
print(x.tn_amt)
print(x.sbi_ac)
print(x.sbi_amt)
print(x.rbi_ac)
print(x.rbi_amt)













