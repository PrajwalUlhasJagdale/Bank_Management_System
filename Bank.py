import pandas as pd
import numpy as np

# import 
# dt=pd.read_csv(r"E:\Sumago\Mini Project\Customer-Records.csv")
# print(dt)



class BankAccount:
    def __init__(self,customer_id,password,dt):
        self.dt=dt
        self.Customer_Id=customer_id
        self.Password=password
        self.user=self.validate()

    def validate(self):
        match=self.dt[(self.dt['CustomerId']==self.Customer_Id) & (self.dt['Password']==self.Password)]
        if not match.empty:
            return match.iloc[0]
        else:
            print("Invalid Customer ID or Password")
            return None
    def get_balance(self):
        if self.user is not None:
            return self.user['Balance']
            self.dt.to_csv("E:/Sumago/Bank_app/Customer-Records.csv", index=False)
        else:
            return None
        
    def debit(self, amount):
     if self.user['Balance'] - amount >= 500:
        self.dt.loc[self.dt['CustomerId'] == self.Customer_Id, 'Balance'] -= amount
        self.user['Balance'] -= amount  # update local too if needed
        self.dt.to_csv("E:/Sumago/Bank_app/Customer-Records.csv", index=False)

        return True
     return False

    def credit(self, amount):
       self.dt.loc[self.dt['CustomerId'] == self.Customer_Id, 'Balance'] += amount
       self.user['Balance'] += amount
       self.dt.to_csv("E:/Sumago/Bank_app/Customer-Records.csv", index=False)
         # Update the CSV file with the new balance
       return True

            

    def send_money(self, recipient_id, amount):
     if self.user is None:
        return False
     recipient_index = self.dt[self.dt['CustomerId'] == recipient_id].index
     user_index = self.dt[self.dt['CustomerId'] == self.Customer_Id].index
     if not recipient_index.empty:
         if self.user['Balance'] - amount >= 500:
            self.user['Balance'] -= amount
            self.dt.loc[user_index[0], 'Balance'] -= amount
            self.dt.loc[recipient_index[0], 'Balance'] += amount
            self.dt.to_csv("E:/Sumago/Bank_app/Customer-Records.csv", index=False)

            return True
         else:
            return False  # Not enough balance
     else:
        return False  # Recipient not found


    
           
        
