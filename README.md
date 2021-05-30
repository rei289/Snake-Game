# Snake-Game
This snake game is like any ordinary snake game, except it can be played as a singleplayer or multiplayer! For singleplayer, it is pretty self-explanitory; you play by yourself. For multiplayer, you can either play against the computer (not an AI but a simple object finding algorithm) or with one of your friends. Note that to switch the multiplayer mode, you have to physically correct the code (more information in the "Notes about code" section). </br> </br>
**Enjoy!** 😊

## Instllation (mac)
### Python
This game uses python. If you have already used or installed python in the past, skip this section. </br>
1. Download package from this website: https://www.python.org/downloads/
2. Once downloaded, open package and follow instructions 
3. Using an IDE will significantly make your life easier in running and modifying the code. Examples of good IDE include PyCharm, Wing (IDE I used to run this code), Spyder

### Libraries
To run this game, you need to install 3 python libraries: pygame, sys, random. These can be installed simply by opening your terminal (for mac) and typing the following:
```
pip install pygame
```
```
pip install sys
```
```
pip install random
```

## Notes about code
1. The code is currently set to play against the computer. If you wish to play with someone else, comment out code from line 646-668 and uncomment code from line 617-644 </br>
**To switch:**
Remove comment from this code (Line 617-644)
```
                    '''
                    # MOVE RIGHT PLAYER LEFT
                    if keys[pygame.K_LEFT]:
                        move_left_right = True
                        move_right_right = False
                        move_up_right = False
                        move_down_right = False        
                    
                    # MOVE RIGHT PLAYER RIGHT
                    if keys[pygame.K_RIGHT]:
                        move_left_right = False
                        move_right_right = True
                        move_up_right = False
                        move_down_right = False
                    
                    # MOVE RIGHT PLAYER UP
                    if keys[pygame.K_UP]:
                        move_left_right = False
                        move_right_right = False
                        move_up_right = True
                        move_down_right = False
                
                    # MOVE RIGHT PLAYER DOWN
                    if keys[pygame.K_DOWN]:
                        move_left_right = False
                        move_right_right = False
                        move_up_right = False
                        move_down_right = True '''
```
And comment out this code (Line 646-668)
```
                    if Snake_right.x_snake > Food_right.x_food:
                        move_left_right = True
                        move_right_right = False
                        move_up_right = False
                        move_down_right = False 
                        
                    if Snake_right.x_snake < Food_right.x_food:
                        move_left_right = False
                        move_right_right = True
                        move_up_right = False
                        move_down_right = False
                    
                    if Snake_right.y_snake > Food_right.y_food:
                        move_left_right = False
                        move_right_right = False
                        move_up_right = True
                        move_down_right = False
                    
                    if Snake_right.y_snake < Food_right.y_food:
                        move_left_right = False
                        move_right_right = False
                        move_up_right = False
                        move_down_right = True    
```
2. To change the speed of the snake, change number in line 344 </br>
**To increase speed, set number higher. To decrease speed, set number lower**
```
        clock.tick(100) 
```
3. You can change the parameters of the snake and food on line 318-326 </br>
* To change colour, change the RGB value in (255,0,0) for Food class and (100,255,100) for Snake class
```
#SINGLEPLAYER
Snake = Snake((100, 255, 100), snake_x_starting_coordinate, snake_y_starting_coordinate, vel, vel)
Food_1 = Food((255, 0, 0), vel, vel)
Food_2 = Food((255, 0, 0), vel, vel)

#MULTIPLAYER
Snake_left = Player_left((100, 255, 100), snake_x_starting_coordinate, snake_y_starting_coordinate, vel, vel)
Snake_right = Player_right((100, 255, 100), 500, snake_y_starting_coordinate, vel, vel)
Food_left = Food_left((255, 0, 0), vel, vel, window_width, window_height)
Food_right = Food_right((255, 0, 0), vel, vel, window_width, window_height)
```
4. You can also change the parameters of the snake and food on line 303-305
* To change starting position of the snake, change the value for snake_x_starting_coordinate and snake_y_starting coordinate
* To change the size of the snake, change the value for vel 
```
vel = 10
snake_x_starting_coordinate = 50
snake_y_starting_coordinate = 50
```

5. This version of snake game is not optimized in anyway, rather it focuses on more of the creativity aspect of the game (allowing singleplayer and multiplayer capabilities)

