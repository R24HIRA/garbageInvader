# Name: Raj Hira
# Date: June 7th, 2021
# Course: ICS3U1-01
# Description: Final Summitive

# import pygame and random
import pygame, random

#CONSTANT
RED = (255, 0, 0)
BLACK = (0,0,0)
BLUE = (0,0,255)
DARK_BLUE = (0,0,153)
LIGHT_BLUE = (0, 255, 251)
OCEAN_BLUE = (51,153, 255)
OCEAN_BLUE_DARK = (0,128,255)
OCEAN_BLUE_DARKER = (0,102,204)
SAND_ORANGE = (255,178,102)
TREE_GREEN = (23,124,20)
GRASS_GREEN = (0,170,0)
DARK_GREEN = (0,102,0)
YELLOW = (255,255,51)
BROWN = (102,51,0)
WHITE = (255,255,255)
GREY = (160,160,160)
LIGHT_GREY = (192,192,192)
TRASH_RADUIS = 15
POWER_RADUIS = 15
SHOOT_RADUIS = 7
WWIDTH = 30
LLENGTH= 30
AMOUNT_OF_STARS = 100
STAR_RADUIS = 1
WIDTH, HEIGHT = 800, 600
SIZE = (WIDTH, HEIGHT)

#list
bullet_y_cord = []
bullet_x_cord = []
enemy_health = [100,100,100,100,100,100]
enemy_x = [100, 200, 300, 400, 500, 600]
enemy_y = [100, 200, 100, 200, 100, 200]
trash_x = []
trash_y = []
power_x = []
power_y = []

#VARIABLES
#character variables
char_x = WIDTH//2
char_y = 500
char_speed = 5

#bullet variables
bullet_x = 0
bullet_y = 500
bul_trac = 0
times_shot = 0
total_shot = 0
bullet_hit = 0
average = 0

#enemy variables
num_of_enemy = 6
ene_trac = 0

#trash variables
trash_con = 0
trash_generator = 0
trash_ran_index = 0

#page variable
page = 0

#mouse variables
mx = 0
my = 0
button = 0

#point variable
points = 0

#lives varibles 
lives = 3

#wave variable
wave = 1

#death variable
death = 0

#power variable
power_con = 0
power_up_genarator = 0

#Game states
running = True
key_left = False
key_right = False
bullet_shot = False
del_enemy = False
direction_change = True 
del_bullet = False
trash_del = False
new_stats = False
power_up_var = False
background_switch = False
myClock = pygame.time.Clock()


#initiate pygame
pygame.init()
screen = pygame.display.set_mode(SIZE)

#Rendering in text
fontHello = pygame.font.SysFont("Times New Roman",30) # done once
fontHello_1 = pygame.font.SysFont("Times New Roman",20) # done once


#define enemy function
def home_screen():
    #fill screen dark blue
    screen.fill(DARK_BLUE)
    #forloop looping for how many stars over and over again
    for star in range (AMOUNT_OF_STARS):
        #drawing a white circle at random locations
        pygame.draw.circle(screen, WHITE, (random.randint(0,800),random.randint(0,600)),STAR_RADUIS)
    #Game name Text
    text = fontHello.render("GARBAGE INVADERS" , 1, WHITE)
    screen.blit(text, pygame.Rect(250,200,400,100))   
    #Pygame drawing for buttons
    pygame.draw.rect(screen,WHITE,pygame.Rect(300,300,200,40))
    pygame.draw.rect(screen,WHITE,pygame.Rect(300,400,200,40))
    pygame.draw.rect(screen,WHITE,pygame.Rect(300,500,240,40))
    #outlines of buttons
    pygame.draw.rect(screen,BLACK,pygame.Rect(300,300,200,40),4)
    pygame.draw.rect(screen,BLACK,pygame.Rect(300,400,200,40),4)
    pygame.draw.rect(screen,BLACK,pygame.Rect(300,500,240,40),4)
    #text on top of buttons to help user play the game
    text = fontHello.render("START" , 1, BLACK)
    screen.blit(text, pygame.Rect(350,300,200,40))    
    text = fontHello.render("INSTRUCTION" , 1, BLACK)
    screen.blit(text, pygame.Rect(300,400,200,40))
    text = fontHello_1.render("BACKGROUND SWITCH" , 1, BLACK)
    screen.blit(text, pygame.Rect(310,510,200,40))    

