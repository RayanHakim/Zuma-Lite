import pygame
import json
import os
import config
import utils

DATA_FILE = "zuma_highscore.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        default_data = [] 
        with open(DATA_FILE, "w") as f: json.dump(default_data, f)
        return default_data
    try:
        with open(DATA_FILE, "r") as f: return json.load(f)
    except: return []

def save_data(data):
    with open(DATA_FILE, "w") as f: json.dump(data, f)

def add_high_score(name, score):
    data = load_data()
    data.append({"name": name, "score": score})
    data.sort(key=lambda x: x["score"], reverse=True)
    data = data[:5]
    save_data(data)

def check_is_high_score(score):
    data = load_data()
    if len(data) < 5: return True
    if score > data[-1]["score"]: return True
    return False

def input_name_menu(score):
    input_active = True
    user_text = ''
    while input_active:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("NEW HIGH SCORE!", config.score_font, config.YELLOW, config.dis, config.WIDTH/2, 100)
        utils.draw_text_centered(f"Score: {score}", config.font_style, config.WHITE, config.dis, config.WIDTH/2, 150)
        utils.draw_text_centered("Input Name:", config.font_style, config.WHITE, config.dis, config.WIDTH/2, 200)
        pygame.draw.rect(config.dis, config.WHITE, [config.WIDTH/2 - 100, 230, 200, 40], 2)
        text_surf = config.input_font.render(user_text, True, config.YELLOW)
        config.dis.blit(text_surf, text_surf.get_rect(center=(config.WIDTH/2, 250)))
        utils.draw_text_centered("(Press ENTER)", config.info_font, config.GRAY, config.dis, config.WIDTH/2, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(user_text) > 0: add_high_score(user_text, score); input_active = False 
                elif event.key == pygame.K_BACKSPACE: user_text = user_text[:-1]
                else: 
                    if len(user_text) < 10: user_text += event.unicode
        pygame.display.update(); config.clock.tick(30)

def high_score_menu():
    hs_running = True
    while hs_running:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("TOP 5 SCORES", config.score_font, config.WHITE, config.dis, config.WIDTH/2, 80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
        data = load_data()
        if not data: utils.draw_text_centered("- No Data -", config.font_style, config.GRAY, config.dis, config.WIDTH/2, 250)
        else:
            for i, entry in enumerate(data):
                text = f"{i+1}. {entry['name']} : {entry['score']}"
                utils.draw_text_centered(text, config.font_style, config.WHITE, config.dis, config.WIDTH/2, 180 + (i * 40))
        if utils.button("RESET", config.WIDTH/2 - 60, config.HEIGHT - 170, 120, 50, config.RED, config.WHITE):
            if os.path.exists(DATA_FILE): os.remove(DATA_FILE)
        if utils.button("BACK", config.WIDTH/2 - 60, config.HEIGHT - 100, 120, 50, config.BLUE, config.WHITE): hs_running = False
        pygame.display.update(); config.clock.tick(60)