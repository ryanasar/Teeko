
'''install pygame package(terminal: pip install pygame)'''

import pygame
from pygame.locals import *

pygame.init()

def check_exit():
    '''if user ever clicks X in top corner, it will close the game'''
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                running = False
                return True

def display_rules(text):
    '''displays rules and continues to game when user clicks 'OK"'''

    # draws outline of rules
    screen.fill('white')
    pygame.draw.rect(screen, "black", (100,30,800,780), 4, 15)

    # draws title
    title_font = pygame.font.SysFont('freesansbold.ttf', 130)
    title_text = title_font.render('Teeko', True, 'black')
    title_pos = (370, 50)
    screen.blit(title_text, title_pos)


    # creates start button
    play_game_rect = pygame.Rect(304,664,392,112)
    button_color = 'grey'
    pygame.draw.rect(screen, button_color, play_game_rect, 0, 8)
    pygame.draw.rect(screen, "black", (300,660,400,120), 4, 15)

    # creates text for start button
    start_game_font = pygame.font.SysFont('freesansbold.ttf', 90)
    start_game_text = start_game_font.render(text, True, 'black')
    start_game_pos = (335, 690)
    screen.blit(start_game_text, start_game_pos)


    # sets text fotn for the instructions
    instructions_font = pygame.font.SysFont('freesansbold.ttf', 40)

    # writes instructions
    instructions_text = instructions_font.render("1. Players take turns placing their colored pieces on", True, 'black')
    instructions_pos = (140, 200)
    screen.blit(instructions_text, instructions_pos)

    instructions_text = instructions_font.render("   the board, with black going first", True, 'black')
    instructions_pos = (140, 240)
    screen.blit(instructions_text, instructions_pos)


    instructions_text = instructions_font.render("2. Once each player has placed four pieces, they take", True, 'black')
    instructions_pos = (140, 300)
    screen.blit(instructions_text, instructions_pos)

    instructions_text = instructions_font.render("   turns moving their pieces by one square", True, 'black')
    instructions_pos = (140, 340)
    screen.blit(instructions_text, instructions_pos)
    

    instructions_text = instructions_font.render("3. If a player has four of their pieces in a row vertically,", True, 'black')
    instructions_pos = (140, 400)
    screen.blit(instructions_text, instructions_pos)

    instructions_text = instructions_font.render("   horizontally, or diagonally, they win", True, 'black')
    instructions_pos = (140, 440)
    screen.blit(instructions_text, instructions_pos)

    pygame.display.flip()

    show_instructions = True
    while show_instructions:

        # if mouse is hovering the button, it will change color
        if play_game_rect.collidepoint(pygame.mouse.get_pos()):

            # if the button is pressed, it will exit the instruction page
            if pygame.mouse.get_pressed()[0]:
                show_instructions = False
                break

            if button_color != 'grey87':
                button_color = 'grey87'
                pygame.draw.rect(screen, button_color, play_game_rect, 0, 8)
                screen.blit(start_game_text, start_game_pos)
                pygame.display.flip()
        else:
            if button_color != 'grey':
                button_color = 'grey'
                pygame.draw.rect(screen, button_color, play_game_rect, 0, 8)
                screen.blit(start_game_text, start_game_pos)
                pygame.display.flip()

        
        if check_exit():
            return
                
