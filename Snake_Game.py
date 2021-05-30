import pygame
import sys
import random

#SINGLEPLYAER
class Snake():
    def __init__(self, colour_snake, x_snake, y_snake, width_snake, height_snake):
        self.colour_snake = colour_snake
        self.x_snake = x_snake
        self.y_snake = y_snake
        self.width_snake = width_snake
        self.height_snake = height_snake
        
    def draw(self):
        pygame.draw.rect(window, self.colour_snake, [self.x_snake, self.y_snake, self.width_snake, self.height_snake]) 
        pygame.display.update()  
        
    def move(self):
        if move_left == True:
            self.x_snake -= vel
        if move_right == True:
            self.x_snake += vel 
        if move_up == True:
            self.y_snake -= vel  
        if move_down == True:
            self.y_snake += vel 
            
class Food():
    def __init__(self, colour_food, width_food, height_food):
        self.colour_food = colour_food
        self.width_food = width_food
        self.height_food = height_food
        self.x_food = random.randrange(0, window_width - width_food, 10)
        self.y_food = random.randrange(0, window_height - height_food, 10)
        
    def draw(self):
        pygame.draw.rect(window, self.colour_food, [self.x_food, self.y_food, self.width_food, self.height_food])
        pygame.display.update()


#MULTIPLAYER
class Player_right():
    def __init__(self, colour_snake, x_snake, y_snake, width_snake, height_snake):
        self.colour_snake = colour_snake
        self.x_snake = x_snake
        self.y_snake = y_snake
        self.width_snake = width_snake
        self.height_snake = height_snake
        
    def draw(self):
        pygame.draw.rect(window, self.colour_snake, [self.x_snake, self.y_snake, self.width_snake, self.height_snake]) 
        pygame.display.update()  
        
    def move(self):
        if move_left_right == True:
            self.x_snake -= vel
        if move_right_right == True:
            self.x_snake += vel 
        if move_up_right == True:
            self.y_snake -= vel  
        if move_down_right == True:
            self.y_snake += vel 
            
class Player_left():
    def __init__(self, colour_snake, x_snake, y_snake, width_snake, height_snake):
        self.colour_snake = colour_snake
        self.x_snake = x_snake
        self.y_snake = y_snake
        self.width_snake = width_snake
        self.height_snake = height_snake
        
    def draw(self):
        pygame.draw.rect(window, self.colour_snake, [self.x_snake, self.y_snake, self.width_snake, self.height_snake]) 
        pygame.display.update()  
        
    def move(self):
        if move_left_left == True:
            self.x_snake -= vel
        if move_right_left == True:
            self.x_snake += vel 
        if move_up_left == True:
            self.y_snake -= vel  
        if move_down_left == True:
            self.y_snake += vel 

class Food_right():
    def __init__(self, colour_food, width_food, height_food, window_width, window_height):
        self.colour_food = colour_food
        self.width_food = width_food
        self.height_food = height_food
        self.x_food = random.randrange(window_width/2 + width_food, window_width - width_food, 10)
        self.y_food = random.randrange(0, window_height - height_food, 10)
        
    def draw(self):
        pygame.draw.rect(window, self.colour_food, [self.x_food, self.y_food, self.width_food, self.height_food])
        pygame.display.update()
        
class Food_left():
    def __init__(self, colour_food, width_food, height_food, window_width, window_height):
        self.colour_food = colour_food
        self.width_food = width_food
        self.height_food = height_food
        self.x_food = random.randrange(0, window_width/2 - width_food, 10)
        self.y_food = random.randrange(0, window_height - height_food, 10)
        
    def draw(self):
        pygame.draw.rect(window, self.colour_food, [self.x_food, self.y_food, self.width_food, self.height_food])
        pygame.display.update()


# BEFORE THE GAME    
def main_menu():
    # Initialize font
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = font.render('Welcome to the Snake Game!', False, (255, 255, 255))
    # Make the text centered
    textrect = textsurface.get_rect(center = (window_width/2, window_height/4))
    window.blit(textsurface, textrect) 
    pygame.display.update() 
    
def singleplayer_before_hover(width, height):
    pygame.draw.rect(window, (255, 0, 0), [1*window_width/4 - width/2, 3*window_height/4 - height/2, width, height])
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = font.render('Singleplayer', False, (255, 255, 255))
    # Make the text centered 
    textrect = textsurface.get_rect(center = (1*window_width/4, 3*window_height/4))
    window.blit(textsurface, textrect)
    pygame.display.update()                 

