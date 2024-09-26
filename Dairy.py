#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import datetime
import pandas as pd

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def get_customer_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer ID: {self.customer_id}")

class Bill:
    def __init__(self, customer, bill_no, from_date, to_date):
        self.customer = customer
        self.bill_no = bill_no
        self.from_date = from_date
        self.to_date = to_date
        self.morning_milk = 0
        self.evening_milk = 0
        self.total_milk = 0
        self.total_amount = 0
        self.deposit = 0
        self.feed_amount = 0
        self.feed_paid = 0
        self.feed_remaining = 0
        self.bank_amount = 0
        self.bank_paid = 0
        self.bank_remaining = 0
        self.other_paid = 0
        self.total_deduction = 0
        self.remaining_amount = 0

    def take_user_input(self):
        self.morning_milk = float(input("Enter morning milk quantity: "))
        self.evening_milk = float(input("Enter evening milk quantity: "))
        self.total_milk = self.morning_milk + self.evening_milk
        self.total_amount = float(input("Enter total amount: "))
        self.deposit = float(input("Enter deposit amount: "))
        self.feed_amount = float(input("Enter feed amount: "))
        self.feed_paid = float(input("Enter feed paid amount: "))
        self.bank_amount = float(input("Enter bank amount: "))
        self.bank_paid = float(input("Enter bank paid amount: "))
        self.other_paid = float(input("Enter other paid amount: "))
        self.total_deduction = self.deposit + self.feed_paid + self.bank_paid + self.other_paid
        self.remaining_amount = self.total_amount - self.total_deduction

    def generate_bill(self):
        bill_data = {
            "Bill No": [self.bill_no],
            "From Date": [self.from_date.strftime('%d/%m/%y')],
            "To Date": [self.to_date.strftime('%d/%m/%y')],
            "Morning Milk": [self.format_decimal(self.morning_milk)],
            "Evening Milk": [self.format_decimal(self.evening_milk)],
            "Total Milk": [self.format_decimal(self.total_milk)],
            "Total Amount": [self.format_decimal(self.total_amount)],
            "Deposit": [self.format_decimal(self.deposit)],
            "Feed Amount": [self.format_decimal(self.feed_amount)],
            "Feed Paid": [self.format_decimal(self.feed_paid)],
            "Feed Remaining": [self.format_decimal(self.feed_remaining)],
            "Bank Amount": [self.format_decimal(self.bank_amount)],
            "Bank Paid": [self.format_decimal(self.bank_paid)],
            "Bank Remaining": [self.format_decimal(self.bank_remaining)],
            "Other Paid": [self.format_decimal(self.other_paid)],
            "Total Deduction": [self.format_decimal(self.total_deduction)],
            "Remaining Amount": [self.format_decimal(self.remaining_amount)]
        }

        df = pd.DataFrame(bill_data)
        df.to_csv(f'bill_{self.customer.customer_id}_{self.bill_no}.csv', index=False)
        print(f"\nBill saved as CSV: bill_{self.customer.customer_id}_{self.bill_no}.csv")
        print(df)

    def format_decimal(self, value):
        return format(value, '.2f')

# Taking the number of customers as input
num_customers = int(input("Enter the number of customers: "))

# Loop through each customer
for _ in range(num_customers):
    # Taking customer information input
    customer_name = input("\nEnter customer name: ")
    customer_id = int(input("Enter customer ID: "))
    customer = Customer(customer_name, customer_id)
    customer.get_customer_info()

    # Taking bill information input
    bill_no = int(input("\nEnter Bill No: "))
    from_date_str = input("Enter From Date (dd/mm/yy): ")
    to_date_str = input("Enter To Date (dd/mm/yy): ")
    from_date = datetime.strptime(from_date_str, "%d/%m/%y")
    to_date = datetime.strptime(to_date_str, "%d/%m/%y")

    # Creating Bill object, taking user input, generating the bill, and saving it to a DataFrame
    bill = Bill(customer, bill_no, from_date, to_date)
    bill.take_user_input()
    bill.generate_bill()


# In[ ]:




