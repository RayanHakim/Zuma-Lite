import pygame
import config
import utils

def settings_menu():
    running = True
    while running:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("SETTINGS", config.score_font, config.WHITE, config.dis, config.WIDTH/2, 50)
        
        status_text = "Normal"
        if config.MARBLE_SPEED < 1.0: status_text = "Slow"
        elif config.MARBLE_SPEED > 1.0: status_text = "Fast"
        utils.draw_text_centered(f"Speed: {status_text}", config.font_style, config.YELLOW, config.dis, config.WIDTH/2, 120)

        c_easy = config.WHITE if config.MARBLE_SPEED < 1.0 else config.GRAY
        c_norm = config.WHITE if config.MARBLE_SPEED == 1.0 else config.GRAY
        c_hard = config.WHITE if config.MARBLE_SPEED > 1.0 else config.GRAY

        if utils.button("Slow", 50, 160, 80, 40, c_easy, config.WHITE): config.MARBLE_SPEED = 0.5
        if utils.button("Normal", 160, 160, 80, 40, c_norm, config.WHITE): config.MARBLE_SPEED = 1.0
        if utils.button("Fast", 270, 160, 80, 40, c_hard, config.WHITE): config.MARBLE_SPEED = 2.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
        if utils.button("BACK", config.WIDTH/2 - 60, 450, 120, 50, config.RED, (255, 100, 100)): running = False 
        pygame.display.update(); config.clock.tick(60)