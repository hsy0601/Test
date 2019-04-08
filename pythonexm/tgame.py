import pygame
import time
import numpy as np
from pygame.locals import *

BOARDWIDTH=48
BOARDHEIGHT=28
score=0

class Snack(object):
    def __init__(self):
        self.item=[(3,25),(2,25),(1,25),(1,24)]
        self.x = 0
        self.y = -1

    def move(self,enlarge):
        #enlarge用于标记贪吃蛇是否吃到食物
        if not enlarge:
            self.item.pop()
        head=(self.item[0][0]+self.x,self.item[0][1]+self.y)
        self.item.insert(0,head)

    def eat_food(self,food):
        global score
        snack_x,snack_y=self.item[0]
        food_x,food_y=food.item
        if (food_x == snack_x) and (food_y == snack_y):
            score+=100
            return 1
        else:
            return 0

    def toward(self,x,y):
        if self.x*x>=0 and self.y*y>=0:
            self.x=x
            self.y=y

    def get_head(self):
        return self.item[0]

    def draw(self,screen):
        radius=15
        width=15
        color=225,0,0
        position=10+20*self.item[0][0,10+20*self.item[0][1]]
        pygame.draw.circle(screen,color,position,radius,width)
        radius=10
        width=10
        color=255,255,0
        for i ,j in self.item[1:]:
            position=10+20*i,10+20*j
            pygame.draw.circle(screen,color,position,radius,width)
'''
class Food(object):
    def __init__(self):
        self.item=(4,5)

    def _draw(self,screen,i,j):  #画出食物
        color=255,0,255
        radius=10
        width=10
        position=10+20*i,10+20*j
        pygame.draw.circle(screen,color,position,radius,width)

    def update(self,screen,enlarge,snack):  #随机产生食物
        if enlarge:
            self.item=np.random.randint(1,BOARDWIDTH-2),np.random.randint(1,BOARDHEIGHT-2)
            while self.item in snack.item:
                self.item=np.random.randint(1,BOARDWIDTH-2),np.random.randint(1,BOARDHEIGHT-2)
        self._draw(screen,self.item[0],self.item[1])

def init_board(screen):
    board_width=BOARDWIDTH
    board_height=BOARDHEIGHT
    color=10,225,225
    width=0

    for i in range(board_width):
        pos=i*20,0,20,20
        pygame.draw.rect(screen,color,pos,width)
        pos=i*20,(board_height-1)*20,20,20
        pygame.draw.rect(screen,color,pos,width)

    for i in range(board_height-1):
        pos=0,20+i*20,20,20
        pygame.draw.rect(screen,color,pos,width)
        pos=(board_width-1)*20,20+i*20,20,20
        pygame.draw.rect(screen,color,pos,width)

def game_over(snack):
    broad_x,broad_y=snack.get_head()
    flag=0
    old=len(snack.item)
    new=len(set(snack.item))

    if new<old:
        flag=1
    if broad_x==0 or broad_x==BOARDWIDTH-1:
        flag=1
    if broad_y==0 or broad_y==BOARDHEIGHT-1:
        flag=1

    if flag:
        return True
    else:
        return False

def print_text(screen,font,x,y,text,color=(255,0,0)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))

def press(keys,snack):
    global score
    if keys[K_w] or keys[K_UP]:
        snack.toward(0,-1)
    elif keys[K_s] or keys[K_DOWN]:
        snack.toward(0,1)
    elif keys[K_a] or keys[K_LEFT]:
        snack.toward(-1,0)
    elif keys[K_d] or keys[K_RIGHT]:
        snack.toward(1,0)
    elif keys[K_r]:
        score=0
        main()
    elif keys[K_ESCAPE]:
        exit()
'''
def game_init():
    pygame.init()
    screen=pygame.display.set_mode((BOARDWIDTH*20,BOARDHEIGHT*20))
    pygame.display.set_caption('贪吃蛇游戏')
    return screen

def game(screen):
    snack=Snack()
    food=Food()

    font=pygame.font.SysFont('SimHei',20)
    is_fail=0
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
        screen.fill((0,0,100))
        init_board(screen=screen)
        keys=pygame.key.get_pressed()
        press(keys,snack)
        if is_fail:
            font2=pygame.font.Font(None,40)
            print_text(screen,font,0,0,text)
            print_text(screen,font2,400,200,"GAME OVER")
        #游戏主进程
        if not is_fail:
            enlarge=snack.eat_food(food)
            text=u"score:{}贪吃蛇小游戏".format(score)
            print_text(screen,font,0,0,text)
            food.update(screen,enlarge,snack)
            snack.move(enlarge)
            is_fail=game_over(snack=snack)
            snack.draw(screen)
        #游戏刷新
        pygame.display.update()
        time.sleep(0.1)

def main():
    screen=game_init()
    game(screen)

if __name__ == '__main__':
    main()

