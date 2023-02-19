import pygame
import numpy 

pygame.init()

#game window
(w,h) = (1200, 900)


screen = pygame.display.set_mode((w,h))

pygame.display.flip()


#Name of game display
TEXT_COL = (0,0,0)
font = pygame.font.SysFont("arialblack",80)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img, (x,y))

#Buttons

def button1(screen, position, text):
    font = pygame.font.SysFont("Arial", 70)
    text_render = font.render(text, 1, (255,255,255))
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.rect(screen, (0, 0, 0), (x, y, w ,h))
    return screen.blit(text_render, (x, y))

def button2(screen, position, text):
    font = pygame.font.SysFont("Arial", 70)
    text_render = font.render(text, 1, (255,255,255))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.rect(screen, (0, 0, 0), (x, y, w ,h))
    return screen.blit(text_render, (x, y))

 # Render n lines of text
def create_text(lines, font, color, x, y, line_spacing):
    rendered_lines = []
    y_offset = y

    for line in lines:
        text = font.render(line, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y_offset)
        rendered_lines.append((text, text_rect))
        y_offset += line_spacing
    
    return rendered_lines

def show_dialogue(rendered_lines):
    for line in rendered_lines:
               screen.blit(line[0], line[1])






def menu():
    """ This is the menu that waits you to click the s key to start """
    
    linesss = ["Rule", "No cheating", "Translate the picture"]
    font = pygame.font.Font('freesansbold.ttf', 32)
    color = (0, 0, 0)
    x = 600
    y = 250
    line_spacing = 50
    user_answer = ""

    rendered_lines = create_text(linesss, font, color, x, y, line_spacing)

    show_dialogue(rendered_lines)
    
    b2 = button1(screen, (400, 550), "Start")
    b1 = button2(screen, (600, 550), "Quit")

    while True:

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
        pygame.display.update()

def part2():


    # Set the dimensions of the screen
    screen_width = 1200
    screen_height = 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255,255,255))

    item = ['chiken']

    # Load the image
    image_path = (r"images/" + item[0] + ".png")
    image = pygame.image.load(image_path)

    # Set the size of the image
    image_width = 400
    image_height = 400
    image = pygame.transform.scale(image, (image_width, image_height))

    # Set the position of the image
    image_x = 400
    image_y = 300

    # Set the timer
    display_time = 3000  # in milliseconds
    end_time = pygame.time.get_ticks() + display_time

    # Blit (copy) the image onto the screen
    screen.blit(image,(image_x, image_y))

    # Update the display
    pygame.display.flip()

    # Name of the Window 
    pygame.display.set_caption('Game')

    # Font of text
    font = pygame.font.Font('freesansbold.ttf',32)

##    # Render n lines of text
##    def create_text(lines, font, color, x, y, line_spacing):
##        rendered_lines = []
##        y_offset = y
##
##        for line in lines:
##            text = font.render(line, True, color)
##            text_rect = text.get_rect()
##            text_rect.center = (x, y_offset)
##            rendered_lines.append((text, text_rect))
##            y_offset += line_spacing
##        
##        return rendered_lines

    line1 = ["You're lost bro"]
    line3 = ["Wow translator pro"]
    font = pygame.font.Font('freesansbold.ttf', 32)
    color = (0, 0, 0)
    x = 600
    y = 450
    line_spacing = 50
    user_answer = ""

    rendered_lines = create_text(line1, font, color, x, y, line_spacing)
    rendered_line = create_text(line3, font, color, x, y, line_spacing)

##    def show_dialogue():
##        for line in rendered_lines:
##                    screen.blit(line[0], line[1])

    # Add an event loop to keep the window open
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Check if the timer has run out
        if pygame.time.get_ticks() >= end_time:
            # Remove the image from the screen
            screen.fill((255,255,255))
            pygame.display.update()

            #Answer options
            q1a1 = button1(screen, (100, 200), "Cheekan")
            q1a2 = button2(screen, (100, 400), "Shekan")
            q1a3 = button1(screen, (700, 200), "ˈCHikən")
            q1a4 = button2(screen, (700, 400), "Chick")

            stop = 1

            while stop == 1:
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if q1a1.collidepoint(pygame.mouse.get_pos()):
                            user_answer += "A"
                            screen.fill((255,255,255))
                            show_dialogue(rendered_lines)
                            stop+1
                             
                            
                        elif q1a2.collidepoint(pygame.mouse.get_pos()):
                            user_answer += "B"
                            screen.fill((255,255,255))
                            show_dialogue(rendered_lines)
                            stop+1
                            
                        elif q1a3.collidepoint(pygame.mouse.get_pos()):
                            user_answer += "C"
                            screen.fill((255,255,255))
                            show_dialogue(rendered_line)
                            stop+1
                            
                        elif q1a4.collidepoint(pygame.mouse.get_pos()):
                            user_answer += "D"
                            screen.fill((255,255,255))
                            show_dialogue(rendered_lines)
                            stop+1
                        
                    pygame.display.update()
    
    
def start():
    part2()

#Transition with key - click
game_paused = False

run = True
while run:
    screen.fill((255,255,255))

    if game_paused == True:
        pass
        menu()

    else: 

        draw_text("Lost in Translation",font,TEXT_COL,200,300)
        draw_text("Press SPACE for menu",pygame.font.SysFont("arialblack",20),TEXT_COL,475,500)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True

        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()


pygame.quit()