#define instruction screen function
def instr_screen():
    #fill screen black
    screen.fill(BLACK)
    #text to help read how to play
    text = fontHello.render("How to play?" , 1, WHITE)
    screen.blit(text, pygame.Rect(325,50,200,40))
    text = fontHello_1.render("To controll the character press, left or right on the kep pad" , 1, WHITE)
    screen.blit(text, pygame.Rect(50,150,200,40))
    text = fontHello_1.render("To shoot, press the space bar, make sure that trash does not hit the water or you lose a life" , 1, WHITE)
    screen.blit(text, pygame.Rect(50,200,200,40)) 
    text = fontHello_1.render("If trash hits the water 3 times, you lose, kill the main trash until all of them are dead" , 1, WHITE)
    screen.blit(text, pygame.Rect(50,250,200,40))
    text = fontHello_1.render("There are power ups (red symbol ball) which make you go faster " , 1, WHITE)
    screen.blit(text, pygame.Rect(50,300,200,40))
    text = fontHello_1.render("you earn points as you progress" , 1, WHITE)
    screen.blit(text, pygame.Rect(50,350,200,40))  
    pygame.draw.rect(screen,WHITE,pygame.Rect(300,500,200,100))
    text = fontHello_1.render("Exit" , 1, BLACK)
    screen.blit(text, pygame.Rect(380,550,150,60))     
    
#define restart promt function
def restart_promt():
    #call function
    #checking if background switch is true to change function
    if background_switch == True:
        background_night()
    else:
        background()
    #red box
    pygame.draw.rect(screen, RED, pygame.Rect(0,200,800,200),)
    text = fontHello.render("You died, press anywhere on the red box to go to home" , 1, WHITE)
    screen.blit(text, pygame.Rect(100,300,200,40))      

#define winning_screen function
def winning_screen(p):
    #call function
    #checking if background switch is true to change function
    if background_switch == True:
        background_night()
    else:
        background()
    #white box and text
    pygame.draw.rect(screen, WHITE, pygame.Rect(0,200,800,200),)
    text = fontHello.render("You Won, Press anywhere on the white screen to go to home" , 1, BLACK)
    screen.blit(text, pygame.Rect(50,250,200,40))     
    
#define enemy drawing function    
def enemy(x,y,w,l):
    #a forloop drawing the amount of enemies (trash can)
    for num in range (num_of_enemy):
        pygame.draw.rect(screen, GREY, pygame.Rect(x[num],y[num],w,l))
        pygame.draw.rect(screen, BLACK, pygame.Rect(x[num],y[num],w,l),2)
        pygame.draw.rect(screen, BLACK, pygame.Rect(x[num],y[num],30,10))
        pygame.draw.rect(screen, LIGHT_GREY, pygame.Rect(x[num],y[num]+10,5,20))
        pygame.draw.rect(screen, LIGHT_GREY, pygame.Rect(x[num]+10,y[num]+10,5,20))
        pygame.draw.rect(screen, LIGHT_GREY, pygame.Rect(x[num]+20,y[num]+10,5,20))


#define background function
def background():
    #fill screen light blue
    screen.fill(LIGHT_BLUE)
    #sun function
    sun(100)
    #drawing some grass
    pygame.draw.rect(screen, GRASS_GREEN,pygame.Rect(0,200,800,100))
    #drawing sand
    pygame.draw.rect(screen, SAND_ORANGE,pygame.Rect(0,300,800,200))
    #drawing ocean
    pygame.draw.rect(screen, OCEAN_BLUE,pygame.Rect(0,500,800,100))
    pygame.draw.rect(screen, OCEAN_BLUE_DARK,pygame.Rect(0,550,800,50))
    pygame.draw.rect(screen, OCEAN_BLUE_DARKER,pygame.Rect(0,580,800,20))
    #calling waves function
    waves()
    #calling forest function
    forest()
    #calling tree function
    tree(100,200)
    tree(700,200)
    #bush function
    bush(200,200)
    bush(0,200)
    bush(700,200)
    bush(600,200)
    
