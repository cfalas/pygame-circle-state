#!/usr/bin/python

import pygame
from pygame.locals import *
import pygame_textinput

def draw_circles(r1,r2,d, screen):
    screen_width = screen.get_size()[0]
    screen_height = 700
    width = 2*r1+2*r2+d
    distance_ratio = d/width * screen_width
    radius_ratio = (r1-r2)/width * screen_width
    pygame.draw.circle(screen, (0,0,0), (int(screen_width/2-distance_ratio/2 + radius_ratio/2),int(screen_height/2)), int((r1/width)*screen_width), 2)
    pygame.draw.line(screen, (0,0,0), (int(screen_width/2-distance_ratio/2 + radius_ratio/2),int(screen_height/2)), (int(screen_width/2-distance_ratio/2 + radius_ratio/2) + int((r1/width)*screen_width), int(screen_height/2)))
    pygame.draw.circle(screen, (0,0,0), (int(screen_width/2+distance_ratio/2 + radius_ratio/2),int(screen_height/2)), int((r2/width)*screen_width), 2)
    pygame.draw.line(screen, (0,0,0), (int(screen_width/2+distance_ratio/2 + radius_ratio/2),int(screen_height/2)), (int(screen_width/2+distance_ratio/2 + radius_ratio/2) - int((r2/width)*screen_width), int(screen_height/2)))


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Basic Pygame program')
    focus = ""
    screen.fill((250, 250, 250))

    # Fill background
    background = pygame.Surface((200,100))
    background = background.convert()
    background.fill((255,255,255))

    # Display some text
    font = pygame.font.Font(None, 36)
    text_r1 = font.render("Circle 1 Radius:", 1, (10, 10, 10))
    text_r2 = font.render("Circle 2 Radius:", 1, (10, 10, 10))
    text_d = font.render("Distance:", 1, (10, 10, 10))
    background.blit(text_r1, text_r1.get_rect())
    background.blit(text_r2, text_r2.get_rect(topleft=(0,30)))
    background.blit(text_d, text_d.get_rect(topleft=(0,60)))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    r1_input = pygame_textinput.TextInput(initial_string="2")
    r2_input = pygame_textinput.TextInput(initial_string="3")
    d_input = pygame_textinput.TextInput(initial_string="4")
    r1=2
    r2=3
    d=4
    answer = "Circles have two points of intersection"
    clock = pygame.time.Clock()
    # Event loop
    while 1:
        events = pygame.event.get()
        screen.fill((255,255,255))
        screen.blit(background, (0,0))
        for event in events:
            if event.type == QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if r1_rect.collidepoint(pos):
                    focus="r1"
                elif r2_rect.collidepoint(pos):
                    focus="r2"
                elif d_rect.collidepoint(pos):
                    focus="d"
                else:
                    r1 = float(r1_input.get_text())
                    r2 = float(r2_input.get_text())
                    d = float(d_input.get_text())
                    if d==0:
                        answer = "Circles are concentric"
                    elif r1+r2==d or (r1+d==r2 or r2+d==r1):
                        answer = "Circles are Tangent"
                    elif r1+r2<d or (r1+d<r2 or r2+d<r1):
                        answer = "Circles have no points of intersection"
                    elif r1+r2>d:
                        answer = "Circles have two points of intersection"
                print(focus)


        if focus=='r1':
            r1_input.update(events)
        elif focus=='r2':
            r2_input.update(events)
        elif focus=='d':
            d_input.update(events)
        else:
            d_input.update(events)
            r2_input.update(events)
            r1_input.update(events)

        r1_rect = screen.blit(r1_input.get_surface(), (200, 0))
        r2_rect = screen.blit(r2_input.get_surface(), (200, 30))
        d_rect = screen.blit(d_input.get_surface(), (200, 60))

        draw_circles(r1,r2,d, screen)
        text_answer = font.render(answer, 1, (10,10,10))
        screen.blit(text_answer, text_answer.get_rect(center=(screen.get_size()[0]/2,650)))

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__': main()
