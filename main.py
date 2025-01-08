import pygame
import copy
import random

player_choice_list = []
round = 1
round_limit = 0
difficulty = 4
congrats_banner_toggle = 0
game_on = False
settings_on = False
instructions_on = False
guess_animation = False
replay_game = False
mastermind_choice_list = []
player_turn = False

class GuessAnimation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        blue_fire = pygame.image.load('./Mastermind/graphics/blue-fire-left.png').convert_alpha()
        blue_fire = pygame.transform.scale(blue_fire, (75,100))
        green_fire = pygame.image.load('./Mastermind/graphics/green-fire-left.png').convert_alpha()
        green_fire = pygame.transform.scale(green_fire, (75,100))
        orange_fire = pygame.image.load('./Mastermind/graphics/orange-fire-left.png').convert_alpha()
        orange_fire = pygame.transform.scale(orange_fire, (75,100))
        pink_fire = pygame.image.load('./Mastermind/graphics/pink-fire-left.png').convert_alpha()
        pink_fire = pygame.transform.scale(pink_fire, (75,100))
        red_fire = pygame.image.load('./Mastermind/graphics/red-fire-left.png').convert_alpha()
        red_fire = pygame.transform.scale(red_fire, (75,100))
        white_fire = pygame.image.load('./Mastermind/graphics/white-fire-left.png').convert_alpha()
        white_fire = pygame.transform.scale(white_fire, (75,100))
        yellow_fire = pygame.image.load('./Mastermind/graphics/yellow-fire-left.png').convert_alpha()
        yellow_fire = pygame.transform.scale(yellow_fire, (75,100))

        if guess == 'B':
            self.image = blue_fire
        elif guess == 'G':
            self.image = green_fire
        elif guess == 'O':
            self.image = orange_fire
        elif guess == 'P':
            self.image = pink_fire
        elif guess == 'R':
            self.image = red_fire
        elif guess == 'W':
            self.image = white_fire
        else:
            self.image = yellow_fire

        if index == 0:
            x_pos = 518
        elif index == 1:
            x_pos = 636
        elif index == 2:
            x_pos = 756
        else:
            x_pos = 876
        
        destination_x_pos = [170, 238, 310, 382]
        self.destination_x_pos = destination_x_pos[index]
        
        y_pos = 350

        if difficulty == 0:
            destination_y_pos = [672, 622, 572, 522, 472, 422, 372, 322, 272, 222, 172, 122]
        elif difficulty in [1,2,3]:
            destination_y_pos = [664, 604, 544, 484, 424, 364, 304, 244, 184, 124]
        else:
            destination_y_pos = [656, 580, 506, 430, 356, 280, 206, 130]
        self.destination_y_pos = destination_y_pos[round-1]

        self.rect = self.image.get_rect(topleft = (x_pos, y_pos))
    
    def clear_animations(self):
        if self.rect.x == self.destination_x_pos and self.rect.y == self.destination_y_pos-80:
            animation_group.empty()
    
    def update(self):
        if self.rect.x > self.destination_x_pos:
            self.rect.x -= 2
        if self.rect.y < self.destination_y_pos-80:
            self.rect.y += 1
        elif self.rect.y > self.destination_y_pos-80:
            self.rect.y -= 1
        self.clear_animations()