def background_night():
    #fill screen light blue
    screen.fill(DARK_BLUE)
    #sun function
    sun(100)
    #drawing some grass
    pygame.draw.rect(screen, GRASS_GREEN,pygame.Rect(0,200,800,100))
    #drawing sand
    pygame.draw.rect(screen, SAND_ORANGE,pygame.Rect(0,300,800,200))
    #drawing ocean
    pygame.draw.rect(screen, OCEAN_BLUE,pygame.Rect(0,500,800,100))
    pygame.draw.rect(screen, OCEAN_BLUE_DARK,pygame.Rect(0,550,800,50))
    pygame.draw.rect(screen, OCEAN_BLUE_DARKER,pygame.Rect(0,580,800,20))
    #calling waves function
    waves()
    #calling forest function
    forest()
    #calling tree function
    tree(100,200)
    tree(700,200)
    #bush function
    bush(200,200)
    bush(0,200)
    bush(700,200)
    bush(600,200)


#define wave function    
def wave_dra(x,y):
    #drawing a wave
    pygame.draw.line(screen, BLACK,(x,y),(x+10,y-10),2)
    pygame.draw.line(screen, BLACK,(x+10,y-10),(x+20,y-15),2)
    pygame.draw.line(screen, BLACK,(x+20,y-15),(x+20,y),2)
    
#define waves function    
def waves():
    #for loop running from 0 to 401 and skipping by 100 to draw waves
    for ocean_space in range (0,401,100):
        wave_dra(ocean_space-100,515)
        wave_dra(ocean_space-80,515)
        wave_dra(ocean_space-60,515)
        wave_dra(ocean_space-40,515)
        wave_dra(ocean_space-20,515)
        wave_dra(ocean_space,515)
    #for loop running from 400 to 801 and skipping by 100 to draw waves
    for ocean_space in range (400,801,100):
        wave_dra(ocean_space-100,540)
        wave_dra(ocean_space-80,540)
        wave_dra(ocean_space-60,540)
        wave_dra(ocean_space-40,540)
        wave_dra(ocean_space-20,540)
        wave_dra(ocean_space,540)    
        
#define tree function
def tree(x,y):
    #the truck
    pygame.draw.rect(screen, BROWN, pygame.Rect(x,y,40,100))
    pygame.draw.rect(screen, BLACK, pygame.Rect(x,y,40,100), 2)
    #leafs
    pygame.draw.circle(screen, TREE_GREEN, (x-10,y-10), 30)
    pygame.draw.circle(screen, TREE_GREEN, (x+50,y-10), 30)
    pygame.draw.circle(screen, TREE_GREEN, (x+40,y-50), 30)
    pygame.draw.circle(screen, TREE_GREEN, (x,y-50), 30)
    pygame.draw.circle(screen, BLACK, (x-10,y-10), 30, 2)
    pygame.draw.circle(screen, BLACK, (x+50,y-10), 30, 2)
    pygame.draw.circle(screen, BLACK, (x,y-50), 30, 2)
    pygame.draw.circle(screen, BLACK, (x+40,y-50), 30, 2)    
    pygame.draw.circle(screen, TREE_GREEN, (x+20,y-30), 40)

#define forest function
def forest():
    tree(100,150)
    tree(200,150)
    tree(300,150)
    tree(0,150)
    tree(600,150)
    tree(700,150)
    tree(800,150)
    tree(650,150)
    tree(500,150)
    tree(750,150)    
    tree(525,170)
    tree(240,170) 
    tree(150,170)
    tree(750,170)     
    
