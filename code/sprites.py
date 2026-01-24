from setting import * 

class Collision_sprite(pygame.sprite.Sprite):
    def __init__(self, groups, pos, size):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_frect(center = pos)