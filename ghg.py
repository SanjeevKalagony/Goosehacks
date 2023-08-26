import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLIMATE SHOOTOUT 1 V 1")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
FPS = 60 
VEL = 5
BVEL = 7
MAX_BULLETS = 3
GUY_HIT = pygame.USEREVENT + 1
CO2_HIT = pygame.USEREVENT + 2

GUY_IMAGE = pygame.image.load(os.path.join('guy.png'))
GUY_IMAGE = pygame.transform.scale(GUY_IMAGE, (55, 60))
CO2_IMAGE = pygame.image.load(os.path.join('co2.png'))
CO2_IMAGE = pygame.transform.scale(CO2_IMAGE, (55, 60))
LAND = pygame.image.load(os.path.join('background.png'))

def draw_window(guy, co2, guy_bullets, CO2_HEALTH):
    WIN.fill(WHITE)
    WIN.blit(LAND, (0, 0))

    CO2_HEALTH = HEALTH_FONT.render("Health: " + str(CO2_HEALTH), 1, BLACK)
    WIN.blit(CO2_HEALTH, (WIDTH - CO2_HEALTH.get_width() - 10, 10))
    WIN.blit(GUY_IMAGE, (guy.x, guy.y))
    WIN.blit(CO2_IMAGE, (co2.x, co2.y))


    for bullet in guy_bullets:
        pygame.draw.rect(WIN, RED, bullet)  

    pygame.display.update()

def guy_movement(keys_pressed, guy):
    if keys_pressed[pygame.K_a] and guy.x - VEL > 0: # LEFT
        guy.x -= VEL
    if keys_pressed[pygame.K_d] and guy.x + VEL + guy.width < 900: # RIGHT
        guy.x += VEL
    if keys_pressed[pygame.K_w] and guy.x - VEL > 0 + 50: # UP
        guy.y -= VEL
    if keys_pressed[pygame.K_s] and guy.x + VEL + guy.height < 500 - 50: # DOWN
        guy.y += VEL

def co2_movement(keys_pressed, co2):
    if keys_pressed[pygame.K_LEFT] and co2.x - VEL > 0: # LEFT
        co2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and co2.x + VEL + co2.width < 900: # RIGHT
        co2.x += VEL
    if keys_pressed[pygame.K_UP] and co2.x - VEL > 0 + 50: # UP
        co2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and co2.x + VEL + co2.height < 500 - 50: # DOWN
        co2.y += VEL

def handle_bullets(guy_bullets, guy, co2):
    for bullet in guy_bullets:
        bullet.x += BVEL
        if guy.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CO2_HIT))
            guy_bullets.remove(bullet)
def main():
    guy = pygame.Rect(100, 300, 55, 60)
    co2 = pygame.Rect(700, 300, 100, 100)

    guy_bullets = []

    CO2_HEALTH = 1

    clock = pygame.time.Clock()
    # keeps window open
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g and len(guy_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(guy.x + guy.width, guy.y + guy.height//2 - 2, 10, 5)
                guy_bullets.append(bullet)

            if event.type == CO2_HIT:
                CO2_HEALTH -= 1

        if CO2_HEALTH <=0:
            winner_text = "PLAYER WINS!"
        
        else:
            winner_text = "CO2 WINS ._."

        if winner_text != "":
            pass

        keys_pressed = pygame.key.get_pressed()
        guy_movement(keys_pressed, guy)
        co2_movement(keys_pressed, co2)

        handle_bullets(guy_bullets, guy, co2)
        draw_window(guy, co2, guy_bullets, CO2_HEALTH)

    pygame.quit()


if __name__ == "__main__":
    main()