#define bush function
def bush(x,y):
    #many circle to make a bush
    pygame.draw.ellipse(screen, DARK_GREEN, pygame.Rect(x,y,60,35))
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x,y,60,35),2)
    pygame.draw.ellipse(screen, DARK_GREEN, pygame.Rect(x+40,y,60,35))
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+40,y,60,35),2)
    pygame.draw.ellipse(screen, DARK_GREEN, pygame.Rect(x+20,y-10,60,45))
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x+20,y-10,60,45),2)
    
#define bush function
def sun(y):
    #yellow son
    pygame.draw.circle(screen, YELLOW, (WIDTH/2,y) ,50) 

#define character function
def character(x,y):
    #draw character with x and y
    pygame.draw.rect(screen, BLUE, pygame.Rect(x,y,40,40))
    pygame.draw.rect(screen, BLACK, pygame.Rect(x,y,40,40),2)
    #character symbol
    pygame.draw.line(screen, WHITE, (x+10,y+15),(x+20,y+10),2)
    pygame.draw.line(screen, WHITE, (x+20,y+10),(x+30,y+15),2)
    pygame.draw.line(screen, WHITE, (x+30,y+15),(x+35,y+25),2)
    pygame.draw.line(screen, WHITE, (x+35,y+25),(x+20,y+35),2)
    pygame.draw.line(screen, WHITE, (x+20,y+35),(x+5,y+25),2)
    pygame.draw.line(screen, WHITE, (x+5,y+25),(x+10,y+15),2)
    #top of the recycling bin
    pygame.draw.rect(screen, WHITE, (x,y-5,40,5))
    
    
    
#define bullets
def shoot(x,y,shot,r):
    #checking if x is not a empty list
    if len(x) != 0:
        #a forloop running the amount of times shot
        for shoot_ind in range (shot):
            #pygame drawing from x, y and r
            pygame.draw.circle(screen, WHITE,(x[shoot_ind],y[shoot_ind]),r)
            pygame.draw.circle(screen, BLACK,(x[shoot_ind],y[shoot_ind]-10),r)
   
def trash(x,y,con,r):
    #checking if x is not a empty list
    if len(x) != 0:
        #a forloop running the amount of trash 
        for trash_ind in range (con):
            #pygame drawing trash from x and y
            pygame.draw.circle(screen, BLACK, (x[trash_ind],y[trash_ind]),r)
            pygame.draw.circle(screen, BLACK, (x[trash_ind],y[trash_ind]-15),r-5)
            pygame.draw.line(screen, YELLOW,(x[trash_ind]-7,y[trash_ind]-10),(x[trash_ind]+7,y[trash_ind]-10),)
            
def power_up(x,y,con,r):
    #checking if x is not a empty list
    if len(x) != 0:
        #a forloop running the amount of power ups
        for power_ind in range (con):
            #pygame drawing of power up graphic
            pygame.draw.circle(screen, WHITE, (x[power_ind],y[power_ind]),r)
            pygame.draw.circle(screen, BLACK, (x[power_ind],y[power_ind]),r)
            #symbol on power_up
            pygame.draw.line(screen,RED, (x[power_ind]-10,y[power_ind]),(x[power_ind]+10,y[power_ind]),2)
            pygame.draw.line(screen,RED, (x[power_ind]-10,y[power_ind]),(x[power_ind]+5,y[power_ind]-5),2)
            pygame.draw.line(screen,RED, (x[power_ind]-10,y[power_ind]),(x[power_ind]+5,y[power_ind]+5),2)
            pygame.draw.line(screen,RED, (x[power_ind]+10,y[power_ind]),(x[power_ind]-5,y[power_ind]-5),2)
            pygame.draw.line(screen,RED, (x[power_ind]+10,y[power_ind]),(x[power_ind]-5,y[power_ind]+5),2)
                               
            
