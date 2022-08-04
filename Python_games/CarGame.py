import pygame, random
from car import Car


pygame.init()
#for the song
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Retro_music.mp3')
pygame.mixer.music.play(-1) #-1 means loops for ever, 0 means play just once)


# different RGB colors
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
 
speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)
 
 
SCREENWIDTH=500
SCREENHEIGHT=600
 
size = (SCREENWIDTH, SCREENHEIGHT)
#used to dislay
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Racing")

def paused():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
#X key = quit
            elif event.key == pygame.K_x:
                pygame.quit()
                quit()
        clock.tick(5)
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
 #Object and class
playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = SCREENHEIGHT - 100
 
car1 = Car(PURPLE, 60, 80, random.randint(50,100))
car1.rect.x = 60
car1.rect.y = -100
 
car2 = Car(YELLOW, 60, 80, random.randint(50,100))
car2.rect.x = 160
car2.rect.y = -600
 
car3 = Car(CYAN, 60, 80, random.randint(50,100))
car3.rect.x = 260
car3.rect.y = -300
 
car4 = Car(BLUE, 60, 80, random.randint(50,100))
car4.rect.x = 360
car4.rect.y = -900
 
 #different X and Y coordinates
 
# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)
 
all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)


 
#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn: #carryon = false means that the while loop would stop
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                while True: #Infinite loop that will be broken when the user press the space bar again
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break #Exit infinite loop
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Makes the game stop after pressing X
                    carryOn=False
        keys = pygame.key.get_pressed()

         #car collision code (works because it's inside the carry on code)
        car_collision_list = pygame.sprite.spritecollide(playerCar,all_coming_cars,False,pygame.sprite.collide_mask)
        for car in car_collision_list:
            print("Car crash!")
            carryOn=False
 


        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            speed +=0.05
            playerCar.moveBackward(5)
        if keys[pygame.K_DOWN]:
            speed -= 0.05
            playerCar.moveForward(5)

        #Game Logic
        for car in all_coming_cars:
            car.moveForward(speed)
            if car.rect.y > SCREENHEIGHT:
                car.changeSpeed(random.randint(50,100))
                car.repaint(random.choice(colorList))
                car.rect.y = -200
 
        all_sprites_list.update()
 
        #Drawing on Screen
        screen.fill(GREEN)
        #Draw The Road
        pygame.draw.rect(screen, BLACK, [40,0, 400,SCREENHEIGHT])
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [140,0],[140,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [240,0],[240,SCREENHEIGHT],5)
        #Draw Line painting on the road
        pygame.draw.line(screen, WHITE, [340,0],[340,SCREENHEIGHT],5)
        pygame.draw.line(screen, WHITE, [40,0],[40,SCREENHEIGHT],5)
        pygame.draw.line(screen, WHITE, [440,0],[440,SCREENHEIGHT],5)
 
 
        #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
        all_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 


pygame.quit()