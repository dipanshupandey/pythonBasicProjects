import random

class game:
    def __init__(self):
        self.players=0
        self.players_score=[]
        self.start()

    def start(self):
        while True:
            self.players=input("Enter Number of players between 2-4: \nEnter other Number to end the game-")
            if self.players.isdigit():
                self.players=int(self.players)
                if self.players<2 or self.players>4:
                    print("GameEnd!!!")
                    break
                else:
                    print("welcome to the game")
                    self.startGame()

            else:
                print("GameEnd!!!")
                break
    def startGame(self):
        self.players_score = [0 for i in range(self.players)]
        # print(self.players_score)
        max_score=100

        while max(self.players_score)<max_score:
            for i in range(self.players):
                print(f"\nPlayer {i+1}, your turn has started\n")
                score=0
                while True:
                    choice=input(f"Player {i+1} do you want to roll dice? y/n")
                    if choice.lower() == 'n':
                        break
                    rollval=self.roll()
                    if rollval == 1:
                        print("oops! its a 1")
                        score=0
                        break
                    else:
                        score+=(rollval)
                        print(f"Your Current score is {score}")
                self.players_score[i]+=score
                print(f"Your Total score is {self.players_score[i]}")
            print("Results of round")
            for i in range(self.players):
                print(f"player {i+1} score: {self.players_score[i]}")

        print(f"\nPlayer {self.players_score.index(max(self.players_score))+1} WON! score= {max_score}\n")

    def roll(self):
        number=random.randint(1,6)
        print(f"you rolled a {number}!")
        return number


x=game()