#The game loop 
while running:
    
    #For loop to grab which button is being used
    for evnt in pygame.event.get():
        
        #if the x is clicked on the screen, turn game loop false
        if evnt.type == pygame.QUIT:
            running = False
        #if mousebutton is clicked define mouse location variables and what button is pressed down 
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            #define variable
            mx, my = evnt.pos
            button = evnt.button        
            
        #checking to see if buttons are down
        if evnt.type == pygame.KEYDOWN:
            #if left button is pressed down turn key_left true
            if evnt.key == pygame.K_LEFT:
                key_left = True
            #if right button is pressed down turn key_right true
            if evnt.key == pygame.K_RIGHT:
                key_right = True
            #if space button is pressed down turn key_space true
            if evnt.key == pygame.K_SPACE:
                #checking to see if page is 4
                if page == 4:
                    #adding 1 to total shot for average
                    total_shot += 1
                    #if button is clicked increase bullet
                    times_shot += 1
                    #turn bullet_shot true
                    bullet_shot = True
                    #checking if bullet y or bullet_x meet the requirements to update the bullet cords
                    if bullet_y == char_y or bullet_x == 0:
                        bullet_x = char_x+20
                    
        #checking to see if the button is up
        if evnt.type == pygame.KEYUP:
            #if left button is let go turn key_left false
            if evnt.key == pygame.K_LEFT:
                key_left = False
            #if right button is let go turn key_right false
            if evnt.key == pygame.K_RIGHT:
                key_right = False 
    if page == 6:
        background_night()
                
    #checking if page is 0            
    if page == 0:
        #if left button is clicked in the specific hitbox flip screens to 4
        if button == 1 and mx >= 300 and mx <= 500 and my >= 300 and my <= 340:
            page = 4
        #if left button is clicked in the specific hitbox flip screens to 1
        if button == 1 and mx >= 300 and mx <= 500 and my >= 400 and my <= 440:
            page = 1 
        #if left button is clicked in the specific hitbox flip screens to 1
        if button == 1 and mx >= 300 and mx <= 520 and my >= 500 and my <= 540:
            background_switch = True         
        #calling home_screen function
        home_screen()
        
    #checking if page is 1    
    if page == 1: 
        #if page is one display function
        instr_screen()
        ##if left button is clicked in the specific hitbox to take to back to home screen
        if button == 1 and mx >= 300 and mx <= 500 and my >= 500 and my <= 600:
            page = 0        
    
    #checking if page is 2    
    if page == 2:
        #if left button is clicked in the specific hitbox to restart game by changing variables to default
        if button == 1 and mx >= 0 and mx <= 800 and my >= 200 and my <= 400:
            page = 0
            points = 0
            lives = 3
            wave = 1
            death += 1
            
        #display restart_promt() function    
        restart_promt()
    
    #checking if page is 3    
    if page == 3:
        
        #if left button is clicked in the specific hitbox to restart game by changing variables to default
        if button == 1 and mx >= 0 and mx <= 800 and my >= 200 and my <= 400:
            page = 0
            lives = 3
            wave = 1
            death += 1        
        
        #display winning_screen funtion
        winning_screen(points)
        
        
    #if page is 4 start the game    
    if page == 4:
        #checking what wave, if wave is one 
        if wave == 1:
            #if death is 1 or more, reassign lists and turn death 0 to not repeat 
            if death >= 1:
                enemy_health = [100,100,100,100,100,100]
                enemy_x = [100, 200, 300, 400, 500, 600]
                enemy_y = [100, 200, 100, 200, 100, 200]
                death = 0
            
            #a forloop running the amount of num_of_enemy
            for ene_ind in range (num_of_enemy):
                #checking if direction_change is true to move enemy right by increasing individual value in list 
                if direction_change == True:
                    #increase enemy_x value by 0.5
                    enemy_x[ene_ind] += 0.5
                    #increase enemy_y value by 0.01
                    enemy_y[ene_ind] += 0.01
                    #checking if a value in enemy_x is 800 or greater, if yes turn direction_change false
                    if enemy_x[ene_ind]+WWIDTH >= 800:
                        direction_change = False
                #checking if direction_change is false to move enemy left by decreasing individual value in list 
                elif direction_change == False:
                    #decrease enemy_x value by 0.5
                    enemy_x[ene_ind] -= 0.5
                    #decrease enemy_y value by 0.01
                    enemy_y[ene_ind] += 0.01
                    #checking if a value in enemy_x is 0 or less to change direction_change to true
                    if enemy_x[ene_ind] <= 0:
                        direction_change = True 
        #checking if wave is 2                
        if wave == 2:
            #checking to see is new stats is true to assign values to enemy_x,enemy_y,health, # of enemies and turning new_states false to not repeat
            if new_stats == True:
                enemy_health = [100,100,100,100,100,100,100]
                enemy_x = [100, 200, 300, 400, 500, 600, 700]
                enemy_y = [100, 200, 100, 200, 100, 200, 100]  
                num_of_enemy = 7
                new_stats = False
           
           #a forloop running the amount of num_of_enemy
            for index in range (num_of_enemy):
                #checking if direction_change is true to move enemy right by increasing individual value in list 
                if direction_change == True:
                    #increase enemy_x value by 0.0
                    enemy_x[index] += 0.9
                    #increase enemy_y value by 0.1
                    enemy_y[index] += 0.1
                    #checking if a value in enemy_x is 800 or greater, if yes turn direction_change false
                    if enemy_x[index]+WWIDTH >= 800:
                        direction_change = False
                #checking if direction_change is false to move enemy left by decreasing individual value in list 
                elif direction_change == False:
                    #decrease enemy_x value by 0.9
                    enemy_x[index] -= 0.9
                    #decrease enemy_y value by 0.1
                    enemy_y[index] += 0.1
                    #checking if a value in enemy_x is 0 or less to change direction_change to true
                    if enemy_x[index] <= 0:
                        direction_change = True            
    
        #Boundries checking if char_x is below 0 or at 0
        if char_x <= 0: 
            #if yes turn key_left false
            key_left = False
        #checking if char_x is above WIDTH or at WIDTH
        elif char_x+WWIDTH >= WIDTH: 
            #if yes turn key_right false
            key_right = False    
            
        #Checking to see if variable is true to move character left or right
        #if key_left is true reduce char_x cords by char_speed (moving speed)
        if key_left == True:
            char_x -= char_speed
        #if key_right is true add to char_x cords by char_speed (moving speed)
        if key_right == True:
            char_x += char_speed
        
        #generatoring a random number from 1 to 70, every time the loop is run    
        trash_generator = random.randint(1,70)  
        
        #checking if number 2 is generated   
        if trash_generator == 2:
            #pick a index value from enemy_x and define trash_ran_index
            trash_ran_index = random.randint(0,len(enemy_x)-1)
            #appending enemy_x and enemy_y value using the trash_ran_index to trash_x and trash_y to create values for trash
            trash_x.append(enemy_x[trash_ran_index])
            trash_y.append(enemy_y[trash_ran_index])
            #add one to trash_con to keep track of how many times trash spawned in
            trash_con += 1
            
        
        #generatoring a random number from 1 to 1000, every time the loop is run    
        power_up_genarator = random.randint(1,1000)
        
        #checking if number 1 is generated     
        if power_up_genarator == 1:
            #pick a index value from enemy_x and defining power_ran_index
            power_ran_index = random.randint(0,len(enemy_x)-1)
            #appending enemy_x and enemy_y value using the power_ran_index to power_x and power_y to create values for power up
            power_x.append(enemy_x[power_ran_index])
            power_y.append(enemy_y[power_ran_index])
            #add one to power_con to keep track of how many times power_up spawned in
            power_con += 1
                     
        #checking if bullet is true 
        if bullet_shot == True:
            #add bullet to list by appending bullet_x and bullet_y
            bullet_x_cord.append(bullet_x)                
            bullet_y_cord.append(bullet_y)        
            #checking if bullet_y values are 0 and then defining bul_trac
            if bullet_y_cord[bul_trac] == 0:
                bul_trac = bullet_y_cord.index(bullet_y)
            #turning bullet_shot to false to avoid appening muliple times
            bullet_shot = False
            
        #update bullet_y_cord by checking if bullet_y_cord list is empty
        if len(bullet_y_cord) != 0: 
            #running a forlop for the length of bulley_y_cord
            for bullet_index_search in range (len(bullet_y_cord)):
                #reducing every value in the list by -10 to show the affecting of shooting up
                bullet_y_cord[bullet_index_search] -= 10
        
        #updating trash_x value by checking if trash_x list is empty           
        if len(trash_x) != 0:
            #running a forlop for the length of trash_y
            for co in range (len(trash_y)):
                #adding every value in the list by 1 to show the affecting of falling up
                trash_y[co] += 1
                
        #updating power_x value by checking if power_x list is empyy              
        if len(power_x) != 0:
            #running a forlop for the length of trash_y
            for do in range (len(power_y)):
                #adding every value in the list by 1 to show the affecting of falling up
                power_y[do] += 1        
                        
        #nested for loop running the length of the list
        for bu_counter in range (len(bullet_x_cord)):
            
            #loop running for the num of enemy
            for en_counter in range (num_of_enemy):
                #if statement checking if enemy and bullet collided
                if bullet_y_cord[bu_counter]+SHOOT_RADUIS < enemy_y[en_counter]+LLENGTH and bullet_y_cord[bu_counter]+SHOOT_RADUIS > enemy_y[en_counter] and bullet_x_cord[bu_counter] > enemy_x[en_counter] and bullet_x_cord[bu_counter] < enemy_x[en_counter] + WWIDTH:
                    #reducing enemy health
                    enemy_health[en_counter] -= 50                
                    #define variable to help determine what to delete
                    ene_trac = en_counter
                    #turn del_enemy true
                    del_enemy = True
                    #adding points
                    points += 20
                    #adding 1 to bullet hit for average
                    bullet_hit += 1                    
                    
            #loop running for the trash_con
            for trash_counter in range (trash_con):
                #if statement checking if trash and bullet collided
                if bullet_y_cord[bu_counter]+SHOOT_RADUIS < trash_y[trash_counter]+TRASH_RADUIS and bullet_y_cord[bu_counter]+SHOOT_RADUIS > trash_y[trash_counter]-TRASH_RADUIS and bullet_x_cord[bu_counter] > trash_x[trash_counter]-TRASH_RADUIS and bullet_x_cord[bu_counter] < trash_x[trash_counter]+TRASH_RADUIS:     
                    #define variable to help determine what to delete
                    tra_del_in = trash_counter
                    #turn trash_del true
                    trash_del = True
                    #adding points
                    points += 5
                    #adding 1 to bullet hit for average
                    bullet_hit += 1                    
         
            #loop running for the power_con
            for power_counter in range (power_con):
                #if statement checking if power_up and bullet collided
                if bullet_y_cord[bu_counter]+SHOOT_RADUIS < power_y[power_counter]+POWER_RADUIS and bullet_y_cord[bu_counter]+SHOOT_RADUIS > power_y[power_counter]-POWER_RADUIS and bullet_x_cord[bu_counter] > power_x[power_counter]-POWER_RADUIS and bullet_x_cord[bu_counter] < power_x[power_counter]+POWER_RADUIS:         
                    #define variable to help determine what to delete
                    pow_del_in = power_counter
                    #turning power_up_var true
                    power_up_var = True
                    #adding 2 to char_speed
                    char_speed += 2
                    #adding 1 to bullet hit for average
                    bullet_hit += 1
           
        #checking if trash_x list is empty             
        if len(trash_x) != 0:  
            #running a forloop for the length of trash_x
            for index_checker in range (len(trash_x)):
                #using index_checker. checking if trash_y is greater than 500
                if trash_y[index_checker] > 500:
                    #define tra_del_in by index_checker to help determine what to delete 
                    tra_del_in = index_checker
                    #turn trash_del true
                    trash_del = True
                    #reduce life by -1
                    lives -= 1
                    
        #checking if enemy_health is 50 and if bullet_y_cord is empty and del_enemyis true to delete bullet when bullets collided    
        if enemy_health[ene_trac] == 50 and len(bullet_y_cord) != 0 and del_enemy == True:
            #turn del_bullet true to delete bullet when hit
            del_bullet = True 
            #turn del_enemy true because enemy is not being deleted yet
            del_enemy = False
            
        #check to see if bullet_y list is empty, have to add this if statement first because sometimes bul_trac is not defined or ene_trac
        if len(bullet_y_cord) != 0:
            #checking if  bullet_y_cord vales are below 0 or 0 or enemy values are 0 or trash_del is true and power_up_car is true. Another statement to delete bullet because bul_trac is not defined sometimes when bullet_y list is empty 
            if bullet_y_cord[bul_trac] <= 0 or enemy_health[ene_trac] == 0 or trash_del == True or power_up_var == True:
                del_bullet = True
        
        #checking if trash_del is true   
        if trash_del == True:
            #if it is reduce trash_counter by 1
            trash_con -= 1
            #delete the trash values which were collided with or beyond 500
            del trash_y[tra_del_in]
            del trash_x[tra_del_in]
            #turn trash_del false to not repeat
            trash_del = False
        
        #checking if power_up_val is true    
        if power_up_var == True:
            #if it is reduce power_up_var by 1
            power_con -= 1
            #delete the power_up values which were collided with
            del power_y[pow_del_in]
            del power_x[pow_del_in]
            #turn power_up_val false to not repeat
            power_up_var = False
        
        #checking if del_bullet is true                            
        if del_bullet == True:
            #if it is times_shot reduced by one
            times_shot -= 1
            #delete bullet values which were collided with or less than or at 0
            del bullet_y_cord[bul_trac]
            del bullet_x_cord[bul_trac]
            #updating bullet_y var
            bullet_y = char_y
            #turning del_bullet false to not repeat
            del_bullet = False
            
        #checking if variable is true and enemy health is 0 to delete enemy character
        if del_enemy == True and enemy_health[ene_trac] == 0:
            #reducing number of enemy by 1
            num_of_enemy -= 1
            #deleting the values from enemy from specific index defined when collided
            del enemy_health[ene_trac]
            del enemy_x[ene_trac]
            del enemy_y[ene_trac]
            #turn ene_trac 0 to not make the program crash because it is an idex value
            ene_trac = 0
            #turn del_enemy false
            del_enemy = False
            
        #checking if lives are 0 and then ressign variables to play the game again
        if lives == 0:
            trash_x = []
            trash_y = []            
            trash_con = 0
            points = 0
            page = 2
            
        #checking if the length of enemy is 0 
        if len(enemy_x) == 0:
            #checking if wave is 1 and then turn to value to and turn new stats on to assign new values for enemy
            if wave == 1:
                new_stats = True
                wave = 2
            #checking if wave is 2
            elif wave == 2:
                #if yes turn to a new page with winning promt
                page = 3
                
        ##checking if bullet shot is above 1 to find average    
        #if total_shot >=1:
            #average = total_shot/bullet_hit
        
        text = fontHello_1.render("LIVES %i" % lives , 1, BLACK)
        screen.blit(text, pygame.Rect(0,50,150,60))
        text = fontHello_1.render("POINTS %i" % points , 1, BLACK)
        screen.blit(text, pygame.Rect(0,100,150,60))
        text = fontHello_1.render("ACCURACY %f" % average , 1, BLACK)
        screen.blit(text, pygame.Rect(0,150,150,60))         
        
            
        #calling all the functions  
        #checking if background switch is true to change function
        if background_switch == True:
            background_night()
        else:
            background()        
        enemy(enemy_x,enemy_y,WWIDTH,LLENGTH)
        trash(trash_x,trash_y,trash_con,TRASH_RADUIS)
        power_up(power_x,power_y,power_con,POWER_RADUIS)
        shoot(bullet_x_cord,bullet_y_cord,times_shot,SHOOT_RADUIS)
        character(char_x,char_y)
    
    #flip to see all the pygame screens
    pygame.display.flip()
    #clock frame rate is 60
    myClock.tick(60)
pygame.quit()
