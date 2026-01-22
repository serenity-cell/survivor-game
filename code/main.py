from setting import *


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((100,200))
        self.image.fill((200,200,200))
        self.rect = self.image.get_rect(center = ( window_width/2, window_height/2))


#--BASIC SETUP--
pygame.init()
screen = pygame.display.set_mode((window_width , window_height ))
pygame.display.set_caption("shooter survival game - project #2")
running = True


#--IMPORTING--
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)


#--MAIN LOOP--
while running:
     
    #--basics events--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    all_sprites.update()

    screen.fill((0, 180, 70))
    all_sprites.draw(screen)

    pygame.display.update()

