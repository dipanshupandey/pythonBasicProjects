import tkinter
import random

ROW=25
COL=25
TILE_SIZE=25
WINDOW_WIDTH=TILE_SIZE*COL
WINDOW_HEIGHT=TILE_SIZE*ROW
class tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y
root=tkinter.Tk()
root.title("SNAKE GAME")
root.resizable(False,False)



canvas=tkinter.Canvas(root,background="black",width=WINDOW_WIDTH,height=WINDOW_HEIGHT,borderwidth=0,highlightthickness=0)
canvas.pack()
root.update()


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = root.winfo_width()
window_height = root.winfo_height()
# Calculate coordinates for the center of the screen
center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

snake=tile(5*TILE_SIZE,5*TILE_SIZE)
food=tile(10*TILE_SIZE,10*TILE_SIZE)
speed_x=0
speed_y=0
snake_body=[]
GAME_OVER=False
SCORE=0
OBSTACKLES=[]
def move():
    global snake,GAME_OVER,food,snake_body,SCORE,OBSTACKLES

    if (snake.x<0 or snake.x>=WINDOW_WIDTH) or (snake.y<0 or snake.y>=WINDOW_HEIGHT):
        GAME_OVER=True

    for tilee in snake_body:
        if snake.x==tilee.x and snake.y == tilee.y:
            GAME_OVER=True

    for obs in OBSTACKLES:
        if snake.x==obs.x and snake.y == obs.y:
            GAME_OVER=True

    if GAME_OVER:
        return
    if snake.x==food.x and snake.y == food.y:
        snake_body.append(tile(food.x,food.y))
        while True:
            food.x=random.randint(0,COL-1)*TILE_SIZE
            food.y=random.randint(0,ROW-1)*TILE_SIZE
            if (food.x,food.y) not in OBSTACKLES:
                break
        SCORE+=1
        if SCORE % 2==1:

            obstacklex = random.randint(0, COL - 1) * TILE_SIZE
            obstackley = random.randint(0, ROW - 1) * TILE_SIZE
            obstackle = tile(obstacklex,obstackley)
            OBSTACKLES.append((obstackle))

    for i in range(len(snake_body)-1,-1,-1):
        if i==0:
            snake_body[i].x=snake.x
            snake_body[i].y=snake.y
        else:
            snake_body[i].x=snake_body[i-1].x
            snake_body[i].y=snake_body[i-1].y

    snake.x+=(speed_x*TILE_SIZE)
    snake.y+=(speed_y*TILE_SIZE)


def changeDirection(e):
    k=e.keysym
    if GAME_OVER:
        return
    global speed_x,speed_y
    if k=="Up" and speed_y!=1:
        speed_y=-1
        speed_x=0
        # print("up")
    elif k=="Down" and speed_y!=-1:
        speed_y =1
        speed_x =0
    elif k=="Right" and speed_x!=-1:
        speed_y =0
        speed_x =1
    elif k=="Left" and speed_x!=1:
        speed_y =0
        speed_x =-1
    # print(speed_x,speed_y,k)

def draw():
    #snake
    global snake,food,GAME_OVER
    if GAME_OVER:
        return
    move()
    canvas.delete('all')
    # point
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="RED")
    #snake
    canvas.create_rectangle(snake.x,snake.y,snake.x+TILE_SIZE,snake.y+TILE_SIZE,fill="lime green")
    for tilee in snake_body:
        canvas.create_rectangle(tilee.x,tilee.y,tilee.x+TILE_SIZE,tilee.y+TILE_SIZE,fill="lime green")

    for obstackle in OBSTACKLES:
        canvas.create_rectangle(obstackle.x, obstackle.y, obstackle.x + TILE_SIZE, obstackle.y + TILE_SIZE, fill="blue")
    root.after(100,draw)

    if GAME_OVER:
        canvas.create_text(WINDOW_WIDTH/2,WINDOW_HEIGHT/2,font='Arial 20',text=f"GAME OVER ! \nSCORE {SCORE}",fill="white")
    else:
        canvas.create_text(30,20,font="Arial 10",text=f"SCORE {SCORE}",fill="white")
draw()

root.bind("<KeyRelease>",changeDirection)
root.mainloop()