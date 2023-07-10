import pygame
import os
import random
import tkinter as tk


# Initialize pygame
pygame.init()

# Create the screen
width, height = 500, 600
os.environ['SDL_VIDEO_WINDOW_POS'] = "{x},{y}".format(x=600, y=200)
screen = pygame.display.set_mode((width, height))

# Title and icon
pygame.display.set_caption("Sky Invader")
icon = pygame.image.load("IMG/dragon_icon.png")
pygame.display.set_icon(icon)


# Colours|RGB = Red, Green, Blue
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (150, 0, 0)
DARK_GREEN = (0, 80, 0)
VIOLET = (0, 0, 150)


# Background
background = pygame.image.load("IMG/sky.jpg")
lower_gap = 70

# Background music
music_volume = 0.4
volume = music_volume
pygame.mixer.music.load("Music/WoT.wav")
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(-1)


# Score
score_font = pygame.font.Font("Fonds/jack_font.ttf", 40)
highscore_font = pygame.font.Font("Fonds/jack_font.ttf", 30)


# Mouse is no longer visible
pygame.mouse.set_visible(False)

def show_score():
        score = score_font.render("Score:" + str(score_value), True, VIOLET)
        screen.blit(score, (10, 10))
        
        highscore = highscore_font.render("Highscore:" + str(highscore_value), True, BLACK)
        screen.blit(highscore, (width - 7*(width/16), 15))


# Player
player_img = pygame.image.load("IMG/triangle1.png")

def show_player(x, y):
    screen.blit(player_img, (x, y))


# Enemy
enemy_img = pygame.image.load("IMG/dragon.png")

def show_enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Bullet
bullet_img = pygame.image.load("IMG/bullet.png")

def show_bullet(x, y):
    global fire, bullet_fire, collision
    if bullet_fire:
        # Bullet sound
        if fire == False:
            bullet_sound = pygame.mixer.Sound("Music/laser.wav")
            bullet_sound.set_volume(0.4)
            if sounds:
                bullet_sound.play()
        fire = True
        bullet_fire = False
    if y < -20 or collision:
        fire = False
        collision = False
    if fire:
        screen.blit(bullet_img, (x, y))


# Checking if there was a collision
def collision_check():
    global collision
    disX, disY = abs((enemyX + 32) - (bulletX + 16)), abs(enemyY - bulletY)
    if disX < 32 and disY < velocity*3 + 64:
        collision = True


# Key controls
text_colour = WHITE
controls_font = pygame.font.Font("Fonds/coolvetica.ttf", 28)

space_text = controls_font.render("Shoot", True, text_colour)
space2_text = controls_font.render("[SPACE]", True, text_colour)

left_text = controls_font.render("Move left", True, text_colour)
left2_text = controls_font.render("[LEFT]", True, text_colour)

right_text = controls_font.render("Move right", True, text_colour)
right2_text = controls_font.render("[RIGHT]", True, text_colour)

up_text = controls_font.render("Reduce volume", True, text_colour)
up2_text = controls_font.render("[DOWN]", True, text_colour)

down_text = controls_font.render("Increase volume", True, text_colour)
down2_text = controls_font.render("[UP]", True, text_colour)

mute_text = controls_font.render("Mute music", True, text_colour)
mute2_text = controls_font.render("[M]", True, text_colour)

sound_text = controls_font.render("Mute sounds", True, text_colour)
sound2_text = controls_font.render("[N]", True, text_colour)

shift_text = controls_font.render("Start the game", True, text_colour)
shift2_text = controls_font.render("[SHIFT]", True, text_colour)

tab_text = controls_font.render("Pause", True, text_colour)
tab2_text = controls_font.render("[TAB]", True, text_colour)

highscore_text = controls_font.render("Highscores", True, text_colour)
highscore2_text = controls_font.render("[Q]", True, text_colour)

save_text = controls_font.render("Save score", True, text_colour)
save2_text = controls_font.render("[S]", True, text_colour)

exit_text = controls_font.render("Exit the game", True, text_colour)
exit2_text = controls_font.render("[ESC]", True, text_colour)

