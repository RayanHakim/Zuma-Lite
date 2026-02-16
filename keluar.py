import pygame
import config
import utils
import high_score 

def game_over_menu(score):
    if high_score.check_is_high_score(score) and score > 0:
        high_score.input_name_menu(score)
    while True:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("GAME OVER", config.score_font, config.RED, config.dis, config.WIDTH/2, 150)
        utils.draw_text_centered(f"Score: {score}", config.font_style, config.WHITE, config.dis, config.WIDTH/2, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
        if utils.button("RETRY", config.WIDTH/2 - 70, 300, 140, 50, config.GREEN, (100, 255, 100)): return 'restart'
        if utils.button("MENU", config.WIDTH/2 - 70, 370, 140, 50, config.GRAY, config.WHITE): return 'menu'
        if utils.button("EXIT", config.WIDTH/2 - 70, 440, 140, 50, config.RED, (255, 100, 100)): pygame.quit(); quit()
        pygame.display.update(); config.clock.tick(60)