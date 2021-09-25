import pygame
import random
import os
pygame.init()
pygame.mixer.init()
game_window=pygame.display.set_mode((1100,500))#Creating the Game Window

pygame.display.set_caption("Snake Game")#Giving a Title to the Game
c=pygame.time.Clock()
font=pygame.font.SysFont('tahoma',50,bold=True,italic=True) #Choosing a font from the System
font1=pygame.font.SysFont('calibri',80,bold=True,italic=True) #Choosing a font from the System
font2=pygame.font.SysFont('georgia',50,bold=True,italic=True) #Choosing a font from the System
font3=pygame.font.SysFont('consolas',60,bold=True,italic=True) #Choosing a font from the System
#Colours
yellow=(255,255,0)
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
orange=(255,128,0)
black=(0,0,0)
chocklate=(255,127,36)
white=(255,255,255)
def print_text(string,color,x,y):
    text=font.render(string,True,color)#Creating the Text which we have to print in the Game Window
    game_window.blit(text,[x,y])#Printong the text in the Game Window
def print_text1(string,color,x,y):
    text1=font1.render(string,True,color)#Creating the Text which we have to print in the Game Window
    game_window.blit(text1,[x,y])#Printong the text in the Game Window
def print_text2(string,color,x,y):
    text2=font2.render(string,True,color)#Creating the Text which we have to print in the Game Window
    game_window.blit(text2,[x,y])#Printong the text in the Game Window
def print_text3(string,color,x,y):
    text3=font3.render(string,True,color)#Creating the Text which we have to print in the Game Window
    game_window.blit(text3,[x,y])#Printong the text in the Game Window

def plot_snake(gameWindow, color, snk_list,l,b):# Function to plot the snake at an(x,y) position from the list 
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x,y,l,b])
def welcome():
    #game_window.fill(white)
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play()
    img1=pygame.image.load("snake1.jpg")
    img1=pygame.transform.scale(img1,(1100,500)).convert_alpha()
    game_window.blit(img1,(0,0))
    print_text1("!!!Welcome to the Snake Game!!!",black,10,50)
    print_text3("Press Enter To Continue",red,200,150)
    pygame.display.update()
    game_quit=True
    while game_quit:
        for e in pygame.event.get():
            if(e.type==pygame.QUIT):
                game_quit=False
            if(e.type==pygame.KEYDOWN):
                if(e.key==pygame.K_RETURN):
                    game_loop()
    pygame.quit()
    quit      
#Game loop
def game_loop():
    #Game Variables
    s=0
    game_quit=True
    game_over=0
    snake_x=10
    snake_y=10
    v_x=0
    v_y=0
    speed=5
    fps=40
    snake_length=15
    snake_breadth=15
    food_x=random.randint(300,700)
    food_y=random.randint(300,400)
    snake_list=[]
    check=1
    with open("Hiscore.text","r") as g:
        ct=g.read()
    while game_quit :
        if (game_over==1):
            #pygame.mixer.music.load("exit.mp3")
            #pygame.mixer.music.play()
            img3=pygame.image.load("snake4.jpg")
            img3=pygame.transform.scale(img3,(1100,500)).convert_alpha()
            game_window.blit(img3,(0,0))
            #game_window.fill(green)
            print_text1("Game Over",red,350,30)
            print_text3("Score:"+str(s)+"!Here Highscore is:-"+ct,blue,4,140)
            print_text("Press Enter To Play Again",black,250,350)
            for e in pygame.event.get():
                if(e.type==pygame.QUIT): #For Quiting the game by clicking the cross buttom in the top rightmost corner
                    game_quit=False
                if(e.type==pygame.KEYDOWN):
                    if(e.key==pygame.K_RETURN):
                        game_loop()
        else:
            for e in pygame.event.get():
                if(e.type==pygame.QUIT): #For Quiting the game by clicking the cross buttom in the top rightmost corner
                    game_quit=False
                if(e.type==pygame.KEYDOWN): #If any key is pressed by the user 
                    if(e.key==pygame.K_RIGHT):
                        v_x=+speed
                        v_y=0
                    if(e.key==pygame.K_LEFT):
                        v_x=-speed
                        v_y=0
                    if(e.key==pygame.K_UP):
                        v_x=0
                        v_y=-speed
                    if(e.key==pygame.K_DOWN):
                        v_y=speed
                        v_x=0
            snake_x+=v_x #For increasing the velocity in x direction according to the chosen case
            snake_y+=v_y #For increasing the velocity in y direction according to the chosen case
            #game_window.fill(yellow) 
            img2=pygame.image.load("snake2.jpg")
            img2=pygame.transform.scale(img2,(1100,500)).convert_alpha()
            game_window.blit(img2,(0,0))
            #pygame.display.update()
            pygame.draw.circle(game_window,yellow,[food_x,food_y],10) #Drawing food for the Snake
            pygame.draw.rect(game_window,red,[snake_x,snake_y,20,10]) #Drawing the snake
            if (abs(snake_x-food_x)<18 and abs(snake_y-food_y)<18): #Cheking if the snake has eaten the food 
                pygame.mixer.music.load("food.mp3")
                pygame.mixer.music.play()
                s+=10
                food_x=random.randint(100,700)#Reploting the food
                food_y=random.randint(100,400)
                speed+=0.5
                check+=5
                if (s>int(ct)):
                    ct=str(s)
                    with open("Hiscore.text","w")as f:
                        f.write(str(ct))
            if (snake_x>1100 or snake_x<0 or snake_y>499 or snake_y<0):
                pygame.mixer.music.load("over1.wav")
                pygame.mixer.music.play()
                game_over=1
            if(len(snake_list)>check):
                del snake_list[0]
            head=[]
            head.append(snake_x)
            head.append(snake_y)       
            snake_list.append(head) 
            if head in snake_list[:-2]:
                pygame.mixer.music.load("over1.wav")
                pygame.mixer.music.play()
                game_over=1
            plot_snake(game_window,red,snake_list,20,20)
            print_text2("Your Score is : "+str(s),red,300,10)
        pygame.display.update()
        c.tick(fps)
    pygame.quit()
    quit
welcome()