key_controls_font = pygame.font.Font("Fonds/coolvetica.ttf", 30)
key_controls = key_controls_font.render("Key controls [TAB]", True, text_colour)

def controls():
    x = 3*(width/20)
    y = height/10
    xX = width - 7*(width/20)
    gap = 37

    if not tab_click and not game and not highscore_tab:
        screen.blit(key_controls, (10, height - height/5))
    if tab_click:
        # Darker background
        dark = pygame.Surface((400, 12*gap + 20)).convert_alpha()
        dark.fill((0, 0, 0, 150))
        screen.blit(dark, (x - 10, y - 10))
        # Text
        screen.blit(space_text, (x, y))
        screen.blit(space2_text, (xX, y))
        screen.blit(left_text, (x, y + gap))
        screen.blit(left2_text, (xX, y + gap))
        screen.blit(right_text, (x, y + 2*gap))
        screen.blit(right2_text, (xX, y + 2*gap))
        screen.blit(up_text, (x, y + 3*gap))
        screen.blit(up2_text, (xX, y + 3*gap))
        screen.blit(down_text, (x, y + 4*gap))
        screen.blit(down2_text, (xX, y + 4*gap))
        screen.blit(mute_text, (x, y + 5*gap))
        screen.blit(mute2_text, (xX, y + 5*gap))
        screen.blit(sound_text, (x, y + 6*gap))
        screen.blit(sound2_text, (xX, y + 6*gap))
        screen.blit(shift_text, (x, y + 7*gap))
        screen.blit(shift2_text, (xX, y + 7*gap))
        screen.blit(tab_text, (x, y + 8*gap))
        screen.blit(tab2_text, (xX, y + 8*gap))
        screen.blit(highscore_text, (x, y + 9*gap))
        screen.blit(highscore2_text, (xX, y + 9*gap))
        screen.blit(save_text, (x, y + 10*gap))
        screen.blit(save2_text, (xX, y + 10*gap))
        screen.blit(exit_text, (x, y + 11*gap))
        screen.blit(exit2_text, (xX, y + 11*gap))


# Showing volume of music
speaker_pic = pygame.image.load("IMG/speaker.png")
mute_pic = pygame.image.load("IMG/mute.png")
music_pic = pygame.image.load("IMG/music.png")
rect1x = width - 25*(width/60)
rect1y = 20
rect2x = 25
rect2y = height - 13*(height/20)

def show_volume():
    if tab_click:
        if mute:
            volume_line = 0
        else:
            volume_line = (width/5) / 10 * (10 * music_volume)

        dark = pygame.Surface((40, 180)).convert_alpha()
        dark.fill((255, 255, 255, 70))
        screen.blit(dark, (9, 2*(height/20) - 10))
        
        dark2 = pygame.Surface((40, 40)).convert_alpha()
        dark2.fill((255, 255, 255, 70))
        screen.blit(dark2, (9, 8*(height/20) - 4))

        pygame.draw.rect(screen, WHITE, (rect2x, rect2y, 12, -(width/5)))
        pygame.draw.rect(screen, BLACK, (rect2x, rect2y, 12, -(volume_line)))

        if mute:
            screen.blit(mute_pic, (13, 2*(height/20)))
        if not mute:
            screen.blit(music_pic, (13, 2*(height/20)))
        if sounds:
            screen.blit(speaker_pic, (13, 8*(height/20)))
        if not sounds:
            screen.blit(mute_pic, (12, 8*(height/20)))