class PlayerGuess(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        if difficulty == 0:
            self.x_coords = [200, 268, 340, 411]
        else:
            self.x_coords = [203, 270, 342, 413]

        if difficulty == 0:
            self.y_coords = [671, 621, 571, 521, 471, 421, 371, 321, 271, 221, 171, 121]
        elif difficulty in [1,2,3]:
            self.y_coords = [663, 603, 543, 483, 423, 363, 303, 243, 183, 123]
        else:
            self.y_coords = [655, 580, 505, 430, 355, 280, 205, 130]
    
        blue_base = pygame.image.load('Mastermind/graphics/blue-base.png')
        blue_base = pygame.transform.scale(blue_base, (45,45))
        green_base = pygame.image.load('Mastermind/graphics/green-base.png')
        green_base = pygame.transform.scale(green_base, (45,45))
        orange_base = pygame.image.load('Mastermind/graphics/orange-base.png')
        orange_base = pygame.transform.scale(orange_base, (45,45))
        pink_base = pygame.image.load('Mastermind/graphics/pink-base.png')
        pink_base = pygame.transform.scale(pink_base, (45,45))
        red_base = pygame.image.load('Mastermind/graphics/red-base.png')
        red_base = pygame.transform.scale(red_base, (45,45))
        white_base = pygame.image.load('Mastermind/graphics/white-base.png')
        white_base = pygame.transform.scale(white_base, (45,45))
        yellow_base = pygame.image.load('Mastermind/graphics/yellow-base.png')
        yellow_base = pygame.transform.scale(yellow_base, (45,45))       

        if guess == 'B':
            self.image = blue_base
        elif guess == 'G':
            self.image = green_base
        elif guess == 'O':
            self.image = orange_base
        elif guess == 'P':
            self.image = pink_base
        elif guess == 'R':
            self.image = red_base
        elif guess == 'W':
            self.image = white_base
        else:
            self.image = yellow_base


        self.rect = self.image.get_rect(center = (self.x_coords[index], self.y_coords[round-1]))

black_pegs = 0
white_pegs = 0

class MastermindChoice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
        blue_base = pygame.image.load('Mastermind/graphics/blue-base.png')
        blue_base = pygame.transform.scale(blue_base, (45,45))
        green_base = pygame.image.load('Mastermind/graphics/green-base.png')
        green_base = pygame.transform.scale(green_base, (45,45))
        orange_base = pygame.image.load('Mastermind/graphics/orange-base.png')
        orange_base = pygame.transform.scale(orange_base, (45,45))
        pink_base = pygame.image.load('Mastermind/graphics/pink-base.png')
        pink_base = pygame.transform.scale(pink_base, (45,45))
        red_base = pygame.image.load('Mastermind/graphics/red-base.png')
        red_base = pygame.transform.scale(red_base, (45,45))
        white_base = pygame.image.load('Mastermind/graphics/white-base.png')
        white_base = pygame.transform.scale(white_base, (45,45))
        yellow_base = pygame.image.load('Mastermind/graphics/yellow-base.png')
        yellow_base = pygame.transform.scale(yellow_base, (45,45))

        self.mm_coords = [(200,57), (270,57), (343,57), (412,57)]     

        if choice == 'B':
            self.image = blue_base
        elif choice == 'G':
            self.image = green_base
        elif choice == 'O':
            self.image = orange_base
        elif choice == 'P':
            self.image = pink_base
        elif choice == 'R':
            self.image = red_base
        elif choice == 'W':
            self.image = white_base
        else:
            self.image = yellow_base

        self.rect = self.image.get_rect(center = (self.mm_coords[indy]))

class Pegs(pygame.sprite.Sprite):
    def __init__(self, peg, peg_index, round, difficulty):
        super().__init__()
        self.peg = peg
        self.peg_index = peg_index
        self.round = round
        self.difficulty = difficulty

        if difficulty == 0:
            peg_x_coords = [129, 154]
            peg_y_coords = [[663, 685], [613, 635], [563, 585], [513, 535],
                            [463, 485], [413, 435], [363, 385], [313, 335],
                            [263, 285], [213, 235], [163, 185], [113, 135]]
        elif difficulty == 4:
            peg_x_coords = [132, 157]
            peg_y_coords = [[643, 678], [569, 604], [495, 530], [421, 456],
                            [347, 382], [273, 308], [199, 234], [125, 160]]
        else:
            peg_x_coords = [131, 156]
            peg_y_coords = [[655, 683], [595, 623], [535, 563], [475, 503], [415, 443], 
                            [355, 383], [295, 323], [235, 263], [175, 203], [115, 143]]
            
        if peg_index in [0,1]:
            self.x_coord = peg_x_coords[0]
        else:
            self.x_coord = peg_x_coords[1]
        if peg_index in [0,2]:
            self.y_coord = peg_y_coords[round-1][0]
        else:
            self.y_coord = peg_y_coords[round-1][1]
        
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)

        if peg == 'b':
            pygame.draw.circle(self.image, (0, 0, 0), (8, 8), 8)
        else:
            pygame.draw.circle(self.image, (255, 255, 255), (8, 8), 8)
  
        self.rect = self.image.get_rect(center = (self.x_coord, self.y_coord))

