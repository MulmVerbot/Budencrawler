import pygame
import random
import sys

# Konstanten
SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 720
TILE_SIZE = 40
PLAYER_SPEED = 5
ENEMY_SPEED = 2

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
GREEN = (50, 200, 50)

# Setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Dungeon Crawler")
clock = pygame.time.Clock()

# Klassen
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hp = 100

    def update(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_w]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.rect.y += PLAYER_SPEED

        # Begrenzung auf Bildschirm
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - TILE_SIZE))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - TILE_SIZE))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hp = 30

    def update(self, player):
        # Richtung auf Spieler zu
        if self.rect.x < player.rect.x:
            self.rect.x += ENEMY_SPEED
        if self.rect.x > player.rect.x:
            self.rect.x -= ENEMY_SPEED
        if self.rect.y < player.rect.y:
            self.rect.y += ENEMY_SPEED
        if self.rect.y > player.rect.y:
            self.rect.y -= ENEMY_SPEED

# Funktionen
def spawn_enemy():
    x = (random.randint(0, SCREEN_WIDTH // TILE_SIZE - 1) * TILE_SIZE) + 10
    y = (random.randint(0, SCREEN_HEIGHT // TILE_SIZE - 1) * TILE_SIZE) - 10
    return Enemy(x, y)

def draw_health_bar(surface, x, y, hp, max_hp):
    bar_width = 100
    bar_height = 10
    fill = (hp / max_hp) * bar_width
    border = pygame.Rect(x, y, bar_width, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surface, RED, fill_rect)
    pygame.draw.rect(surface, WHITE, border, 2)

# Hauptprogramm
def main():
    player = Player(100, 100)
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    for _ in range(10):
        enemy = spawn_enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    running = True
    while running:
        clock.tick(30)  # FPS
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(keys)

        for enemy in enemies:
            enemy.update(player)

        # Kollision überprüfen
        hits = pygame.sprite.spritecollide(player, enemies, False)
        for hit in hits:
            player.hp -= 1
            if player.hp <= 0:
                print("Game Over!")
                running = False

        # Zeichnen
        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_health_bar(screen, 10, 10, player.hp, 100)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
