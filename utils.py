import pygame
import math
import config 

def draw_text_centered(text, font, color, surface, center_x, center_y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(center_x, center_y))
    surface.blit(textobj, textrect)

def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    action_triggered = False
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(config.dis, ac, (x, y, w, h)) 
        if click[0] == 1:
            while pygame.mouse.get_pressed()[0]:
                pygame.event.pump() 
            action_triggered = True
    else:
        pygame.draw.rect(config.dis, ic, (x, y, w, h)) 
    text_surf = config.button_font.render(msg, True, config.BLACK)
    text_rect = text_surf.get_rect(center=(x + (w / 2), y + (h / 2)))
    config.dis.blit(text_surf, text_rect)
    return action_triggered

def show_score(score):
    score_surf = config.score_font.render(str(score), True, config.WHITE)
    config.dis.blit(score_surf, (10, 10))

# --- MATEMATIKA ZUMA ---

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Mengubah "Jarak Tempuh" menjadi koordinat X, Y di jalur
def get_pos_on_path(dist_traveled):
    current_dist = 0
    points = config.PATH_POINTS
    
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i+1]
        seg_len = distance(p1, p2)
        
        if current_dist + seg_len >= dist_traveled:
            # Bola berada di segmen ini
            remaining = dist_traveled - current_dist
            ratio = remaining / seg_len
            
            # Interpolasi Linear
            x = p1[0] + (p2[0] - p1[0]) * ratio
            y = p1[1] + (p2[1] - p1[1]) * ratio
            return int(x), int(y)
            
        current_dist += seg_len
    
    return points[-1] # Sampai ujung