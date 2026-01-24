from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.Surface((100,200))
        self.image.fill((200,200,200))
        self.rect: pygame.FRect =  self.image.get_frect(center = pos)

        #--MOVEMENT BASE--
        self.direction = pygame.math.Vector2()
        self.speed = 400
    
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a]) 
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.move(dt)