# Press shift to continue
def press_shift():
    global number_of_places
    
    textX = 0.5 * width - 100
    textY = 0.4 * height
    
    gameover_font = pygame.font.Font("Fonds/dark_college.otf", 40)
    gameover = gameover_font.render("Game Over", True, VIOLET)

    score_font = pygame.font.Font("Fonds/jack_font.ttf", 50)
    score = score_font.render("Score:" + str(score_value), True, WHITE)

    highscore_font = pygame.font.Font("Fonds/jack_font.ttf", 40)
    highscore = highscore_font.render("Highscore:" + str(highscore_value), True, BLACK)

    tom_best_font = pygame.font.Font("Fonds/college.ttf", 30)
    tom_best = tom_best_font.render("Tom\'s best: " + str(tom_best_value), True, WHITE)

    sky_font = pygame.font.Font("Fonds/dark_college.otf", 50)
    sky = sky_font.render("Sky Invader", True, VIOLET)

    dark = pygame.Surface((240, 50)).convert_alpha()
    dark.fill((0, 0, 0, 150))

    shift_textX = 0.5 * width - 200
    shift_textY = 0.9 * height
    shift_font = pygame.font.Font("Fonds/jack_font.ttf", 35)
    shift_text = shift_font.render("Press [Shift] to start", True, RED)

    if not highscore_tab:
        screen.blit(tom_best, (10, 10))

    if not tab_click and not highscore_tab:
        screen.blit(shift_text, (shift_textX, shift_textY))
        if not start:
            screen.blit(dark, (textX - 15, textY + 50))
            screen.blit(gameover, (textX, textY))
            screen.blit(score, (textX - 5, textY + 50))
            screen.blit(highscore, (textX - 25, textY - 100))

        elif start:
            screen.blit(sky, (5*(width/24), height/2 - height/10))


# Highscores
def show_highscores():
    global number_of_places

    x = 6*(width/20)
    y = height/10
    xX = width - 9*(width/20)
    gap = 45

    if highscore_tab:
        
        places = open('highscore.txt', 'r', encoding='utf-8')
        contents = places.readlines()

        for iii in range(1, int(len(contents)/2)):
            for i in range(1, int(len(contents)/2)):
                try:
                    while int(contents[i*2+1][:]) > int(contents[i*2-1][:]):
                        n = contents.index(contents[i*2-1])
                        contents.insert(n-1, contents[n+2])
                        contents.insert(n-1, contents[n+2])
                        del contents[n+3]
                        del contents[n+3]

                except IndexError:
                    pass
                except ValueError:
                    pass

        for line in range(0, len(contents)):
            number_of_places = int(line/2)+1

        # Darker backround
        dark = pygame.Surface((200, gap + 20)).convert_alpha()
        dark.fill((0, 0, 0, 150))
        screen.blit(dark, (x - 10, y - 10))
        dark2 = pygame.Surface((250, number_of_places*gap + 20)).convert_alpha()
        dark2.fill((0, 0, 0, 150))
        screen.blit(dark2, (x - 35, y - 10 + 2*gap))
        # Text
        highscores_text = controls_font.render("Highscores", True, text_colour)
        screen.blit(highscores_text, (x + 1*(width/30), y))

        for num in range(0, number_of_places):
            place1_text = controls_font.render(contents[num*2][0:-1], True, text_colour)
            place2_text = controls_font.render(contents[num*2+1][4:-1], True, text_colour)
            screen.blit(place1_text, (x - 35 + 10, height/4 + 45*num))
            screen.blit(place2_text, (width - width/3 - 15, height/4 + 45*num))
        
        places.close()


# Player direction
def direction():
    global playerX
    
    if left and playerX > 0:
        playerX -= player_vel
    if right and playerX < width - 64:
        playerX += player_vel


# Screen update
def renew_window():
    qx = 6*(width/20)
    qy = height/10
    screen.fill(BLACK)
    screen.blit(pygame.transform.scale(background, (width, height - lower_gap - (lower_gap - 64))), (0, 0))
    if game:
        show_score()
        show_player(playerX, playerY)
        show_enemy(enemyX, enemyY)
        show_bullet(bulletX, bulletY)
    if not game:
        press_shift()
        show_highscores()

    controls()
    show_volume()
    pygame.display.update()


