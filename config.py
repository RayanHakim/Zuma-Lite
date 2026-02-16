import pygame

pygame.init()

# --- Warna Bola ---
RED = (255, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 255)
YELLOW = (255, 220, 0)
PURPLE = (160, 32, 240)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

COLORS = [RED, GREEN, BLUE, YELLOW] # Warna yang muncul

# --- Ukuran Layar ---
WIDTH = 500  
HEIGHT = 600

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zuma Lite')

clock = pygame.time.Clock()
FPS = 60

# --- PENGATURAN GAME ---
MARBLE_RADIUS = 15
MARBLE_SPEED = 1.0     # Kecepatan gerak barisan bola
BULLET_SPEED = 10      # Kecepatan tembakan
SPAWN_RATE = 40        # Jarak antar bola (dalam frame)

# --- DEFINISI JALUR (PATH) ---

PATH_POINTS = [
    (-20, 50),   (450, 50),  # Kiri ke Kanan
    (450, 150),  (50, 150),  # Turun, lalu Kanan ke Kiri
    (50, 250),   (450, 250), # Turun, lalu Kiri ke Kanan
    (450, 350),  (50, 350),  # Turun, lalu Kanan ke Kiri
    (50, 450),   (250, 450), # Turun, lalu ke Tengah (Game Over)
    (250, 600)               # Lubang Game Over
]

# --- UI Fonts ---
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 40)
button_font = pygame.font.SysFont("comicsansms", 20)
info_font = pygame.font.SysFont("comicsansms", 15)
input_font = pygame.font.SysFont("comicsansms", 30)