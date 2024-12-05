import pygame 
import random 
pygame.init()
SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 600 
PLAYER_WIDTH = 50 
PLAYER_HEIGHT = 40 
ASTEROID_WIDTH = 50 
ASTEROID_HEIGHT = 50 
PLAYER_SPEED = 5 
ASTEROID_SPEED = 5
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
RED = (255, 0, 0) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Retro Arcade Game') 
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill(WHITE) 
player_rect = player_img.get_rect() 
player_rect.centerx = SCREEN_WIDTH // 2 
player_rect.bottom = SCREEN_HEIGHT - 10 
asteroids = []
running = True
clock = pygame.time.Clock()
game_over = False
font = pygame.font.SysFont('Arial', 30)

def draw_text(text, x, y, color):

 
    text_surface = font.render(text, True, color) 
     
    screen.blit(text_surface, (x, y)) 

def create_asteroid():
    
     
    x = random.randint(0, SCREEN_WIDTH - ASTEROID_WIDTH) 
      
    asteroid_rect = pygame.Rect(x, -ASTEROID_HEIGHT, ASTEROID_WIDTH, ASTEROID_HEIGHT)
     
    return asteroid_rect 

def handle_collisions():
    global game_over 
      
    for asteroid in asteroids:
         
        if player_rect.colliderect(asteroid): 
            
            game_over = True  
             
            break 

while running:
    
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT: 
            
            running = False  

     
    keys = pygame.key.get_pressed() 
     
    if keys[pygame.K_LEFT] and player_rect.left > 0: 
         
        player_rect.x -= PLAYER_SPEED 
         
    if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH: 
         
        player_rect.x += PLAYER_SPEED 

     
    if random.random() < 0.02: 
        
        asteroids.append(create_asteroid())  

    for asteroid in asteroids: 
        
        asteroid.y += ASTEROID_SPEED  
         
        if asteroid.y > SCREEN_HEIGHT: 
             
            asteroids.remove(asteroid) 
    
     
    if not game_over: 
         
        handle_collisions() 

    screen.fill(BLACK)
    
    screen.blit(player_img, player_rect)
    
    for asteroid in asteroids:
        pygame.draw.rect(screen, RED, asteroid)  
    
    if game_over:
        
        draw_text("GAME OVER", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30, WHITE)  
        
        draw_text("Press R to Restart", SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 10, WHITE)  
         
        pygame.display.update() 
         
        continue 
    
    draw_text(f'Asteroids Avoided: {len(asteroids)}', 10, 10, WHITE)
    
    pygame.display.update()
    
    clock.tick(60)
    
    if game_over:
        
        keys = pygame.key.get_pressed()  
         
        if keys[pygame.K_r]: 
            
            game_over = False  
            
            player_rect.centerx = SCREEN_WIDTH // 2  
            
            player_rect.bottom = SCREEN_HEIGHT - 10  
             
            asteroids.clear() 

pygame.quit()