def multiplayer_before_hover(width, height):
    pygame.draw.rect(window, (0, 200, 0), [3*window_width/4 - width/2, 3*window_height/4 - height/2, width, height])
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = font.render('Multiplayer', False, (255, 255, 255))
    # Make the text centered 
    textrect = textsurface.get_rect(center = (3*window_width/4, 3*window_height/4))
    window.blit(textsurface, textrect)    
    pygame.display.update()
    
def singleplayer_after_hover(width, height):
    pygame.draw.rect(window, (255, 100, 100), [1*window_width/4 - width/2, 3*window_height/4 - height/2, width, height])
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = font.render('Singleplayer', False, (255, 255, 255))
    # Make the text centered 
    textrect = textsurface.get_rect(center = (1*window_width/4, 3*window_height/4))
    window.blit(textsurface, textrect)
    pygame.display.update()                     
    
def multiplayer_after_hover(width, height):
    pygame.draw.rect(window, (100, 255, 100), [3*window_width/4 - width/2, 3*window_height/4 - height/2, width, height])
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = font.render('Multiplayer', False, (255, 255, 255))
    # Make the text centered 
    textrect = textsurface.get_rect(center = (3*window_width/4, 3*window_height/4))
    window.blit(textsurface, textrect)    
    pygame.display.update()
    
def countdown(number):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = font.render(str(number), False, (255, 255, 255))
    textrect = textsurface.get_rect(center = (1*window_width/2, 1*window_height/2)) 
    window.blit(textsurface, textrect)
    pygame.display.update()
    
# DURING THE GAME
#SINGLEPLAYER
def score(length_snake):
    # Make the length of snake a string
    snake_length_string = str(length_snake)
    # Initialize font
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('Score: ' + snake_length_string, False, (255, 255, 255))  
    window.blit(textsurface,(600,0))
    pygame.display.update()

#MULTIPLAYER    
def score_right(length_snake):
    # Make the length of snake a string
    snake_length_string = str(length_snake)
    # Initialize font
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('Score: ' + snake_length_string, False, (255, 255, 255))  
    window.blit(textsurface,(600,0))
    pygame.display.update()
    

def score_left(length_snake):
    # Make the length of snake a string
    snake_length_string = str(length_snake)
    # Initialize font
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render('Score: ' + snake_length_string, False, (255, 255, 255))  
    window.blit(textsurface,(50,0))
    pygame.display.update()
    
    
    
# AFTER THE GAME
#SINGLEPLAYER
def final_score(score): 
    # Final Score in the game
    final_score = str(score)
    
    # Intialize the score
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = font.render('Final Score: ' + final_score, False, (0, 0, 0))
    # Make the text centered
    textrect = textsurface.get_rect(center = (window_width/2, window_height/2))
    window.blit(textsurface, textrect)    
    

#MULTIPLAYER
def final_score_left(score): 
    # Final Score in the game
    final_score = str(score)
    
    # Intialize the score
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = font.render('Final Score for left player: ' + final_score, False, (0, 0, 0))
    # Make the text centered
    textrect = textsurface.get_rect(center = (1*window_width/4, window_height/2))
    window.blit(textsurface, textrect)  
    
def final_score_right(score): 
    # Final Score in the game
    final_score = str(score)
    
    # Intialize the score
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = font.render('Final Score for right player: ' + final_score, False, (0, 0, 0))
    # Make the text centered
    textrect = textsurface.get_rect(center = (3*window_width/4, window_height/2))
    window.blit(textsurface, textrect)
    
    
def instructions_1():
    # Intialize the font
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 40)
    textsurface = font.render('Press c to play again', False, (0, 0, 0))
    # Make the text centered
    textrect = textsurface.get_rect(center = (window_width/2, 3*window_height/4))
    window.blit(textsurface, textrect) 
  
  
       
    
# Initialize pygame
pygame.init()

# Title of the game
pygame.display.set_caption("Snake Game")

# Window to draw on
window_width = 760
window_height = 760
window = pygame.display.set_mode((window_width, window_height)) # Window is 500 by 500

# BUTTON ATTRIBUTES
button_width = 140
button_height = 70

# TIMER
time_list = []