def draw_empty_board(black_score, red_score):
    '''creates a clear board for a new game'''

    screen.fill('white')

    # draws board outline
    board = pygame.Rect(200,150,600,600)
    pygame.draw.rect(screen, "black", board, 6)
    #pygame.draw.rect(screen, "black", pygame.Rect(135,95,730,730), 8)

    
    # draws vertical lines in board
    xy_multiplier = 150
    for i in range(1,4):
        pygame.draw.line(screen, "black", (200 + xy_multiplier*i, 160), (200 + xy_multiplier*i, 760), 6)

    # draws horizontal lines in board
    for i in range(1,4):
        pygame.draw.line(screen, "black", (200, 160 + xy_multiplier*i), (800, 160 + xy_multiplier*i), 6)
    
    # draws diagonal lines
    pygame.draw.line(screen, "black", (200,160), (800,760), 6)
    pygame.draw.line(screen, "black", (200,760), (800,160), 6)

    for i in range(1,4):
        pygame.draw.line(screen, "black", (200 + xy_multiplier*i, 160), (200, 160 + xy_multiplier*i), 6)

    for i in range(1,4):
        pygame.draw.line(screen, "black", (800, 160 + xy_multiplier*i), (200 + xy_multiplier*i, 760), 6)

    for i in range(1,4):
        pygame.draw.line(screen, "black", (200 + xy_multiplier*i, 160), (800, 760 - xy_multiplier*i), 6)

    for i in range(1,4):
        pygame.draw.line(screen, "black", (200, 160 + xy_multiplier*i), (800 - xy_multiplier*i, 760), 6)

    
    # draws squares and adds the to a dictionary, with x,y positon as the key
    global coordinate_dict

    for x in range(0,5):
        for y in range(0,5):
            square = pygame.Rect(150 + x*xy_multiplier, 110 + y*xy_multiplier, 100, 100)
            pygame.draw.rect(screen, "black", square, 4)

    for x in range(0,5):
        for y in range(0,5):
            square = pygame.Rect(154 + x*xy_multiplier, 114 + y*xy_multiplier, 92, 92)
            pygame.draw.rect(screen, "white", square)
            coordinate_dict[(x,y)] = square

    # draws box for text at the top
    pygame.draw.rect(screen, 'black', pygame.Rect(300,10,400,80), 4)

    pygame.draw.rect(screen, 'white', pygame.Rect(304,14,392,72), 0)
    font = pygame.font.SysFont('freesansbold.ttf', 80) 
    text = font.render('Black Turn', True, 'black')
    text_pos = (360, 25)
    screen.blit(text, text_pos)

    # draws box and text for scoreboard
    pygame.draw.rect(screen, 'black', pygame.Rect(50,10,200,80), 4)
    pygame.draw.rect(screen, 'white', pygame.Rect(54,14,192,72), 0)
    font = pygame.font.SysFont('freesansbold.ttf', 90) 

    text = font.render(f'{black_score}', True, 'black')
    text_pos = (90, 22)
    screen.blit(text, text_pos)

    text = font.render('-', True, 'black')
    text_pos = (136, 20)
    screen.blit(text, text_pos)

    text = font.render(f'{red_score}', True, 'red')
    text_pos = (170, 22)
    screen.blit(text, text_pos)


    # writes instruction in top right corner
    pygame.draw.rect(screen, 'black', pygame.Rect(750,10,240,80), 4)
    pygame.draw.rect(screen, 'white', pygame.Rect(754,14,232,72), 0)
    font = pygame.font.SysFont('freesansbold.ttf', 40) 

    text = font.render(f'Place a Square', True, 'black')
    text_pos = (770, 38)
    screen.blit(text, text_pos)

    # displays the screen
    pygame.display.flip()

    # returns the empty dictionary
    return coordinate_dict
     
def newgame(black_score, red_score):
    '''used when user starts game or chooses to play again'''

    # creates an empty dictionary and matrix for the board
    coordinate_dict = draw_empty_board(black_score, red_score)
    # coordinate dict uses a tuple containing (x,y) coordinate as key, and a pygame Rect object as its value
    board_matrix = [['x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x'],
                    ['x', 'x', 'x', 'x', 'x']]
    
    return board_matrix, coordinate_dict

def black_place(board):
    turn_in_progress = True
    color = 'white'

    while turn_in_progress:
        if check_exit():
            return
            
        # checks to see if an empty square is being hovered by the mouse
        for cord, square in coordinate_dict.items():
            if square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':

                # if the mouse is pressed while hovering the empty square
                if pygame.mouse.get_pressed()[0]:

                    # this will color the new square black and set its value in the matrix to 'b' (for black)
                    color = 'black'
                    pygame.draw.rect(screen, color, square, 0)
                    board[cord[1]][cord[0]] = 'b'
                    
                    # this draws the box at the top to say 'Red Turn'
                    pygame.draw.rect(screen, 'white', pygame.Rect(304,14,392,72), 0)
                    font = pygame.font.SysFont('freesansbold.ttf', 80) 
                    text = font.render('Red Turn', True, 'red')
                    text_pos = (385, 25)
                    screen.blit(text, text_pos)

                    pygame.display.flip()
                    return board
                
                if color != 'grey78':
                    color = 'grey78'
                    pygame.draw.rect(screen, color, square, 0)
                    pygame.display.flip()
                
            # if the mouse is no longer hovering over an empty square, it will reset its color to white
            if not square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':
                color = 'white'
                pygame.draw.rect(screen, color, square, 0)
                pygame.display.flip()                 

