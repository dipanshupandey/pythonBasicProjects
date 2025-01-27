import pandas as pd
import csv
from datetime import datetime
from data_entry import getDescription,getDate,getCategory,getAmount
import tkinter as tk

class CSV:
    CSV_FILE="finance_data.csv"
    columns=["date","amount","category","description"]
    FORMAT="%d-%m-%Y"
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.columns)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            write=csv.DictWriter(csvfile,fieldnames=cls.columns)
            write.writerow(new_entry)
        print("data added")

    @classmethod
    def get_transactions(cls,start,end):
        df=pd.read_csv(cls.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format="%d-%m-%Y")
        # print(df['date'].dtype)
        start_date=datetime.strptime(start,CSV.FORMAT)
        end_date=datetime.strptime(end,CSV.FORMAT)
        mask=(df['date']>=start_date) & (df['date']<=end_date)
        filtered_df=df.loc[mask]
        if filtered_df.empty:
            print("No Transaction found")
            return
        else:
            print(f"transactions between {datetime.strftime(start_date,CSV.FORMAT)} to {datetime.strftime(end_date,CSV.FORMAT)} :")

            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))
            income_sum=filtered_df[filtered_df["category"]=="Income"].amount.sum()
            expense_sum=filtered_df[filtered_df["category"]=="Expense"].amount.sum()
            saving=income_sum-expense_sum
            print(income_sum,expense_sum,saving)
CSV.initialize_csv()
def addData():
    date=getDate("Enter Date format -DD-MM-YY press enter to add todays date:")
    amount=getAmount()
    cat=getCategory()
    desc=getDescription()
    CSV.add_entry(date,amount,cat,desc)
# CSV.add_entry("15-3-2003",100000,"birthday","happybirthday")

# addData()
# addData()
# addData()

# CSV.get_transactions("15-3-2003","1-1-2026")

class GUI:
    def __init__(self):
        root=tk.Tk()
        root.title("Main")
        root.geometry("600x600")
        tk.Label(root,text="Transaction Management System ",font=("arial",18)).pack(pady=20)
        tk.Button(root,text="Add Transaction" ,width=50,height=5,command=self.openWindow1).pack(pady=20)
        tk.Button(root,text="Show Transaction" ,width=50,height=5,command=self.openWindow2).pack(pady=20)
        root.mainloop()

    def openWindow1(self):


        # def add_placeholder(entry, placeholder_text, placeholder_color="gray"):
        #     """Add placeholder text to an entry widget."""
        #     if not entry.get():
        #         entry.insert(0, placeholder_text)
        #         entry.config(fg=placeholder_color)

        def remove_placeholder(event, entry, placeholder_text, default_color="black"):
            """Remove placeholder text when the entry is focused."""
            if entry.get() == placeholder_text:
                entry.delete(0, tk.END)
                entry.config(fg=default_color)

        def setup_placeholder(entry, placeholder_text, placeholder_color="gray", default_color="black"):
            """Setup placeholder functionality for an entry widget."""
            entry.insert(0, placeholder_text)
            entry.config(fg=placeholder_color)
            entry.bind("<FocusIn>", lambda e: remove_placeholder(e, entry, placeholder_text, default_color))
            # entry.bind("<FocusOut>", lambda e: add_placeholder(entry, placeholder_text, placeholder_color))
        def setData():

            # print(date.get())
            d=date.get()
            a=Amount.get()
            c=cat.get()
            de=desc.get()
            if d == "":
                d = datetime.today().strftime("%d-%m-%Y")
            if a== "":
                a = 0
            if c== "":
                c = "N/A"
            if de == "":
                de = "N/A"


            # print(d,a,c,de)
            CSV.add_entry(d,a,c,de)
            window1.destroy()
        window1=tk.Toplevel()
        window1.title("Add Transactions")
        window1.geometry("500x550")
        tk.Label(window1, text="Add Transactions", font=("Arial", 16)).pack(pady=20)
        tk.Label(window1,text="Date :",font=("Arial",16)).pack(pady=20)
        date=tk.Entry(window1,width=30,fg="grey")
        # date.insert(0, "dd-mm-yy")
        date.pack()
        tk.Label(window1,text="Amount",font=("Arial",16)).pack(pady=20)
        Amount = tk.Entry(window1, width=30, fg="grey")
        # Amount.insert(0, "$")
        Amount.pack()
        tk.Label(window1,text="Category",font=("Arial",16)).pack(pady=20)
        cat = tk.Entry(window1, width=30, fg="grey")
        # cat.insert(0, "I for Income E for Expense")
        cat.pack()
        tk.Label(window1,text="Desciption",font=("Arial",16)).pack(pady=20)
        desc = tk.Entry(window1, width=30, fg="grey")
        # desc.insert(0, "Description (optional)")
        desc.pack()
        setup_placeholder(date,"dd-mm-yy")
        setup_placeholder(Amount,"$")
        setup_placeholder(cat,"I for Income E for Expense")
        setup_placeholder(desc,"Description (optional)")
        tk.Button(window1, text="submit",command=setData).pack(pady=10)
        tk.Button(window1, text="Close", command=window1.destroy).pack(pady=10)



    def openWindow2(self):
        window2 = tk.Toplevel()
        window2.title("Show Transactions")
        window2.geometry("500x500")
        tk.Label(window2,text="Show Transactions",font=("Arial",16)).pack(pady=20)
        tk.Button(window2,text="close",command=window2.destroy).pack(pady=20)

GUI()