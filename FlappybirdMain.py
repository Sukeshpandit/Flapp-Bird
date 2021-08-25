import pygame
from pygame import mixer
import sys
import time
from pygame.constants import QUIT

pygame.init()#initializing pygame
#screen and backround

screen_size = [970,500]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load("flappy baground.jpg")
bird = pygame.image.load("bird.png")
bird_x = 0 
bird_y = 210

clock = pygame.time.Clock()
alive = True
move_direction = 'right'

#playing backgroundmusic 

mixer.music.load('backgroundmusic.wav')#while using music for entire end use mixer.music (try using wav format than mp3)
mixer.music.play(-1,0.0) #-1 makes music to play in loop after it is finished and 0.0 is the starting point of music

#playing crash music
crash_sound = mixer.Sound('crash.wav')#while playing sounds other than background use mixer.sound

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',25)


#main loop
while alive:
    screen.blit(background,[0,0])
    screen.blit(bird,[bird_x,bird_y])
   

    #exit or quit action 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

      #space key to fly
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] == True:
      bird_y -= 2
    else:
       bird_y += 2
    

    #forward movement of bird
    if move_direction == 'right':
        bird_x += 2
        if bird_x == 970:
            score_value += 1
            bird_x = 50 # once birds hits right cornor birds x postion changes to original
            bird_y = 270# once birds hits right cornor birds y postion changes to original
        elif bird_y == 500 :#if bird touches upward 
            bird_y = 10    #it will come from below
        elif bird_y ==10:  #if bird touches below 
            bird_y = 500  #it comes from above

  
    #1st piler uo
    if bird_y < 200 and bird_x > 20 and bird_x < 125:
       mixer.music.stop() #stops the main background music
       crash_sound.play()# plzys crash sound
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
       print("\n \n YOU FAILED YOUR MISSION ")
       
       
      #1st piler  down
    elif bird_y > 300 and bird_x >20 and bird_x < 125:
       mixer.music.stop() #stops the main background music
       crash_sound.play()
       print("\n \n YOU FAILED YOUR MISSION ")
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
    

      #2nd piller(up) collision
    elif bird_y < 280 and bird_x >265 and bird_x < 370:
       mixer.music.stop() #stops the main background music
       crash_sound.play()
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
       print("\n \n YOU FAILED YOUR MISSION ") 
          
    #2nd piller down collision
    elif bird_y > 390 and bird_x >265 and bird_x < 370:
       mixer.music.stop() #stops the main background music
       crash_sound.play()
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
       print("\n \n YOU FAILED YOUR MISSION ") 

    #3nd piller up collision
    elif bird_y < 280 and bird_x >525 and bird_x < 630:
       mixer.music.stop() #stops the main background music
       crash_sound.play()
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
       print("\n \n YOU FAILED YOUR MISSION ") 

    #3nd piller down collision
    elif bird_y > 370 and bird_x >525 and bird_x < 630:
       mixer.music.stop() #stops the main background music
       crash_sound.play()
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
       print("\n \n YOU FAILED YOUR MISSION ") 
    
     #4nd piller up collision
    elif bird_y < 120 and bird_x > 780 and bird_x < 885:
       mixer.music.stop() #stops the main background music
       crash_sound.play()
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
       print("\n \n YOU FAILED YOUR MISSION  ") 

    #4nd piller down collision
    elif bird_y > 225 and bird_x > 780 and bird_x < 885:
       mixer.music.stop() #stops the main background music
       crash_sound.play()
       time.sleep(0.8) #stops screen for sec befor exiting
       alive = False
       print("\n \n YOU FAILED YOUR MISSION ") 
    
      
    score = font.render("SCORE:" + str(score_value),True,(0,0,0))
    screen.blit(score,[130,10])
 
    pygame.display.update()
    clock.tick(60)#FPS