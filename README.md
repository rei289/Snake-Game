# Snake-Game
This snake game is like any ordinary snake game, except it can be played as a singleplayer or multiplayer! For singleplayer, it is pretty self-explanitory; you play by yourself. For multiplayer, you can either play against the computer (not an AI but a simple object finding algorithm) or with one of your friends. Note that to switch the multiplayer mode, you have to physically correct the code (more information in the "Notes about code" section). </br>
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
1. The code is currently set to play against the computer. If you wish to play with someone else, comment out code from line 646-668 and uncomment code from line 617-644
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
2. To change the speed of the snake, change number in line 344
**To increase speed, set number higher. To decrease speed, set number lower**
```
        clock.tick(100) 
```
3. This version of snake game is not optimized in anyway, rather it focuses on more of the creativity aspect of the game (allowing singleplayer and multiplayer capabilities)


## How the code works
If you are interested in knowing how the code works, there are comments written in the code briefly describing most of the line in the code. However, for a more in-depth description of the code, here is a description of the code:

```

```