def red_place(board):
    turn_in_progress = True
    color = 'white'

    while turn_in_progress:
        if check_exit():
            return
            
        # checks to see if an empty square is being hovered by the mouse
        for cord, square in coordinate_dict.items():
            if square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':

                # if the mouse is pressed while hovering the empty square
                if pygame.mouse.get_pressed()[0]:

                    # this will color the new square red and set its value in the matrix to 'r' (for red)
                    color = 'red'
                    pygame.draw.rect(screen, color, square, 0)
                    board[cord[1]][cord[0]] = 'r'
                    
                    # this draws the box at the top to say 'Black Turn'
                    pygame.draw.rect(screen, 'white', pygame.Rect(304,14,392,72), 0)
                    font = pygame.font.SysFont('freesansbold.ttf', 80) 
                    text = font.render('Black Turn', True, 'black')
                    text_pos = (360, 25)
                    screen.blit(text, text_pos)

                    pygame.display.flip()
                    return board
                
                if color != 'lightpink':
                    color = 'lightpink'
                    pygame.draw.rect(screen, color, square, 0)
                    pygame.display.flip()
                
    
            # if the mouse is no longer hovering over an empty square, it will reset its color to white
            if not square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':
                color = 'white'
                pygame.draw.rect(screen, color, square, 0)
                pygame.display.flip() 

def select_square(square):
    '''takes in a square as a parameter, and outlines it in white to signify it is selected'''
    
    # takes positional and dimenstion values from givenn square
    x, y = square.left, square.top
    width, height = square.width, square.height

    # draws the white outline using the dimensions of the square
    outline = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, 'white', outline, 4)
    pygame.display.flip()

def unselect_square(square, color):
    '''never actually got to use this method because i was lazy and didnt feel like adding this feature'''
    x, y = square.left, square.top
    width, height = square.width, square.height
    outline = pygame.Rect(x, y, width, height)

    pygame.draw.rect(screen, color, outline, 4)
    pygame.display.flip()

def get_valid_moves(coordinate, board):
    '''returns all possible moves based on the input coordinate of a square and the current board'''
    valid = []
    x, y = coordinate[0], coordinate[1]

    # if the differece between the row and index from the input coordinate is less than or equal to one, it is added to the valid_moves list
    for row_index, row,  in enumerate(board):
        if abs(row_index - y) <= 1:
            for col_index, col in enumerate(row):
                if abs(col_index - x) <= 1 and board[row_index][col_index] == 'x':
                    valid.append((col_index,row_index))
    
    return valid
    
def black_move(board):
    '''allows the black pieces to be moved by the player'''

    global coordinate_dict
    square_selected = False

    # loop runs until the user selects a square
    while not square_selected:
        if check_exit():
            return
            
        valid_moves = []

        # allows user to click a black square and gets all possible moves from that square
        for cord, square in coordinate_dict.items():
            if square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'b':
                if pygame.mouse.get_pressed()[0]:
                    select_square(square)
                    clicked_square = square
                    original_coordinates = cord

                    # gets the valid moves from this square by calling valid_moves()
                    valid_moves = get_valid_moves(cord, board)
                    square_selected = True
                    pygame.time.delay(200)

    new_square_selected = False

    # this loop runs until the user selects a new square
    while not new_square_selected:

        if check_exit():
            return
        
        # this loop runs only through squares that are valid and checks if the user hovers or clicks one
        for move_coordinate in valid_moves:
            move_square = coordinate_dict[move_coordinate]
            if move_square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':
                color = 'black'
                if pygame.mouse.get_pressed()[0]:
                    
                    board[original_coordinates[1]][original_coordinates[0]] = 'x'
                    pygame.draw.rect(screen, 'white', clicked_square, 0)

                    color = 'black'
                    pygame.draw.rect(screen, color, move_square, 0)
                    board[move_coordinate[1]][move_coordinate[0]] = 'b'
                    
                    pygame.draw.rect(screen, 'white', pygame.Rect(304,14,392,72), 0)
                    font = pygame.font.SysFont('freesansbold.ttf', 80) 
                    text = font.render('Red Turn', True, 'red')
                    text_pos = (385, 25)
                    screen.blit(text, text_pos)

                    pygame.display.flip()
                    return board
                
                if color != 'grey78':
                    color = 'grey78'
                    pygame.draw.rect(screen, color, move_square, 0)
                    pygame.display.flip()
                

            #if clicked_square.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                #unselect_square(clicked_square, 'black')
                #pygame.time.delay(200)
                #black_move(board)

            if not move_square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':
                color = 'white'
                pygame.draw.rect(screen, color, move_square, 0)
                pygame.display.flip()         

