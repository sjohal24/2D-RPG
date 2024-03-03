import pygame
from debug import debug

class Weapon(pygame.sprite.Sprite):
  def __init__(self, player, groups):
    super().__init__(groups)
    self.sprite_type = 'weapon'
    direction = player.status.split('_')[0]

    full_path = f'/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/{player.weapon}/{direction}.png'
    self.image = pygame.image.load(full_path).convert_alpha()
    
    if direction == 'right':
      self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-26,6))
    elif direction == 'left':
      self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(8,6))
    elif direction == 'up':
      self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-16,12))
    elif direction == 'down':
      self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-18,-26))
    
    else:
      self.rect = self.image.get_rect(center = player.rect.center)
  
  
  
    