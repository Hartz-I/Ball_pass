import pygame
import sys

def run_game():
    pygame.init()
    screen_width=1000
    screen_height=600
    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Ball pass'.title())

    box_1_width = 20
    box_1_height = 100
    box_1x=0
    box_1y=300-box_1_height/2

    box_2_width = 20
    box_2_height = 100
    box_2x = 1000-box_2_width
    box_2y = 300 - box_1_height // 2

    box_vel=1

    radius=10
    ball_x=(screen_width//2)-radius
    ball_y=(screen_height//2)+radius
    ball_move=False
    move_ver=False
    move_ver_up=False
    move_ver_down=False
    ball_dir_x=1
    ball_dir_y=1
    ball_hit_up=1
    ball_hit_down=(-1)
    ball_speed=2

    ball_exist=True

    point_1=0
    point_2=0


    #sounds
    score=pygame.mixer.Sound('score.wav')
    hit=pygame.mixer.Sound('hit.wav')
    hit_1=pygame.mixer.Sound('hit_1.wav')

    music=pygame.mixer.music.load('bg_sound.mp3')
    pygame.mixer.music.play(-1)

    font = pygame.font.SysFont('comicsans',30, True, True)

    while True:
        pygame.time.delay(5)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        screen.fill((113,215,98))

        player_1=pygame.draw.rect(screen,(101,67,33),(box_1x,box_1y,box_1_width,box_1_height))
        player_2=pygame.draw.rect(screen, (92,72,146), (box_2x, box_2y, box_2_width, box_2_height))
        if ball_exist:
            pygame.draw.circle(screen,(0,0,255),(ball_x,ball_y),radius)

        keys=pygame.key.get_pressed()


        if keys[pygame.K_q]:
            if box_1y>5:
                box_1y-=box_vel

        if keys[pygame.K_a]:
            if box_1y<=495:
                box_1y+=box_vel

        if keys[pygame.K_p]:
            if box_2y>5:
                box_2y-=box_vel

        if keys[pygame.K_l]:
            if box_2y<=495:
                box_2y+=box_vel

        if keys[pygame.K_SPACE]:
            ball_move=True


        if ball_move:
            ball_x += ball_speed * ball_dir_x


        else:
            screen.blit(pygame.image.load('intro_500.png'),((screen_width//2)-250,(screen_height//2)-250))

        if ball_x<=box_1x+box_1_width+5 and ball_y+2*radius>=box_1y and  ball_y<box_1y+(box_1_height//2):
            ball_dir_x*=(-1)
            hit_1.play()
            move_ver_up=True
            move_ver_down=False

        elif ball_x<=box_1x+box_1_width+5 and ball_y+2*radius>=box_1y+(box_1_height//2) and  ball_y<box_1y+box_1_height:
            ball_dir_x*=(-1)
            hit_1.play()
            move_ver_up = False
            move_ver_down = True

        #elif ball_x<=box_1x+box_1_width:
           # if ball_y+2*radius>=box_1y+(box_1_height//2)-10 and  ball_y<box_1y+(box_1_height//2)+10:
               # ball_dir_x*=(-1)
                #move_ver_down = False
                #move_ver_up = False







        elif ball_x>=box_2x and ball_y+2*radius>=box_2y and ball_y<box_2y+(box_2_height//2):
            ball_dir_x*=(-1)
            hit_1.play()
            move_ver_up=True
            move_ver_down=False

        elif ball_x>=box_2x and ball_y+2*radius>=box_2y+(box_2_height//2) and ball_y<box_2y+box_2_height:
            ball_dir_x*=(-1)
            hit_1.play()
            move_ver_up=False
            move_ver_down=True





        """if ball_dir_x>0 and ball_dir_y<0:
            ball_hit_up=-1
        else:
            ball_hit_up=1"""
                
        

        if move_ver_up:
            ball_y-=1*ball_hit_up*ball_dir_y
        if move_ver_down:
            ball_y-=1*ball_hit_down*ball_dir_y


        if ball_exist:
            if ball_x<=0:
                ball_exist=False
                move_ver_up=False
                move_ver_down=False
                score.play()
                #print('You Lose!')
                point_1+=1
                ball_x = (screen_width // 2) - radius
                ball_y = (screen_height // 2) + radius
                ball_exist=True
                i=0
                while i<300:
                    pygame.time.delay(10)

                    font_s = pygame.font.SysFont('comicsans', 30, True, True)
                    text_s = font_s.render("Score!!", 1, (255, 255, 255))
                    screen.blit(text_s, (500, 300))

                    i+=1

                    pygame.display.update()
            if ball_x >= screen_width:
                ball_exist = False
                move_ver_up = False
                move_ver_down = False
                #print('You Lose!')
                score.play()
                point_2+=1
                ball_x = (screen_width // 2) - radius
                ball_y = (screen_height // 2) + radius
                ball_exist=True

                i = 0
                while i < 300:
                    pygame.time.delay(10)

                    font_s = pygame.font.SysFont('comicsans', 30, True, True)
                    text_s = font_s.render("Score!!", 1, (255, 255, 255))
                    screen.blit(text_s, (500-50, 300-30))

                    i += 1

                    pygame.display.update()

            if ball_y<0 or ball_y+2*radius>screen_height:
                hit.play()
                ball_dir_y*=(-1)

        text = font.render('Score Board: '+str(point_2) + " : " + str(point_1), 1, (255, 255, 255))
        screen.blit(text,(700,50))



        pygame.display.update()

run_game()