def red_move(board):
    global coordinate_dict
    square_selected = False

    # this loop runs until the user selects a square
    while not square_selected:
        if check_exit():
            return
            
        valid_moves = []

        # allows user to click a black square and gets all possible moves from that square
        for cord, square in coordinate_dict.items():
            if square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'r':
                if pygame.mouse.get_pressed()[0]:
                    select_square(square)
                    clicked_square = square
                    original_coordinates = cord

                    # gets the valid moves from this square by calling valid_moves()
                    valid_moves = get_valid_moves(cord, board)
                    square_selected = True
                    pygame.time.delay(200)

    new_square_selected = False

    # this loop runs until the user selects a square to move to 
    while not new_square_selected:

        if check_exit():
            return

        # this loop runs only through squares that are valid and checks if the user hovers or clicks one
        for move_coordinate in valid_moves:
            move_square = coordinate_dict[move_coordinate]
            if move_square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':
                color = 'red'
                if pygame.mouse.get_pressed()[0]:
                    
                    board[original_coordinates[1]][original_coordinates[0]] = 'x'
                    pygame.draw.rect(screen, 'white', clicked_square, 0)

                    color = 'red'
                    pygame.draw.rect(screen, color, move_square, 0)
                    board[move_coordinate[1]][move_coordinate[0]] = 'r'
                    
                    pygame.draw.rect(screen, 'white', pygame.Rect(304,14,392,72), 0)
                    font = pygame.font.SysFont('freesansbold.ttf', 80) 
                    text = font.render('Black Turn', True, 'black')
                    text_pos = (385, 25)
                    screen.blit(text, text_pos)

                    pygame.display.flip()
                    return board
                
                if color != 'lightpink':
                    color = 'lightpink'
                    pygame.draw.rect(screen, color, move_square, 0)
                    pygame.display.flip()
                
            
            #if clicked_square.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                #unselect_square(clicked_square, 'red')
                #pygame.time.delay(200)
                #red_move(board)
            

            if not move_square.collidepoint(pygame.mouse.get_pos()) and board[cord[1]][cord[0]] == 'x':
                color = 'white'
                pygame.draw.rect(screen, color, move_square, 0)
                pygame.display.flip()        

def check_consecutive(lst):
    '''called only in the check_min method, checks if there are four of the same consecutive values'''
    for i in range(len(lst) - 3):
        if lst[i] != 'x' and lst[i] == lst[i + 1] == lst[i + 2] == lst[i + 3]:
            print(lst[i])
            return lst[i]
    return None

def check_win(board):
    '''takes the board matrix as the parameter and returns true if there are four of the same color in a row'''
    # Check rows and columns
    for i in range(5):
        winning_value = check_consecutive(board[i])
        if winning_value is not None:
            return True, winning_value

        winning_value = check_consecutive([board[j][i] for j in range(5)])
        if winning_value is not None:
            return True, winning_value

    # Check diagonals
    for i in range(2):
        for j in range(2):
            winning_value = check_consecutive([board[i + k][j + k] for k in range(4)])
            if winning_value is not None:
                return True, winning_value

    for i in range(2):
        for j in range(4, 1, -1):
            winning_value = check_consecutive([board[i + k][j - k] for k in range(4)])
            if winning_value is not None:
                return True, winning_value

    return False, None

