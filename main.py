import pgzrun
import random

WIDTH = 400
HEIGHT = 400
TITLE = "Bee Game"

score = 0
gameover = False

bee = Actor("bee")
bee.pos = (100,100)
flower = Actor("flower")
flower.pos = (200,200)

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score : "+str(score),color="black",topleft=(10,10))

    if gameover:
        screen.fill("blue")
        screen.draw.text("Time's Up! Youre Final Score: "+ str(score), color ="black",midtop=(WIDTH/2,10))

def moveflower():
    flower.x = random.randint(20,380)
    flower.y = random.randint(20,380)

def update():
    global score
    
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.down:
        bee.y=bee.y+2
    if keyboard.up:
        bee.y=bee.y-2
    if bee.colliderect(flower):
        score = score + 10
        moveflower()
def timeup():
    global gameover
    gameover = True



clock.schedule(timeup, 60.0)
pgzrun.go()
