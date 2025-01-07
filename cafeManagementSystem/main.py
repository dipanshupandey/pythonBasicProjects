class cafe:
    def __init__(self):
        print("Welcome to our Cafe")
        self.menuItem={
            "pizza":10,
            "pasta":7,
            "sandwich":4,
            "coffee":2,
            "garlic bread":5
        }
        self.total=0
        self.flag=1
        self.menu()


    def menu(self):
        for x,y in self.menuItem.items():
            print(f'{x}- ${y}')
        self.order()
    def order(self):
        while self.flag == 1:
            price=self.menuItem[input("Enter item you want ").lower()]
            self.total+=(int(input("Enter Quantity ")))*price
            if (input("Anything else? Yes/No ")).lower()=="no":
                print(f"Your total is ${self.total}")
                print("Thanks for visiting!")
                self.flag=0
x=cafe()