def mm_choice(diff):
    colour_list_easy = ['B', 'G', 'P', 'R', 'W']
    colour_list_normal = ['B', 'G', 'O', 'P', 'R', 'W']
    colour_list_hard = ['B', 'G', 'O', 'P', 'R', 'W', 'Y']
    mastermind_choice = []
    
    if diff == 0 or diff == 1:
        mastermind_choice = [colour_list_easy[random.randint(0, 4)] for _ in range(4)]
    elif diff == 3 or diff == 4:
        mastermind_choice = [colour_list_hard[random.randint(0, 6)] for _ in range(4)]
    else:
        mastermind_choice = [colour_list_normal[random.randint(0, 5)] for _ in range(4)]
    return mastermind_choice

def reconcile_choice(pcl, mcl):
    print(f'Player Choice: {pcl}')
    print(f'Mastermind Choice: {mcl}')

    black_peg_indexes = []

    for x in range(len(pcl)):
        print(pcl)
        print(mcl)
        mcl_copy = copy.copy(mcl)
        if pcl[x] == mcl_copy[x]:
            black_peg_indexes.append(x)
            black_peg_indexes.sort(reverse=True)
    if len(black_peg_indexes) > 0:
        for y in black_peg_indexes:
            mcl_copy.pop(y)
            pcl.pop(y)
        print(pcl)
        print(mcl_copy)
    black_pegs = len(black_peg_indexes)
    white_pegs = 0

    for i in (pcl):
        if i in mcl_copy: 
            mcl_copy.remove(i)
            white_pegs += 1

    return black_pegs, white_pegs

def display_round(r, rl):
    round_surface = round_font.render(f'ROUND: {round} / {rl}', False, 'White')
    round_rect = round_surface.get_rect(center = (660, 63))
    screen.blit(round_surface, round_rect)

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mastermind')
clock = pygame.time.Clock()
title_font = pygame.font.Font('./Mastermind/fonts/Pixeltype.ttf', 100)
instruction_font = pygame.font.Font('./Mastermind/fonts/Pixeltype.ttf', 60)
difficulties_font = pygame.font.Font('./Mastermind/fonts/Pixeltype.ttf', 55)
user_text_font = pygame.font.Font(None,40)
round_font = pygame.font.Font('./Mastermind/fonts/Pixeltype.ttf', 80)

pygame_icon = pygame.image.load('Mastermind/graphics/mastermind-alien-icon.png')
pygame.display.set_icon(pygame_icon)

background = pygame.image.load('./Mastermind/graphics/space-bg.png').convert_alpha()
game_bg = pygame.image.load('./Mastermind/graphics/spaceship-interior.png').convert_alpha()

mastermind_alien = pygame.image.load('./Mastermind/graphics/mastermind-alien-img.png').convert_alpha()
mastermind_alien_rect = mastermind_alien.get_rect(center = (700,350))

# start page
title_surface = title_font.render('MASTERMIND', False, 'White')
title_rect = title_surface.get_rect(center = (200,50))
enter_name_surface = instruction_font.render('ENTER YOUR NAME', False, 'White')
enter_name_rect = enter_name_surface.get_rect(center = (200,220))

settings_surface = instruction_font.render('START THE GAME', False, 'White')
settings_rect = settings_surface.get_rect(center = (200,450))
startinstruction_surface = instruction_font.render('INSTRUCTIONS', False, 'White')
startinstruction_rect = startinstruction_surface.get_rect(center = (200,650))

user_text = ''
input_rect = pygame.Rect(75,250,140,34)
color = pygame.Color('white')

# settings page
difficulty_surface = instruction_font.render('DIFFICULTY', False, 'black')
difficulty_rect = difficulty_surface.get_rect(center = (500,100))
difficulties_surface = difficulties_font.render('BABY           EASY           NORMAL           HARD', False, 'black')
difficulties_rect = difficulties_surface.get_rect(center = (415,200))
masterchief_surface = difficulties_font.render('MASTER\n  CHIEF', False, 'black')
masterchief_rect = enter_name_surface.get_rect(center = (920,165))

difficulty_img = pygame.transform.rotozoom(pygame_icon,0,0.1)
clicked_img = pygame.image.load('./Mastermind/graphics/ufo.png').convert_alpha()
clicked_img = pygame.transform.rotozoom(clicked_img,0,0.15)
clicked_index = 2
clicked_coords = [(155,230), (314,230), (492,230), (669,230), (822,230)]

