import random
import time
class SlotMachine:
    def __init__(self):
        self.maxLine=3
        self.minBet=1
        self.maxBet=100
        self.balance=self.enterAmount()
        self.line=self.enterLine()
        while True:
            self.bet=self.enterBet()
            if self.bet * self.line >self.balance:
                print(f"{self.line} lines * ${self.bet} = ${self.bet * self.line}. You dont have enough balance to bet on, Current Balance = ${self.balance}")
            else:
                break
        self.totalBet = self.bet * self.line
        while True:
            if (self.balance <= self.totalBet):
                print("you dont have any coins left! \n GAME OVER!")
                break
            print(f"Blance ${self.balance}")
            print(f"you are betting ${self.bet} on {self.line} lines, total bet = ${self.totalBet}")
            self.balance-=self.totalBet
            print(f"Availble Blance ${self.balance}")
            self.row=3
            self.col=3

            self.symbols={
                "🍒":2,
                "🍋":4,
                "🍊":6,
                "🍇":8
            }

            self.values = {
                "🍒": 8,
                "🍋": 6,
                "🍊": 4,
                "🍇": 2
            }

            self.columns=self.spin()
            self.printcols()
            win,line=self.score()
            print(f"yout won ${win} on lines {line}")
            self.balance+=win
            print(f"Available Balance ${self.balance}")
            if (self.balance <= self.totalBet):
                print("you dont have any coins left! \n GAME OVER!")
                break

            if input("Enter Y for Double or Nothing!").lower()  == "y" :
                x=random.randint(0,10)
                for i in range(10):
                    print(".",end=" ")
                    time.sleep(0.5)
                print()
                print(f"YOU GOT A {x}")
                if x in [2,4,6,9]:

                    print("JACKPOT!")
                    self.balance *= 2
                    print(f"BALANCE ${self.balance}")

                else:
                    print("BETTER LUCK NEXT TIME!!! BALANCE =$0")
                    self.balance=0
            if input("Enter q to quit") == 'q':
                print(f"BALANCE ${self.balance}")
                break

    def enterAmount(self):
        while 1:
            amount=input("Enter amount $")
            if amount.isdigit():
                amount=int(amount)
                if amount>0:
                    return amount
                else:
                    print("Amount cant be zero")
            else:
                print("Enter valid amount")

    def enterLine(self):
        while 1:
            line=input(f"Enter Line to bet on between 1-{self.maxLine}")
            if line.isdigit():
                line=int(line)
                if 1<=line<=self.maxLine:
                    return line
                else:
                    print("Enter valid number of lines")
            else:
                print("Enter valid Lines")

    def enterBet(self):
        while 1:
            bet=input(f"Enter Bet between {self.minBet}-{self.maxBet}")
            if bet.isdigit():
                bet=int(bet)
                if self.minBet<=bet<=self.maxBet:
                    return bet
                else:
                    print("Enter Bet in the range")
            else:
                print("Enter valid Bet")

    def spin(self):
        columns=[]
        allSymbols=[]
        for symbol,symbolCount in self.symbols.items():
            for _ in range(symbolCount):
                allSymbols.append(symbol)
        # print(allSymbols)
        # currentSymbols=allSymbols[:]
        for col in range(self.col):
            column=[]
            currentSymbols = allSymbols[:]
            for row in range(self.row):
                value=random.choice(currentSymbols)
                currentSymbols.remove(value)
                column.append(value)
            columns.append(column)
        return columns
        # print(columns)


    def printcols(self):
        columns=self.columns

        for col in columns:
            n=len(col)
            for x in range(n):
                if x != n-1:
                    print(col[x],end=" | ")
                else:
                    print(col[x],end="\n")

    def score(self):
        # self.columns, self.values, self.row, self.col
        winning =0
        winning_lines=[]
        for x in range(self.line):
            symbol=self.columns[x][0]
            for symbol_to_check in self.columns[x]:
                if symbol != symbol_to_check:
                    break
            else:
                winning+=(self.values[symbol]*self.bet)
                winning_lines.append(x+1)
                # print(symbol,self.values[symbol])
        return winning,winning_lines
SlotMachine()