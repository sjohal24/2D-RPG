import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
  def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player, trigger_death_particles):
    
    super().__init__(groups)
    self.sprite_type = 'enemy'
    
    self.import_graphics(monster_name)
    self.status = 'idle'
    self.image = self.animations[self.status][self.frame_index]
    
    self.rect = self.image.get_rect(topleft = pos)
    self.hitbox = self.rect.inflate(0, -10)
    self.obstacle_sprites = obstacle_sprites
    
    self.monster_name = monster_name
    monster_info = monster_data[self.monster_name]
    self.health = monster_info['health']
    self.exp = monster_info['exp']
    self.speed = monster_info['speed']
    self.attack_damage = monster_info['damage']
    self.resistance = monster_info['resistance']
    self.attack_radius = monster_info['attack_radius']
    self.notice_radius = monster_info['notice_radius']
    self.attack_type = monster_info['attack_type']
    
    self.can_attack = True
    self.attack_time = None
    self.attack_cooldown = 400
    self.damage_player = damage_player
    self.trigger_death = trigger_death_particles
    
    self.vulnerable = True
    self.hit_time = None
    self.invinciblility_duration = 550
    
  def import_graphics(self, name):
    self.animations = {'idle': [], 'move':[], 'attack':[]}
    main_path = f'/Users/sjohal/Desktop/Python/Z-Game/graphics/monsters/{name}/'
    for animation in self.animations.keys():
      self.animations[animation] = import_folder(main_path + animation)
  
  def get_player_distance_direction(self, player):
    enemy_vector = pygame.math.Vector2(self.rect.center)
    player_vector = pygame.math.Vector2(player.rect.center)
    distance = (player_vector - enemy_vector).magnitude()
    if distance > 0:
     direction = (player_vector - enemy_vector).normalize()
    else:
      direction = pygame.math.Vector2()
    
    return (distance, direction)
    
  def get_statuses(self, player):
    distance = self.get_player_distance_direction(player)[0]
    if distance <= self.attack_radius and self.can_attack:
      if self.status != "attack":
        self.frame_index = 0
      self.status = 'attack'
      
    elif distance <= self.notice_radius:
      self.status = 'move'
    else: self.status = 'idle'
    
  def animate(self):
    animation = self.animations[self.status]
    
    self.frame_index += self.animation_speed
    if self.frame_index >= len(animation):
      if self.status == 'attack':
        self.can_attack = False
      self.frame_index = 0
      
    self.image = animation[int(self.frame_index)]
    self.rect = self.image.get_rect(center = self.hitbox.center)
    
    if not self.vulnerable:
      alpha = self.wave_value()
      self.image.set_alpha(alpha)
    else:
      self.image.set_alpha(255)
    
  def actions(self, player):
    if self.status == 'attack':
      self.damage_player(self.attack_damage, self.attack_type)
      self.attack_time = pygame.time.get_ticks()
    elif self.status == 'move':
      self.direction = self.get_player_distance_direction(player)[1]
    else: pygame.math.Vector2()
  
  def cooldowns(self):      
    current_time = pygame.time.get_ticks()
    if not self.can_attack: 
      if current_time - self.attack_time >= self.attack_cooldown:
        self.can_attack = True
    
    if not self.vulnerable:
      if current_time - self.hit_time >= self.invinciblility_duration:
        self.vulnerable = True
        
  def get_damage(self,player,attack_type):
    if self.vulnerable:
      self.direction = self.get_player_distance_direction(player)[1]
      if attack_type == 'weapon':
        self.health -= player.get_full_weapon_damage()
      else:
        pass
				# magic damage 
      self.hit_time = pygame.time.get_ticks()
      self.vulnerable = False
        
  def check_death(self):
    if self.health <= 0:
      self.kill()
      self.trigger_death(self.rect.center, self.monster_name)
      
  def hit_recoil(self):
    if not self.vulnerable:
      self.direction *= -self.resistance
  
  def update(self):
    self.hit_recoil()
    self.move(self.speed)
    self.animate()
    self.cooldowns()
    self.check_death()
      
  def enemy_update(self, player):
    self.get_statuses(player)
    self.actions(player)