baby_rect = difficulty_img.get_rect(center = (153,275))
easy_rect = difficulty_img.get_rect(center = (312,275))
normal_rect = difficulty_img.get_rect(center = (490,275))
hard_rect = difficulty_img.get_rect(center = (667,275))
master_rect = difficulty_img.get_rect(center = (820,275))

play_surface = title_font.render('PLAY', False, 'white')
play_rect = enter_name_surface.get_rect(center = (579,600))
img_rects = {(133,260):0, (292,260):0, (470,260):0, (647,260):0, (800,260):0}



# instruction pages
instruction_toggle = 0

instruction_surface_1 = instruction_font.render('''
                                              You were travelling in your spaceship 
                                                                 when you are captured 
                                                                by alien forces. They want 
                                                         to test the intelligence of your 
                                                    species and give you a challenge.\n
                                                          Earn their respect playing 
                                                    their game to win your freedom. 
                                               Or they will improve universal intellect ... 
                                                                   by executing you!
                                              ''', False, 'White')
instruction_rect_1 = instruction_surface_1.get_rect(center = (325,250))
backtostart_surface = instruction_font.render('BACK', False, 'White')
backtostart_rect = backtostart_surface.get_rect(center = (500,650))

instruction_surface_2 = instruction_font.render('''
                                                The Alien Mastermind has selected 4 colours of
                                                           fire and hidden them behind the orbs. 


                                                Guess a combination of 4 colours and check the 
                                                pegs that are returned to the left of each row.
                                                BLACK PEG - A fire is the right colour
                                                                             and in the right spot
                                                WHITE PEG - A fire is the right colour but wrong spot


                                                
                                                          Get 4 black pegs returned before the
                                                                              end of the rounds....
                                                                              OR FACE YOUR DOOM!
                                              ''', False, 'White')
instruction_rect_2 = instruction_surface_2.get_rect(center = (325,320))
backtostart_surface = instruction_font.render('BACK', False, 'White')
backtostart_rect = backtostart_surface.get_rect(center = (500,650))
instruct_orbs = pygame.image.load('./Mastermind/graphics/instruct-orbs.png').convert_alpha()
instruct_orbs = pygame.transform.scale(instruct_orbs, (330,60))
instruct_orbs_rect = instruct_orbs.get_rect(center = (500,145))
instruct_fires_pegs = pygame.image.load('./Mastermind/graphics/instruct-fires-pegs.png').convert_alpha()
instruct_fires_pegs = pygame.transform.scale(instruct_fires_pegs, (400,90))
instruct_fires_pegs_rect = instruct_fires_pegs.get_rect(center = (500,430))

instruction_surface = [instruction_surface_1, instruction_surface_2]
instruction_rect = [instruction_rect_1, instruction_rect_2]

# game_on
game_bg = pygame.image.load('./Mastermind/graphics/spaceship-interior.png').convert_alpha()
board_8 = pygame.image.load('./Mastermind/graphics/8-board.png').convert_alpha()
board_10 = pygame.image.load('./Mastermind/graphics/10-board.png').convert_alpha()
board_12 = pygame.image.load('./Mastermind/graphics/12-board.png').convert_alpha()
orb = pygame.image.load('./Mastermind/graphics/magic-glass-orb.png').convert_alpha()

board_8 = pygame.transform.scale(board_8, (330,600))
front_row_rect_8 = board_8.get_rect(midbottom = (283, 700))

board_10 = pygame.transform.scale(board_10, (330,600))
front_row_rect_10 = board_10.get_rect(midbottom = (282, 700))

board_12 = pygame.transform.rotozoom(board_12, 0, 0.55)
front_row_rect_12 = board_12.get_rect(midbottom = (280, 700))

orb = pygame.transform.rotozoom(orb, 0, 0.15)

clear_surface = instruction_font.render('CLEAR', False, 'White')
clear_rect = clear_surface.get_rect(center = (570,550))

guess_surface = instruction_font.render('GUESS', False, 'Green')
guess_rect = guess_surface.get_rect(center = (870,550))

replay_surface = title_font.render('REPLAY?', False, 'Blue')
replay_rect = enter_name_surface.get_rect(center = (750,400))
replay_yes_surface = instruction_font.render('YES', False, 'Green')
replay_yes_rect = enter_name_surface.get_rect(center = (775,500))
replay_no_surface = instruction_font.render('NO', False, 'Red')
replay_no_rect = enter_name_surface.get_rect(center = (940,500))