# Game loop
def game_loop():
    global velocity, player_vel, playerX, playerY, score_value, left, right, enemy_vel, enemyX, enemyY, fire, bulletX, bulletY, bullet_vel, collision, bullet_fire

    # Global
    velocity = 7
    score_value = 0
    # Player
    player_vel = velocity
    playerX = (width / 2) - (64 / 2)
    playerY = height - lower_gap
    left, right = False, False
    # Enemy
    enemy_vel = velocity / 2
    enemyX = random.randrange(0, width - 64)
    enemyY = -64
    # Bullet
    fire = False
    bulletY = height - lower_gap - 30
    bulletX = playerX + 16
    bullet_vel = velocity * 2
    collision = False
    bullet_fire = False


# Game running
running = True
clock = pygame.time.Clock()
game = False
start = True
highscore_value = 0
tom_best_value = 86
tab_click = False
highscore_tab = False
mute = False
sounds = True
number_of_places = 0


game_loop()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key assignments, exactly at the moment of click
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not game:
                    running = False
                if game and not tab_click:
                    tab_click = not tab_click
                elif tab_click:
                    running = False

            if event.key == pygame.K_TAB:
                highscore_tab = False
                tab_click = not tab_click

            if event.key == pygame.K_q and not game:
                tab_click = False
                highscore_tab = not highscore_tab

            # Setting mute
            if event.key == pygame.K_m:
                mute = not mute
                if mute:
                    volume = 0
                elif not mute:
                    volume = music_volume
            pygame.mixer.music.set_volume(volume)
            if event.key == pygame.K_n:
                sounds = not sounds


            if event.key == pygame.K_s and not game and not highscore_tab and not tab_click and not start and s:
                may = False
                root = tk.Tk()
                root.geometry('200x100+750+400')
                root.title("Name")
                label = tk.Label(root, text="Your name")
                entry_name = tk.Entry(root)
                entry_name.focus_set()
                label.pack()
                entry_name.pack()

                def volanafunkce():
                    global player_name, may, s
                    player_name = entry_name.get()
                    may = True
                    s = False

                tlacitko = tk.Button(root, text=u"Click and then close", command=volanafunkce)
                tlacitko.pack()
                tk.mainloop()

                places_new = open('highscore.txt', 'a', encoding='utf-8')
                if may:
                    places_new.write(f'{player_name}\n    {score_value}\n')
                number_of_places += 1
                places_new.close()
                may = False

            if not game:
                # If game is False, refresh all important variables
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    if not tab_click and not highscore_tab:
                        game = True
                        s = True
                        game_loop()
                        start = False
            if game and not tab_click:
                if event.key == pygame.K_SPACE:
                    bullet_fire = True
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True

        if event.type == pygame.KEYUP or tab_click:
            if tab_click or event.key == pygame.K_LEFT:
                left = False
            if tab_click or event.key == pygame.K_RIGHT:
                right = False
    
    # Key assignments, when holding key
        # Setting volume
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            music_volume += 0.025
            volume = music_volume
            mute = False
        if event.key == pygame.K_DOWN:
            music_volume += -0.025
            volume = music_volume
            mute = False
        if music_volume < 0:
            music_volume = 0
            mute = True
        elif music_volume > 1:
            music_volume = 1
        pygame.mixer.music.set_volume(volume)

    # Checking direction
    direction()
    
    # Checking game, still running variables
    if game and not tab_click:
        enemyY += enemy_vel
        if fire:
            bulletY -= bullet_vel
            collision_check()
        if not fire:
            bulletX = playerX + 16
            bulletY = height - lower_gap - 30
        if collision:
            # Enemy reborn
            enemyX = random.randrange(0, width - 64)
            enemyY = -64
            # Score +1
            score_value += 1
            # Velocity
            velocity += 0.2
            player_vel = velocity
            enemy_vel = velocity / 2
            bullet_vel = velocity * 2
            # Sound of collision
            explosion_sound = pygame.mixer.Sound("Music/explosion.wav")
            explosion_sound.set_volume(0.3)
            if sounds:
                explosion_sound.play()

    if enemyY > height - lower_gap - (lower_gap - 64):
        game = False

    if score_value > highscore_value:
        highscore_value = score_value
    # Renewing window
    renew_window()


pygame.quit()