# MOVING THE SNAKE 
#SINGLEPLAYER
move_left = False
move_right = True
move_up = False
move_down = False
collision = False
#MULTIPLAYER
move_left_left = False
move_right_left = False
move_up_left = False
move_down_left = True 

move_left_right = False
move_right_right = False
move_up_right = False
move_down_right = True  


collision_left = False
collision_right = False

left_game = True
right_game = True

# SNAKE ATTRIBUTES
vel = 10
snake_x_starting_coordinate = 50
snake_y_starting_coordinate = 50
#SINGLEPLAYER
snake_list = []
#MULTIPLAYER
snake_list_left = []
snake_list_right = []
snake_length_left = 0
snake_length_right = 0

snake_length = 0

# INSTANCES
#SINGLEPLAYER
Snake = Snake((100, 255, 100), snake_x_starting_coordinate, snake_y_starting_coordinate, vel, vel)
Food_1 = Food((255, 0, 0), vel, vel)
Food_2 = Food((255, 0, 0), vel, vel)

#MULTIPLAYER
Snake_left = Player_left((100, 255, 100), snake_x_starting_coordinate, snake_y_starting_coordinate, vel, vel)
Snake_right = Player_right((100, 255, 100), 500, snake_y_starting_coordinate, vel, vel)
Food_left = Food_left((255, 0, 0), vel, vel, window_width, window_height)
Food_right = Food_right((255, 0, 0), vel, vel, window_width, window_height)



start_timer = False
game_over = False
game_start = False
end_game = False
singleplayer = False
multiplayer = False