def display_winning_screen(winner):
    '''displays screen telling the user which player won, and user can choose either exit game or start a new one'''

    global running


    pygame.draw.rect(screen, 'black', pygame.Rect(200,250,600,250), 4, 0, 15, 15)
    pygame.draw.rect(screen, 'grey92', pygame.Rect(204,254,592,242), 0, 0, 10, 10)
    font = pygame.font.SysFont('freesansbold.ttf', 90)
    text = font.render('Play Again?', True, 'black')
    text_pos = (320, 430)
    screen.blit(text, text_pos)

    if winner == 'b':
        font = pygame.font.SysFont('freesansbold.ttf', 120)
        text = font.render('Black Wins!', True, 'black')
        text_pos = (260, 290)
        screen.blit(text, text_pos)
    else:
        font = pygame.font.SysFont('freesansbold.ttf', 120)
        text = font.render('Red Wins!', True, 'red')
        text_pos = (290, 290)
        screen.blit(text, text_pos)



    yes_outline = pygame.Rect(200,500,300,100)
    no_outline = pygame.Rect(500,500,300,100)
    yes_rect = pygame.Rect(204,504,292,92)
    no_rect = pygame.Rect(504,504,292,92)

    pygame.draw.rect(screen, 'grey', yes_rect, 0, 0, 0, 0, 10, 0)
    pygame.draw.rect(screen, 'grey', no_rect, 0, 0, 0, 0, 0, 10)
    pygame.draw.rect(screen, 'black', yes_outline, 4, 0, 0, 0, 15, 0)
    pygame.draw.rect(screen, 'black', no_outline, 4, 0, 0, 0, 0, 15)

    font = pygame.font.SysFont('freesansbold.ttf', 90)
    text = font.render('Play Again?', True, 'black')
    text_pos = (320, 430)
    screen.blit(text, text_pos)

    yes_text = font.render('Yes', True, 'black')
    yes_text_pos = (290, 520)
    screen.blit(yes_text, yes_text_pos)

    no_text = font.render('No', True, 'black')
    no_text_pos = (600, 520)
    screen.blit(no_text, no_text_pos)
        
    pygame.display.flip()




    button_color = 'grey'
    while True:
        global game_in_progress
        if check_exit():
            return

        if yes_rect.collidepoint(pygame.mouse.get_pos()):
            # if the button is pressed, it will exit the start a new game and exit the function
            if pygame.mouse.get_pressed()[0]:
                game_in_progress = False
                return

            if button_color != 'grey':
                button_color = 'grey'
                pygame.draw.rect(screen, button_color, yes_rect, 0, 0, 0, 0, 15, 0)
                screen.blit(yes_text, yes_text_pos)
                pygame.display.flip()
        else:
            if button_color != 'grey93':
                button_color = 'grey93'
                pygame.draw.rect(screen, button_color, yes_rect, 0, 0, 0, 0, 15, 0)
                screen.blit(yes_text, yes_text_pos)
                pygame.display.flip()

        if no_rect.collidepoint(pygame.mouse.get_pos()):
            # if the no button is pressed, it will exit the program
            if pygame.mouse.get_pressed()[0]:
                running = False
                game_in_progress = False
                return

            if button_color != 'grey':
                button_color = 'grey'
                pygame.draw.rect(screen, button_color, no_rect, 0, 0, 0, 0, 0, 15)
                screen.blit(no_text, no_text_pos)
                pygame.display.flip()
        else:
            if button_color != 'grey93':
                button_color = 'grey93'
                pygame.draw.rect(screen, button_color, no_rect, 0, 0, 0, 0, 0, 15)
                screen.blit(no_text, no_text_pos)
                pygame.display.flip()

# initializes pygame and window
pygame.init()
screen = pygame.display.set_mode((1000, 830))
clock = pygame.time.Clock()
running = True

winner_log = open('winner_log.txt', 'w')
coordinate_dict = {}
black_score = 0
red_score = 0
log_list = []

display_rules('Start Game')
 

while running:

    # if user clicks X to close window, game will stop running
    check_exit()


    pygame.time.delay(200)

    if not running:
        break
    
    game_in_progress = True

    try:
        board, coordinate_dict = newgame(black_score, red_score)
    except:
        red_score, black_score = 0,0

    turn = 0

    # runs while the game is in progress
    while game_in_progress:

        # runs through the place() functions until both users have placed four squares
        while turn < 4:
            board = black_place(board)

            if not running:
                break

            board = red_place(board)
            turn += 1
            
            if not running:
                break


        if not running:
            break

        pygame.draw.rect(screen, 'black', pygame.Rect(750,10,240,80), 4)
        pygame.draw.rect(screen, 'white', pygame.Rect(754,14,232,72), 0)
        font = pygame.font.SysFont('freesansbold.ttf', 40) 

        text = font.render(f'Move a Square', True, 'black')
        text_pos = (775, 38)
        screen.blit(text, text_pos)
        pygame.display.flip()
        
        
        # checks to see if black won the game
        if check_win(board)[1] == 'b':
            display_winning_screen('b')
            black_score += 1
            log_list.append(f'Black wins round {red_score + black_score}\n')
            break
        
        # checks to see if black won the game
        elif check_win(board)[1] == 'r':
            display_winning_screen('r')
            red_score += 1
            log_list.append(f'Red wins round {red_score + black_score}\n')
            break

        else:
            board = black_move(board)

        if not running:
                break
        
        if check_win(board)[1] == 'b':
            display_winning_screen('b')
            black_score += 1
            log_list.append(f'Black wins round {red_score + black_score}\n')
            break

        elif check_win(board)[1] == 'r':
            display_winning_screen('r')
            red_score += 1
            log_list.append(f'Red wins round {red_score + black_score}\n')
            break

        else:
            board = red_move(board)


        if not running:
                break


    pygame.display.flip()
    clock.tick(60)

# opens a file called winner_log.txt and writes the final score as well as winners of each round
with open('winner_log.txt', 'w') as winner_log:
    winner_log.write(f'Final score - Black:{black_score}  Red:{red_score}\n\n')
    winner_log.writelines(log_list)
pygame.quit()
    
