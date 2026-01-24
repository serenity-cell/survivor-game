from setting import *
from player import Player
from sprites import Collision_sprite
from random import randint
class Game:
    def __init__(self):
        #--BASIC SETUP--
        pygame.init()
        self.screen = pygame.display.set_mode((window_width , window_height))
        pygame.display.set_caption("shooter survival")
        self.clock = pygame.time.Clock()
        self.running = True

        #--GROUPS--
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprite = pygame.sprite.Group()

        #--SPRITES--
        for i in range(8):
            pos_x, pos_y = randint(0,window_width),randint(0, window_height)
            width, height = randint(100, 200), randint(100, 200)
            self.collision = Collision_sprite((self.all_sprites, self.collision_sprite), (pos_x, pos_y), (width, height))
        self.player = Player(self.all_sprites, self.collision_sprite, (400, 200))

    def run(self):
        #--MAIN LOOP--
        while self.running:
            dt = self.clock.tick(40) / 1000

            #--BASIC EVENT--
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
            #--UPDATE--
            self.all_sprites.update(dt)

            #--DRAW-
            self.screen.fill((0, 180, 70))
            self.all_sprites.draw(self.screen)

            pygame.display.update()


        pygame.quit

    """def imports(self):
        #remember to change the gun_surf to the actual picture and delete color fill
        gun_surf = pygame.Surface((400, 200))
        gun_surf.fill((100,100,100))

        self.all_sprites = pygame.sprite.Group()
        self.gun = Gun(self.all_sprites, gun_surf)
        player = Player(self.all_sprites)"""

        
#--SPRITE CLASSES-- 

class Gun(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = (0,0))
    
    def update(self, dt):
        pass

if __name__ == "__main__":
    game = Game()
    game.run()