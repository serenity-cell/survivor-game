from setting import *

#--SPRITE CLASSES-- 
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((100,200))
        self.image.fill((200,200,200))
        self.rect = self.image.get_rect(center = ( window_width/2, window_height/2))
    
    def update(self):
        pass

class Gun(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = (0,0))
    
    def update(self):
        pass


#--BASIC SETUP--
pygame.init()
screen = pygame.display.set_mode((window_width , window_height ))
pygame.display.set_caption("shooter survival")
running = True
clock = pygame.Clock()


#--IMPORTING--

#remember to change the gun_surf to the actual picture and delete color fill
gun_surf = pygame.Surface((400, 200))
gun_surf.fill((100,100,100))

all_sprites = pygame.sprite.Group()
gun = Gun(all_sprites, gun_surf)
player = Player(all_sprites)


#--MAIN LOOP--
while running:
    dt = clock.tick(60) / 1000

    #--BASIC EVENT--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    all_sprites.update()

    screen.fill((0, 180, 70))
    all_sprites.draw(screen)

    pygame.display.update()

