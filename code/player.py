from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, collision_sprite, pos):
        super().__init__(groups)
        self.image = pygame.Surface((100,200))
        self.image.fill((200,200,200))
        self.rect: pygame.FRect =  self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-40, 0)
        

        #--MOVEMENT BASE--
        self.direction = pygame.math.Vector2()
        self.speed = 600
        self.collision_sprites = collision_sprite
    
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a]) 
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.hitbox.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.hitbox.y+= self.direction.y * self.speed * dt
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox):
                if direction == "horizontal":
                    if self.direction.x > 0: 
                        self.hitbox.right = sprite.rect.left
                    if self.direction.x < 0: 
                        self.hitbox.left = sprite.rect.right
                if direction == "vertical":
                    if self.direction.y > 0: 
                        self.hitbox.bottom = sprite.rect.top
                    if self.direction.y < 0: 
                        self.hitbox.top = sprite.rect.bottom

    def update(self, dt):
        self.input()
        self.move(dt)