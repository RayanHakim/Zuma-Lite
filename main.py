import pygame
import random
import math
import config
import utils
import setting
import high_score
import keluar

def gameLoop():
    game_over = False
    
    # --- LIST BOLA (MARBLES) ---
    # Format: {'dist': jarak_tempuh, 'color': warna}
    marbles = []
    spawn_timer = 0
    
    # --- PLAYER (SHOOTER) ---
    player_x = config.WIDTH / 2
    player_bullet_color = random.choice(config.COLORS)
    next_bullet_color = random.choice(config.COLORS)
    
    bullets = [] # Peluru yang sedang terbang
    score = 0
    
    # Menghitung panjang total jalur untuk cek Game Over
    total_path_length = 0
    for i in range(len(config.PATH_POINTS)-1):
        total_path_length += utils.distance(config.PATH_POINTS[i], config.PATH_POINTS[i+1])

    while not game_over:
        # 1. INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Tembak!
                    bullets.append({'x': player_x, 'y': config.HEIGHT - 50, 'color': player_bullet_color})
                    player_bullet_color = next_bullet_color
                    next_bullet_color = random.choice(config.COLORS)
                if event.key == pygame.K_ESCAPE:
                    # Pause simpel
                    paused = True
                    while paused:
                        utils.draw_text_centered("PAUSED", config.score_font, config.WHITE, config.dis, config.WIDTH/2, config.HEIGHT/2)
                        pygame.display.update()
                        for e in pygame.event.get():
                            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: paused = False

        # Gerakan Player (Kiri/Kanan)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 20: player_x -= 5
        if keys[pygame.K_RIGHT] and player_x < config.WIDTH - 20: player_x += 5

        # 2. LOGIKA GAME
        
        # Spawn Bola Baru
        spawn_timer += 1
        if spawn_timer > config.SPAWN_RATE:
            marbles.append({'dist': 0, 'color': random.choice(config.COLORS)})
            spawn_timer = 0
            
        # Gerakkan Bola di Jalur
        for m in marbles:
            m['dist'] += config.MARBLE_SPEED
            
        # Cek Game Over (Bola sampai ujung)
        if len(marbles) > 0 and marbles[0]['dist'] >= total_path_length:
            game_over = True

        # Gerakkan Peluru
        for b in bullets:
            b['y'] -= config.BULLET_SPEED
            
        # Hapus peluru yang keluar layar
        bullets = [b for b in bullets if b['y'] > 0]

        # 3. TABRAKAN & LOGIKA ZUMA (Match 3)
        hits = [] # Peluru yang kena
        for b in bullets:
            hit_index = -1
            
            # Cek tabrakan dengan setiap bola di rantai
            for i, m in enumerate(marbles):
                mx, my = utils.get_pos_on_path(m['dist'])
                dist = math.sqrt((mx - b['x'])**2 + (my - b['y'])**2)
                
                if dist < config.MARBLE_RADIUS * 2:
                    hit_index = i
                    break
            
            if hit_index != -1:
                # SISIPKAN BOLA (INSERT)
                new_marble = {'dist': marbles[hit_index]['dist'] - config.MARBLE_RADIUS*2, 'color': b['color']}
                
                # Masukkan ke dalam list di posisi yang tepat
                marbles.insert(hit_index + 1, new_marble)
                
                # Geser bola di belakangnya mundur sedikit agar tidak tumpang tindih
                for j in range(hit_index + 1, len(marbles)):
                    marbles[j]['dist'] -= config.MARBLE_RADIUS * 2
                
                hits.append(b) # Tandai peluru untuk dihapus
                
                # CEK MATCH 3 (Logika Penghancuran)
                # Cek ke kiri dan kanan dari posisi hit_index+1
                target_idx = hit_index + 1
                target_color = marbles[target_idx]['color']
                
                # Cari batas kiri
                left = target_idx
                while left > 0 and marbles[left-1]['color'] == target_color:
                    left -= 1
                
                # Cari batas kanan
                right = target_idx
                while right < len(marbles)-1 and marbles[right+1]['color'] == target_color:
                    right += 1
                
                # Hitung jumlah bola yang sama
                count = right - left + 1
                
                if count >= 3:
                    score += count * 10
                    # Hapus bola dari list (del slice)
                    del marbles[left : right+1]

        # Hapus peluru yang sudah menabrak
        for h in hits:
            if h in bullets: bullets.remove(h)

        # 4. GAMBAR (RENDER)
        config.dis.fill(config.BLACK)
        
        # Gambar Jalur (Garis Tipis)
        pygame.draw.lines(config.dis, config.GRAY, False, config.PATH_POINTS, 2)
        
        # Gambar Lubang Game Over
        end_x, end_y = config.PATH_POINTS[-1]
        pygame.draw.circle(config.dis, config.WHITE, (end_x, end_y), 20)
        utils.draw_text_centered("X", config.font_style, config.BLACK, config.dis, end_x, end_y)

        # Gambar Bola Rantai
        for m in marbles:
            mx, my = utils.get_pos_on_path(m['dist'])
            pygame.draw.circle(config.dis, m['color'], (mx, my), config.MARBLE_RADIUS)
            # Kilauan (biar kayak kelereng)
            pygame.draw.circle(config.dis, config.WHITE, (mx-5, my-5), 3)

        # Gambar Player (Shooter)
        pygame.draw.rect(config.dis, config.GRAY, (player_x - 20, config.HEIGHT - 40, 40, 40))
        pygame.draw.circle(config.dis, player_bullet_color, (int(player_x), config.HEIGHT - 20), config.MARBLE_RADIUS)
        
        # Indicator Next Color (Kecil di pojok)
        utils.draw_text_centered("Next:", config.info_font, config.WHITE, config.dis, 40, config.HEIGHT - 30)
        pygame.draw.circle(config.dis, next_bullet_color, (80, config.HEIGHT - 30), 10)

        # Gambar Peluru Terbang
        for b in bullets:
            pygame.draw.circle(config.dis, b['color'], (int(b['x']), int(b['y'])), config.MARBLE_RADIUS)

        utils.show_score(score)
        pygame.display.update()
        config.clock.tick(config.FPS)

    action = keluar.game_over_menu(score)
    return action

def main_menu():
    while True:
        config.dis.fill(config.BLACK)
        utils.draw_text_centered("ZUMA LITE", config.score_font, config.YELLOW, config.dis, config.WIDTH/2, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); quit()

        if utils.button("PLAY", config.WIDTH/2 - 60, 250, 120, 50, config.GREEN, (100, 255, 100)):
            game_action = 'restart'
            while game_action == 'restart': game_action = gameLoop() 
        if utils.button("HIGHSCORE", config.WIDTH/2 - 60, 320, 120, 50, config.YELLOW, config.WHITE): high_score.high_score_menu()
        if utils.button("SETTING", config.WIDTH/2 - 60, 390, 120, 50, config.GRAY, config.WHITE): setting.settings_menu()
        if utils.button("EXIT", config.WIDTH/2 - 60, 460, 120, 50, config.RED, (255, 100, 100)): pygame.quit(); quit()

        pygame.display.update()
        config.clock.tick(60)

if __name__ == "__main__":
    try:
        high_score.load_data() 
        main_menu()
    except Exception as e:
        print(f"Error: {e}")
        pygame.quit()