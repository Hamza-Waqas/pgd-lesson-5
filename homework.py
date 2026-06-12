import pgzrun
import random

WIDTH = 400
HEIGHT = 400
TITLE = "Farmer Game"

score = 0
gameover = False

farmer = Actor("farmer")
farmer.pos = (100,100)
vegetable = Actor("vegetable")
vegetable.pos = (200,200)

def draw():
    screen.blit("background",(0,0))
    farmer.draw()
    vegetable.draw()
    screen.draw.text("Score : "+str(score),color="black",topleft=(10,10))

    if gameover:
        screen.fill("blue")
        screen.draw.text("Time's Up! Youre Final Score: "+ str(score), color ="black",midtop=(WIDTH/2,10))

def movevegetable():
    vegetable.x = random.randint(20,380)
    vegetable.y = random.randint(20,380)

def update():
    global score
    
    if keyboard.right:
        farmer.x=farmer.x+2
    if keyboard.left:
        farmer.x=farmer.x-2
    if keyboard.down:
        farmer.y=farmer.y+2
    if keyboard.up:
        farmer.y=farmer.y-2
    if farmer.colliderect(vegetable):
        score = score + 10
        movevegetable()
def timeup():
    global gameover
    gameover = True



clock.schedule(timeup, 60.0)
pgzrun.go()