# As long as this main while loop is running, you can continue the game
while end_game == False:
    
    while not game_over:   
        
    
        clock = pygame.time.Clock()
        clock.tick(100) 
        # When the game is over
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
                pygame.quit()
                sys.exit() 
                
                
        # CONTROLS OF THE SNAKE
        keys = pygame.key.get_pressed() 
        
        
        # MAIN MENU
        if game_start == False and start_timer == False:
            main_menu()
            mouse = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            # HOVERING OVER THE BUTTONS
            if (window_width/4 - button_width/2) < mouse[0] < (window_width/4 + button_width/2) and (3*window_height/4 - button_height/2) < mouse[1] < (3*window_height/4 + button_height/2):
                singleplayer_after_hover(button_width, button_height)
                multiplayer_before_hover(button_width, button_height)
                
                # START TIMER
                if mouse_pressed[0] == True:
                    start_timer = True
                    singleplayer = True
                    window.fill((0,0,0))
                    pygame.display.update()
                
            elif (3*window_width/4 - button_width/2) < mouse[0] < (3*window_width/4 + button_width/2) and (3*window_height/4 - button_height/2) < mouse[1] < (3*window_height/4 + button_height/2):      
                singleplayer_before_hover(button_width, button_height)
                multiplayer_after_hover(button_width, button_height)
                
                # START TIMER
                if mouse_pressed[0] == True:
                    start_timer = True
                    multiplayer = True
                    window.fill((0,0,0))
                    pygame.display.update()
            
            else:
                singleplayer_before_hover(button_width, button_height)
                multiplayer_before_hover(button_width, button_height)                
            
        # TIMER
        if start_timer == True:
            window.fill((0,0,0))
            
            current_time = pygame.time.get_ticks()
            time_list.append(current_time)
            if current_time >= time_list[0] and current_time < time_list[0] + 1000:
                countdown(3)
                
            elif current_time >= time_list[0] + 1000 and current_time < time_list[0] + 2000:
                countdown(2)
                
            elif current_time >= time_list[0] + 2000 and current_time < time_list[0] + 3000:
                countdown(1)
                
            elif current_time >= time_list[0] + 3000 and current_time < time_list[0] + 4000:
                countdown('GO!')
                
            else:
                game_start = True
                start_timer = False                                
        
        
        # ACTUAL GAME
        if game_start == True:
            # SINGLEPLAYER 
            if singleplayer == True: 
                
                # MOVE LEFT
                if keys[pygame.K_LEFT]:
                    move_left = True
                    move_right = False
                    move_up = False
                    move_down = False        
                
                # MOVE RIGHT
                if keys[pygame.K_RIGHT]:
                    move_left = False
                    move_right = True
                    move_up = False
                    move_down = False        
                
                # MOVE UP
                if keys[pygame.K_UP]:
                    move_left = False
                    move_right = False
                    move_up = True
                    move_down = False 
            
                # MOVE DOWN
                if keys[pygame.K_DOWN]:
                    move_left = False
                    move_right = False
                    move_up = False
                    move_down = True 
                
                # DRAW SNAKE AND 2 FOOD
                Snake.draw() 
                Food_1.draw()  
                Food_2.draw()          
                
                # APPEND THE COORDINATES THAT THE SNAKE MOVED IN
                snake_list.append((Snake.x_snake, Snake.y_snake)) 
                
                if len(snake_list) > 3: 
                    if collision == False:
                        # Get rid of square before 
                        pygame.draw.rect(window, (0, 0, 0), [snake_list[0][0], snake_list[0][1], Snake.width_snake, Snake.height_snake])
                        #pygame.display.update() 
                        snake_list.pop(0)  
                        
                # MOVE THE SNAKE   
                Snake.move()
                # USE FOR DETECTING A COLLISION
                snake = pygame.Rect(Snake.x_snake, Snake.y_snake, Snake.width_snake, Snake.height_snake)
                food_1 = pygame.Rect(Food_1.x_food, Food_1.y_food, Food_1.width_food, Food_1.height_food)
                food_2 = pygame.Rect(Food_2.x_food, Food_2.y_food, Food_2.width_food, Food_2.height_food)
                
                collision = False
                if snake.colliderect(food_1) == True:
                    # Get rid of the food
                    pygame.draw.rect(window, (0, 0, 0), [Food_1.x_food, Food_1.y_food, Food_1.width_food, Food_1.height_food])
                    pygame.display.update()
                    
                    # Food moves to another location
                    Food_1.x_food = random.randrange(0, window_width - Food_1.width_food, 10)
                    Food_1.y_food = random.randrange(0, window_height - Food_1.height_food, 10)
                    
                    # Dont rid of the first coordinate in the list
                    collision = True
                    
                    # Increase the score by one
                    snake_length += 1
                    
                    # Cover up the original score with black box
                    pygame.draw.rect(window, (0, 0, 0), [665, 0, 30, 25])
                    pygame.display.update()
                    
                if snake.colliderect(food_2) == True:
                    # Get rid of the food
                    pygame.draw.rect(window, (0, 0, 0), [Food_2.x_food, Food_2.y_food, Food_2.width_food, Food_2.height_food])
                    pygame.display.update()
                    
                    # Food moves to another location
                    Food_2.x_food = random.randrange(0, window_width - Food_2.width_food, 10)
                    Food_2.y_food = random.randrange(0, window_height - Food_2.height_food, 10)
                    
                    # Dont rid of the first coordinate in the list
                    collision = True
                    
                    # Increase the score by one
                    snake_length += 1
                    
                    # Cover up the original score with black box
                    pygame.draw.rect(window, (0, 0, 0), [665, 0, 30, 25])
                    pygame.display.update()    
                    
                # CHECK IF THE SNAKE HIT ITSELF
                if len(snake_list) != len(set(snake_list)):
                    game_over = True
                
                # CHECK IF THE SNAKE MOVED OFF SCREEN
                if Snake.x_snake < 0 or Snake.x_snake > window_width:
                    game_over = True
                    
                if Snake.y_snake < 0 or Snake.y_snake > window_height:
                    game_over = True
                
                # PRINT THE SCORE    
                score(snake_length)
                
            # MULTIPLAYER
            if multiplayer == True:
                pygame.draw.rect(window, (255, 255, 255), [window_width/2 - 10, 0, 20, window_height])
                pygame.display.update()
                
                # LEFT GAME
                if left_game == True:
                    # MOVE LEFT PLAYER LEFT
                    if keys[pygame.K_a]:
                        move_left_left = True
                        move_right_left = False
                        move_up_left = False
                        move_down_left = False        
                    
                    # MOVE LEFT PLAYER RIGHT
                    if keys[pygame.K_d]:
                        move_left_left = False
                        move_right_left = True
                        move_up_left = False
                        move_down_left = False 
                    
                    # MOVE LEFT PLAYER UP
                    if keys[pygame.K_w]:
                        move_left_left = False
                        move_right_left = False
                        move_up_left = True
                        move_down_left = False 
                
                    # MOVE LEFT PLAYER DOWN
                    if keys[pygame.K_s]:
                        move_left_left = False
                        move_right_left = False
                        move_up_left = False
                        move_down_left = True
                        
                    # DRAW LEFT SNAKE AND LEFT FOOD
                    Snake_left.draw() 
                    Food_left.draw() 
                    
                    # APPEND THE COORDINATES OF THE LEFT SNAKE
                    snake_list_left.append((Snake_left.x_snake, Snake_left.y_snake)) 
                    
                    # MAKE IT LOOK LIKE LEFT SNAKE IS MOVING
                    if len(snake_list_left) > 3: 
                        if collision_left == False:
                            # Get rid of square before 
                            pygame.draw.rect(window, (0, 0, 0), [snake_list_left[0][0], snake_list_left[0][1], Snake_left.width_snake, Snake_left.height_snake])
                            #pygame.display.update() 
                            snake_list_left.pop(0) 
                    
                    # MOVE THE LEFT SNAKE        
                    Snake_left.move()
                    
                    # USE FOR DETECTION OF COLLISION
                    snake_left = pygame.Rect(Snake_left.x_snake, Snake_left.y_snake, Snake_left.width_snake, Snake_left.height_snake)
                    food_left = pygame.Rect(Food_left.x_food, Food_left.y_food, Food_left.width_food, Food_left.height_food)
                    
                    collision_left = False
                    # IF LEFT SNAKE COLLIDES WITH LEFT FOOD
                    if snake_left.colliderect(food_left) == True:
                        # Get rid of the food
                        pygame.draw.rect(window, (0, 0, 0), [Food_left.x_food, Food_left.y_food, Food_left.width_food, Food_left.height_food])
                        pygame.display.update()
                        
                        # Food moves to another location
                        Food_left.x_food = random.randrange(0, window_width/2 - 10 - Food_left.width_food, 10)
                        Food_left.y_food = random.randrange(0, window_height - Food_left.height_food, 10)
                        
                        # Dont rid of the first coordinate in the list
                        collision_left = True
                        
                        # Increase the score by one
                        snake_length_left += 1
                        
                        # Cover up the original score with black box
                        pygame.draw.rect(window, (0, 0, 0), [115, 0, 30, 25])
                        pygame.display.update()      
                        
    
                    # CHECK IF THE LEFT SNAKE HIT ITSELF
                    if len(snake_list_left) != len(set(snake_list_left)):
                        left_game = False   
                        
                    # CHECK IF THE LEFT SNAKE MOVED OFF SCREEN
                    if Snake_left.x_snake < 0 or Snake_left.x_snake > window_width/2 - 20:
                        left_game = False 
                        
                    if Snake_left.y_snake < 0 or Snake_left.y_snake > window_height:
                        left_game = False 
                        
                    # SCORE    
                    score_left(snake_length_left)   
                
                # RIGHT GAME    
                if right_game == True:
                    
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
                    
                    # DRAW RIGHT SNAKE AND RIGHT FOOD
                    Snake_right.draw() 
                    Food_right.draw()         
                
                    # APPEND THE COORDINATES THAT THE RIGHT SNAKE MOVED IN
                    snake_list_right.append((Snake_right.x_snake, Snake_right.y_snake)) 
                
                    # MAKE IT LOOK LIKE RIGHT SNAKE IS MOVING     
                    if len(snake_list_right) > 3: 
                        if collision_right == False:
                            # Get rid of square before 
                            pygame.draw.rect(window, (0, 0, 0), [snake_list_right[0][0], snake_list_right[0][1], Snake_right.width_snake, Snake_right.height_snake])
                            #pygame.display.update() 
                            snake_list_right.pop(0)            
                    # MOVE THE RIGHT SNAKE                  
                    Snake_right.move()
                    
                    # USE FOR DETECTING A COLLISION
                    snake_right = pygame.Rect(Snake_right.x_snake, Snake_right.y_snake, Snake_right.width_snake, Snake_right.height_snake)
                    food_right = pygame.Rect(Food_right.x_food, Food_right.y_food, Food_right.width_food, Food_right.height_food)
                    
                    collision_right = False                
                    # IF THE RIGHT SNAKE COLLIDES WITH RIGHT FOOD    
                    if snake_right.colliderect(food_right) == True:
                        # Get rid of the food
                        pygame.draw.rect(window, (0, 0, 0), [Food_right.x_food, Food_right.y_food, Food_right.width_food, Food_right.height_food])
                        pygame.display.update()
                        
                        # Food moves to another location
                        Food_right.x_food = random.randrange(window_width/2 + Food_right.width_food, window_width - Food_right.width_food, 10)
                        Food_right.y_food = random.randrange(0, window_height - Food_right.height_food, 10)
                        
                        # Dont rid of the first coordinate in the list
                        collision_right = True
                        
                        # Increase the score by one
                        snake_length_right += 1
                        
                        # Cover up the original score with black box
                        pygame.draw.rect(window, (0, 0, 0), [665, 0, 30, 25])
                        pygame.display.update()    
                    
                    # CHECK IF THE RIGHT SNAKE HIT ITSELF         
                    if len(snake_list_right) != len(set(snake_list_right)):
                        right_game = False            
                
                    # CHECK IF THE RIGHT SNAKE MOVED OFF SCREEN
                    if Snake_right.x_snake < window_width/2 + 10 or Snake_right.x_snake > window_width:
                        right_game = False 
                        
                    if Snake_right.y_snake < 0 or Snake_right.y_snake > window_height:
                        right_game = False             
                    
                    # SCORE
                    score_right(snake_length_right)
                
                if left_game == False and right_game == True:
                    pygame.draw.rect(window, (255, 255, 255), [0, 0, window_width/2, window_height])
                    pygame.display.update()
                    
                if left_game == True and right_game == False:
                    pygame.draw.rect(window, (255, 255, 255), [window_width/2, 0, window_width/2, window_height])
                    pygame.display.update()            
                    
                if left_game == False and right_game == False:
                    game_over = True                
        
        
    # AFTER THE GAME IS OVER    
    while game_over:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                end_game = True
                pygame.quit()
                sys.exit() 
        if singleplayer == True:        
            # FINAL SCORE OF THE GAME  
            window.fill((255, 255, 255))
            final_score(snake_length)
            instructions_1()
            pygame.display.update() 
            
        if multiplayer == True:
            # FINAL SCORE OF THE GAME   
            window.fill((255, 255, 255))
            final_score_left(snake_length_left)
            final_score_right(snake_length_right)
            instructions_1()
            pygame.display.update()             
        
        # TO RESET THE GAME
        keys = pygame.key.get_pressed()   
        if keys[pygame.K_c]:
            if singleplayer == True:
                # Reset all the positions and points
                snake_list.clear()
                snake_length = 0
                time_list.clear()
                window.fill((0, 0, 0))
                pygame.display.update()
                
                # VERY IMPORTANT
                Snake.x_snake = snake_x_starting_coordinate
                Snake.y_snake = snake_y_starting_coordinate
                Food_1.x_food = random.randrange(0, window_width - Food_1.width_food, 10)
                Food_1.y_food = random.randrange(0, window_height - Food_1.height_food, 10)
                Food_2.x_food = random.randrange(0, window_width - Food_2.width_food, 10)
                Food_2.y_food = random.randrange(0, window_height - Food_2.height_food, 10)            
                
                move_left = False
                move_right = True
                move_up = False
                move_down = False
                
                start_timer = False
                game_start = False
                game_over = False
                singleplayer = False
            if multiplayer == True:
                # Reset all the positions and points
                snake_list_left.clear()
                snake_list_right.clear()    
                snake_length_left = 0
                snake_length_right = 0
                time_list.clear()
                window.fill((0, 0, 0))
                pygame.display.update()
                
                # VERY IMPORTANT
                Snake_left.x_snake = snake_x_starting_coordinate
                Snake_left.y_snake = snake_y_starting_coordinate
                Snake_right.x_snake = snake_x_starting_coordinate + 500
                Snake_right.y_snake = snake_y_starting_coordinate            
                
                Food_left.x_food = random.randrange(0, window_width/2 + Food_left.width_food, 10)
                Food_left.y_food = random.randrange(0, window_height - Food_left.height_food, 10)
                Food_right.x_food = random.randrange(window_width/2, window_width - Food_right.width_food, 10)
                Food_right.y_food = random.randrange(0, window_height - Food_right.height_food, 10)            
                
                move_left_left = False
                move_right_left = False
                move_up_left = False
                move_down_left = True
                
                move_left_right = False
                move_right_right = False
                move_up_right = False
                move_down_right = True            
                
                left_game = True
                right_game = True
                start_timer = False
                game_start = False
                game_over = False        
                multiplayer = False
    
pygame.quit()
