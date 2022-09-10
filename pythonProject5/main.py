import pygame as py
import random

score=0
times=0
py.init()
value=(1000,800)
window=py.display.set_mode(value)

speed=20
FPS=60
clock=py.time.Clock()

skeleton=py.image.load("shocked.png")
skeleton_coordinate=skeleton.get_rect()
skeleton_coordinate.center=(500,400)

dog=py.image.load("dog.png")
dog_coordinate=dog.get_rect()
dog_coordinate.topleft=(10,10)
case3=True
case=True
case1=True
a=0
while case3:
    for event in py.event.get():
        if event.type==py.QUIT:
            case3=False
            case=False
            case1=False
        if event.type==py.KEYDOWN:
            if event.key==py.K_SPACE:
                case3 = False
    calibri = py.font.SysFont("calibri", 32)
    welcome=calibri.render("FEED THE DOG GAME PRESS 'SPACE' TO START!",True,(255,255,255))
    welcome_coordinate=welcome.get_rect()
    welcome_coordinate.center=(500,400)
    window.blit(welcome,welcome_coordinate)
    py.display.update()

while case:
    for event in py.event.get():
        if event.type==py.QUIT:
            case=False
            case1=False
        if score==20:
            case=False
    key=py.key.get_pressed()
    if key[py.K_LEFT] and dog_coordinate.left>0:
        dog_coordinate.x-=speed
    elif key[py.K_RIGHT] and dog_coordinate.right<1000:
        dog_coordinate.x+=speed
    elif key[py.K_UP] and dog_coordinate.top>0:
        dog_coordinate.y-=speed
    elif key[py.K_DOWN] and dog_coordinate.bottom<800:
        dog_coordinate.y+=speed
    if dog_coordinate.colliderect(skeleton_coordinate):
        skeleton_coordinate.x=random.randint(0,1000)
        skeleton_coordinate.y=random.randint(0,800)
        score+=1
    scoreboard = calibri.render("SCORE:" + str(score), True, (255, 255, 255))
    scoreboard_coordinate = scoreboard.get_rect()
    scoreboard_coordinate.center = (500, 100)
    window.fill((0,0,0))
    window.blit(dog,dog_coordinate)
    window.blit(scoreboard,scoreboard_coordinate)
    window.blit(skeleton,skeleton_coordinate)
    py.display.update()
    clock.tick(FPS)
while case1:
    for event in py.event.get():
        if event.type==py.QUIT:
            case1=False
    py.draw.rect(window,(0,0,0),(0,0,1000,800),0)
    gameover=calibri.render("You Won!CONGRATS!!!",True,(255,255,255))
    gameover_coordinate=gameover.get_rect()
    gameover_coordinate.center=(500,400)
    window.blit(gameover,gameover_coordinate)
    py.display.update()



py.quit()