congrats_banner = pygame.image.load('./Mastermind/graphics/congrats-banner.png').convert_alpha()
congrats_banner = pygame.transform.scale(congrats_banner, (500,200))
fail_banner = pygame.image.load('./Mastermind/graphics/failed-banner.png').convert_alpha()
fail_banner = pygame.transform.scale(fail_banner, (500,200))
bannerlist = [fail_banner, congrats_banner]
banner_rect = bannerlist[congrats_banner_toggle].get_rect(center = (730, 230))

blue_fire_left = pygame.image.load('./Mastermind/graphics/blue-fire-left.png').convert_alpha()
blue_fire_left = pygame.transform.scale(blue_fire_left, (75,100))

green_fire_left = pygame.image.load('./Mastermind/graphics/green-fire-left.png').convert_alpha()
green_fire_left = pygame.transform.scale(green_fire_left, (75,100))

orange_fire_left = pygame.image.load('./Mastermind/graphics/orange-fire-left.png').convert_alpha()
orange_fire_left = pygame.transform.scale(orange_fire_left, (75,100))

pink_fire_left = pygame.image.load('./Mastermind/graphics/pink-fire-left.png').convert_alpha()
pink_fire_left = pygame.transform.scale(pink_fire_left, (75,100))

red_fire_left = pygame.image.load('./Mastermind/graphics/red-fire-left.png').convert_alpha()
red_fire_left = pygame.transform.scale(red_fire_left, (75,100))

white_fire_left = pygame.image.load('./Mastermind/graphics/white-fire-left.png').convert_alpha()
white_fire_left = pygame.transform.scale(white_fire_left, (75,100))

yellow_fire_left = pygame.image.load('./Mastermind/graphics/yellow-fire-left.png').convert_alpha()
yellow_fire_left = pygame.transform.scale(yellow_fire_left, (75,100))

yellow_choice_rect = yellow_fire_left.get_rect(midbottom = (500, 700))
blue_choice_rect = blue_fire_left.get_rect(midbottom = (575, 700))
green_choice_rect = green_fire_left.get_rect(midbottom = (650, 700))
pink_choice_rect = pink_fire_left.get_rect(midbottom = (725, 700))
red_choice_rect = red_fire_left.get_rect(midbottom = (800, 700))
white_choice_rect = white_fire_left.get_rect(midbottom = (875, 700))
orange_choice_rect = orange_fire_left.get_rect(midbottom = (950, 700))

player_choice_fires_list = [
                yellow_fire_left,
                blue_fire_left,
                green_fire_left,
                pink_fire_left,
                red_fire_left,
                white_fire_left,
                orange_fire_left]

player_choice_map_dictionary = {
'Y' : 0,
'B' : 1,
'G' : 2,
'P' : 3,
'R' : 4,
'W' : 5,
'O' : 6}
player_choice_fires_coords = [(515,350), (635,350), (755,350), (875,350)]

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 600)
animation_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

