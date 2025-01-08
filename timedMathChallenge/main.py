import random
import time
class game:
    def __init__(self):
        self.operators=["+","-","//","*"]
        self.numberOfChances=5
        self.level1Score=0
        self.level2Score=0
        self.level3Score=0

    def giveExpression(self,lower_limit=None,upper_limit=None):
        left=random.randint(lower_limit,upper_limit)
        right=random.randint(lower_limit,upper_limit)
        op=random.choice(self.operators)
        ex=(str(left)+op+str(right))
        ans=eval(ex)
        return ex,ans

    def level1(self):
        wrong=0
        input("Press Enter")
        print("level 1 started")
        print("-----------------------")
        for i in range(self.numberOfChances):
            expression,output=self.giveExpression(1,10)
            print(f"Question Number #{i+1}")
            while True:
                ans=int(input(f"{expression}="))
                if ans==output:
                    break
                else:
                    print("Wrong ans!")
                    wrong+=1

        print("-----------------------")
        print("Level 1 Ends")
        self.level1Score=10-(0.75)*wrong
        print(f"your score ={self.level1Score}/10.0")
        print("-----------------------")
        self.level2()
    def level2(self):
        wrong = 0
        input("Press Enter")
        print("level 2 started")
        print("-----------------------")
        for i in range(self.numberOfChances):
            expression,output=self.giveExpression(10,15)
            print(f"Question Number #{i+1}")
            while True:
                ans=int(input(f"{expression}="))
                if ans==output:
                    break
                else:
                    print("Wrong ans!")
                    wrong+=1

        print("-----------------------")
        print("Level 2 Ends")
        self.level2Score=10 - (0.5) * wrong
        print(f"your score ={self.level2Score}/10.0")
        print("-----------------------")
        self.level3()
    def level3(self):
        wrong = 0
        input("Press Enter")
        print("level 3 started")
        print("-----------------------")
        for i in range(self.numberOfChances):
            expression,output=self.giveExpression(15,20)
            print(f"Question Number #{i+1}")
            while True:
                ans=int(input(f"{expression}="))
                if ans==output:
                    break
                else:
                    print("Wrong ans!")
                    wrong+=1

        print("-----------------------")
        print("Level 3 Ends")
        self.level3Score=10 - (0.25) * wrong
        print(f"your score ={self.level3Score}/10.0")
        print("-----------------------")

    def start(self):
        startTime=time.time()
        print("""
        🎮 Welcome to the Ultimate Math Challenge! 🎮

        🧮 Solve math problems across 3 exciting levels!  
        ⏳ The faster you solve, the higher your score!  
        ❌ Wrong answers reduce points, so think carefully!  

        🔥 Can you master all levels and claim the Math Champion title?  
        
        """)

        self.level1()
        endTime=time.time()
        print(f"Game End!!!\nTotal score={(self.level1Score+self.level2Score+self.level3Score)/3}\nYou Finished Game in {round(endTime-startTime,2)}s")
x=game()
x.start()