from datetime import  datetime
date_format = "%d-%m-%Y"

category={"I":"Income",
          "E":"Expense"}

def getDate(prompt,default_date=True):
    date_str=input(prompt)
    if default_date==True and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date=datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print(f"invalid Date fromat please enter date in {date_format} format")
        return getDate(prompt,default_date)

# print(getDate("Enter DAte",True))

def getAmount():
    try:
        amount=float(input("Enter Amount"))
        if amount<=0:
            raise ValueError("Amount should be greater than zero")
        return amount
    except ValueError as e:
        print(e)
        return getAmount()

# print(getAmount())


def getCategory():
    cat=input("enter category ('I' for Income 'E' for Expense)").upper()
    if cat in category:
        return category[cat]
    else:
        print("Invalid entry")
        return getCategory()


# print(getCategory())

def getDescription():
    return input("Enter Description (optional)")

# print(getDescription())