while True:
    screen.fill((228,202,241))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if not settings_on and not instructions_on:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(event.pos):
                    print('settings')
                    settings_on = True
                    print(user_text)
                    
                if startinstruction_rect.collidepoint(event.pos):
                    print('instructions')
                    instructions_on = True
            
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
    
                else:
                    if len(user_text) < 12:
                        user_text += event.unicode.upper()
        
        user_text_surface = user_text_font.render(user_text, True, (255,0,255))

        if settings_on:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if baby_rect.collidepoint(event.pos):
                    clicked_index = 0
                    print('baby')
                if easy_rect.collidepoint(event.pos):
                    clicked_index = 1
                    print('easy')
                if normal_rect.collidepoint(event.pos):
                    clicked_index = 2
                    print('normal')
                if hard_rect.collidepoint(event.pos):
                    clicked_index = 3
                    print('hard')
                if master_rect.collidepoint(event.pos):
                    clicked_index = 4
                    print('master')
                if play_rect.collidepoint(event.pos):
                    print('play')
                    settings_on = False
                    game_on = True
                    difficulty = clicked_index

        if instructions_on:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backtostart_rect.collidepoint(event.pos):
                    instructions_on = False
                    instruction_toggle = 0
                if pygame.draw.polygon(screen, (255, 255, 255), ((900,625),(950,650),(900,675))).collidepoint(event.pos):
                    instruction_toggle = 1
                if pygame.draw.polygon(screen, (255, 255, 255), ((150,625),(100,650),(150,675))).collidepoint(event.pos):
                    instruction_toggle = 0 
        
        if replay_game:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_yes_rect.collidepoint(event.pos):
                    obstacle_group.empty()
                    mastermind_choice_list = []
                    replay_game = False
                    game_on = True
                
                if replay_no_rect.collidepoint(event.pos):
                    obstacle_group.empty()
                    mastermind_choice_list = []
                    replay_game = False
                    game_on = False
                    congrats_banner_toggle = 0

        if player_turn:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(player_choice_list) < 4:
                    if  blue_choice_rect.collidepoint(event.pos):
                        player_choice_list.append('B')
                        print('B')
                    elif green_choice_rect.collidepoint(event.pos):
                        player_choice_list.append('G')
                        print('G')
                    elif pink_choice_rect.collidepoint(event.pos):
                        player_choice_list.append('P')
                        print('P')
                    elif red_choice_rect.collidepoint(event.pos):
                        player_choice_list.append('R')
                        print('R')
                    elif white_choice_rect.collidepoint(event.pos):
                        player_choice_list.append('W')
                        print('W')

                    if difficulty in [3,4]:
                        if yellow_choice_rect.collidepoint(event.pos):
                            player_choice_list.append('Y')
                            print('Y')

                    if difficulty in [2,3,4]:
                        if orange_choice_rect.collidepoint(event.pos):
                            player_choice_list.append('O')
                            print('O')

                if len(player_choice_list) > 0:
                    if clear_rect.collidepoint(event.pos):
                            player_choice_list.clear()

                if len(player_choice_list) == 4:
                    if guess_rect.collidepoint(event.pos):
                        guess_choice_list = copy.copy(player_choice_list)
                        guess_animation = True
                        player_turn = False
                        for index,guess in enumerate(player_choice_list):
                            animation_group.add(GuessAnimation())
                            obstacle_group.add(PlayerGuess())
                        

            

    if settings_on:
        screen.blit(game_bg, (0,0))
        pygame.draw.rect(screen, 'grey', pygame.Rect(100, 50, 800, 300))
        screen.blit(difficulty_surface, difficulty_rect)
        pygame.draw.line(screen, 'black', (385,120), (605,120), width=5)
        screen.blit(difficulties_surface, difficulties_rect)
        screen.blit(masterchief_surface, masterchief_rect)
        difficulty_keys_list = list(img_rects.keys())

        for i in range(5):
            screen.blit(difficulty_img, difficulty_keys_list[i])
        clicked_rect = clicked_img.get_rect(center = clicked_coords[clicked_index])
        screen.blit(clicked_img, clicked_rect)    
        screen.blit(play_surface, play_rect)
        
    elif instructions_on:
        screen.blit(background, (0,0))
        screen.blit(instruction_surface[instruction_toggle], instruction_rect[instruction_toggle])
        screen.blit(backtostart_surface, backtostart_rect)

        if instruction_toggle == 0:
            pygame.draw.polygon(screen, (255, 255, 255), ((900,625),(950,650),(900,675)))
        else: 
            pygame.draw.polygon(screen, (255, 255, 255), ((150,625),(100,650),(150,675)))
            screen.blit(instruct_orbs, instruct_orbs_rect)
            screen.blit(instruct_fires_pegs, instruct_fires_pegs_rect)

    elif game_on:
        screen.blit(game_bg, (0,0))
        display_round(round, round_limit)
        screen.blit(blue_fire_left, blue_choice_rect)
        screen.blit(green_fire_left, green_choice_rect)
        screen.blit(pink_fire_left, pink_choice_rect)
        screen.blit(red_fire_left, red_choice_rect)
        screen.blit(white_fire_left, white_choice_rect)

        if not replay_game:
            pygame.draw.rect(screen, (160,160,160), (500, 518, 140, 55))
            pygame.draw.rect(screen, (240,240,240), (500, 518, 140, 55), width=5)
            pygame.draw.rect(screen, (160,160,160), (800, 518, 138, 55))
            pygame.draw.rect(screen, 'Green', (800, 518, 138, 55), width=5)
            screen.blit(clear_surface, clear_rect)
            screen.blit(guess_surface, guess_rect)

        if replay_game:
            pygame.draw.rect(screen, (160,160,160), (578, 367, 285, 72))
            pygame.draw.rect(screen, 'Blue', (578, 367, 285, 72), width=5)
            pygame.draw.rect(screen, (160,160,160), (605, 468, 95, 55))
            pygame.draw.rect(screen, 'Green', (605, 468, 95, 55), width=5)
            pygame.draw.rect(screen, (160,160,160), (767, 468, 72, 55))
            pygame.draw.rect(screen, 'Red', (767, 468, 72, 55), width=5)
            screen.blit(replay_surface, replay_rect)
            screen.blit(replay_yes_surface, replay_yes_rect)
            screen.blit(replay_no_surface, replay_no_rect)
            screen.blit(bannerlist[congrats_banner_toggle], banner_rect)

        else:

            orb_rect1 = orb.get_rect(center = ((198,60)))
            orb_rect2 = orb.get_rect(center = ((268,60)))
            orb_rect3 = orb.get_rect(center = ((340,60)))
            orb_rect4 = orb.get_rect(center = ((410,60)))
            screen.blit(orb, orb_rect1)
            screen.blit(orb, orb_rect2)
            screen.blit(orb, orb_rect3)
            screen.blit(orb, orb_rect4)

        if difficulty == 0:
            screen.blit(board_12, front_row_rect_12)
            round_limit = 12
        elif difficulty == 1:
            screen.blit(board_10, front_row_rect_10)
            round_limit = 10
        elif difficulty == 2:
            screen.blit(board_10, front_row_rect_10)
            screen.blit(orange_fire_left, orange_choice_rect)
            round_limit = 10
        elif difficulty == 3:
            screen.blit(board_10, front_row_rect_10)
            screen.blit(orange_fire_left, orange_choice_rect)
            screen.blit(yellow_fire_left, yellow_choice_rect)
            round_limit = 10
        elif difficulty == 4:
            screen.blit(board_8, front_row_rect_8)
            screen.blit(orange_fire_left, orange_choice_rect)
            screen.blit(yellow_fire_left, yellow_choice_rect)
            round_limit = 8

        if len(mastermind_choice_list) == 0:
            mastermind_choice_list = mm_choice(difficulty)
            print(mastermind_choice_list)
            round = 1
            player_turn = True
        
        if player_turn and len(player_choice_list)!= 0:
            fire_index = 0
            coord_index = 0
            for item in player_choice_list:
                fire_index = player_choice_map_dictionary[item]
                fire_img = player_choice_fires_list[fire_index]
                screen.blit(fire_img, player_choice_fires_coords[coord_index])
                coord_index += 1

        if not player_turn:
            guess_choice_list.clear()
            print(f'round: {round}')
            peg_list = []
            black_pegs, white_pegs = reconcile_choice(player_choice_list, mastermind_choice_list)
            for bp in range(black_pegs):
                peg_list.append('b')
            for wp in range(white_pegs):
                peg_list.append('w')
            if len(peg_list) == 0:
                pass
            else:
                for peg_index, peg in enumerate(peg_list):
                    obstacle_group.add(Pegs(peg, peg_index, round, difficulty))

            print(black_pegs)
            print(mastermind_choice_list)
            if black_pegs != 4:
                player_choice_list.clear()
                player_turn = True
                
                if round == round_limit:
                    print('Game Over because you went over round limit')
                    replay_game = True
                    for indy,choice in enumerate(mastermind_choice_list):
                        obstacle_group.add(MastermindChoice())
                        congrats_banner_toggle = 0
                else:
                    round += 1

            else:
                print('Game Over because you won')
                replay_game = True
                for indy,choice in enumerate(mastermind_choice_list):
                    obstacle_group.add(MastermindChoice())
                congrats_banner_toggle = 1

        animation_group.update()
        animation_group.draw(screen)
        obstacle_group.update()
        obstacle_group.draw(screen)

    else:
        screen.blit(background, (0,0))
        screen.blit(mastermind_alien, mastermind_alien_rect)
        screen.blit(title_surface, title_rect)
        screen.blit(settings_surface, settings_rect)
        screen.blit(startinstruction_surface, startinstruction_rect)
        screen.blit(enter_name_surface, enter_name_rect)
        screen.blit(user_text_surface, (input_rect.x + 5, input_rect.y+4))
        input_rect.w = user_text_surface.get_width() + 10
        pygame.draw.rect(screen,color,input_rect,3)
        
    pygame.display.update()
pygame.quit()