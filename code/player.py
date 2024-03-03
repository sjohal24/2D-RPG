import pygame
from settings import *
from pygame_functions import *
from support import import_folder
from debug import debug
from entity import Entity

class Player(Entity):
  def __init__(self, position, groups, obstacle_sprites, create_attack, end_attack, create_spell, end_spell):
    super().__init__(groups)
    sprite_sheet = pygame.image.load('/Users/sjohal/Desktop/Python/Z-Game/graphics/output.gif').convert_alpha()
    frame_rect = pygame.Rect(0, 0, 32, 60)
    self.image = sprite_sheet.subsurface(frame_rect)
    self.rect = self.image.get_rect(topleft = position)
    self.hitbox = self.rect.inflate(0, -26)
    
    self.import_player_assets()
    self.status = 'down'
    
    self.direction = pygame.math.Vector2()
    self.attacking = False
    self.attack_cooldown = 400
    self.attack_time = None
    self.obstacle_sprites = obstacle_sprites
    
    self.create_attack = create_attack
    self.end_attack = end_attack
    self.weapon_index = 0
    self.weapon = list(weapon_data.keys())[self.weapon_index]
    self.can_switch_weapon = True
    self.weapon_switch_time = None
    self.switch_duration_cooldown = 200
    
    self.create_spell = create_spell
    self.end_spell = end_spell
    self.spell_index = 0
    self.spell = list(spells_data.keys())[self.spell_index]
    self.can_switch_spell = True
    self.spell_switch_time = None
    
    self.stats = {
      'health': 100,
      'mana': 60,
      'attack': 10,
      'magic': 4,
      'speed': 5,
      'stamina': 100
    }
    self.health = self.stats['health']
    self.mana = self.stats['mana']
    self.exp = 120
    self.speed = self.stats['speed']
    self.stamina = self.stats['stamina']
    
    self.vulnerable = True
    self.hurt_time = None
    self.invulerability_duration = 500

  def import_player_assets(self):
    character_path = '/Users/sjohal/Desktop/Python/Z-Game/graphics/link'
    self.animations = {'up': [], 'down': [], 'left': [], 'right': []
                       , 'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [], 
                       'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}
    
    for animation in self.animations.keys():
      full_path = character_path + '/' + animation
      self.animations[animation] = import_folder(full_path)
        
  def input(self):
     
     if not self.attacking: 
      keys = pygame.key.get_pressed()
      
      if keys[pygame.K_UP]:
        self.direction.y = -1
        self.status = 'up'
        
      elif keys[pygame.K_DOWN]:
        self.direction.y = 1
        self.status = 'down'
        
      else:
        self.direction.y = 0
        
      if keys[pygame.K_LEFT]:
        self.direction.x = -1
        self.status = 'left'
        
      elif keys[pygame.K_RIGHT]:
        self.direction.x = 1
        self.status = 'right'
        
      else:
        self.direction.x = 0
        
      if keys[pygame.K_q]:
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()
        self.create_attack()
      
      if keys[pygame.K_w] and self.can_switch_spell:
        self.attacking = True
        self.attack_time = pygame.time.get_ticks()
        style = list(spells_data.keys())[self.spell_index]
        strength = list(spells_data.values())[self.spell_index]['strength'] + self.stats['magic']
        cost = list(spells_data.values())[self.spell_index]['cost']
        self.create_spell(style, strength, cost)
        
      if keys[pygame.K_e] and self.can_switch_weapon:
        self.can_switch_weapon = False
        self.weapon_switch_time = pygame.time.get_ticks()
        if self.weapon_index+1 < len(weapon_data.keys()):
          self.weapon_index += 1
        else :
          self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
      
      if keys[pygame.K_r] and self.can_switch_spell:
        self.can_switch_spell = False
        self.spell_switch_time = pygame.time.get_ticks()
        
        if self.spell_index+1 < len(spells_data.keys()):
          self.spell_index += 1
        else :
          self.spell_index = 0
        self.spell = list(spells_data.keys())[self.spell_index]
      
      if keys[pygame.K_1] and self.can_switch_weapon:
        self.can_switch_weapon = False
        self.weapon_switch_time = pygame.time.get_ticks()
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]

      if keys[pygame.K_2] and self.can_switch_weapon:
        self.can_switch_weapon = False
        self.weapon_switch_time = pygame.time.get_ticks()
        self.weapon_index = 1
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        
      if keys[pygame.K_3] and self.can_switch_weapon:
        self.can_switch_weapon = False
        self.weapon_switch_time = pygame.time.get_ticks()
        self.weapon_index = 2
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        
      if keys[pygame.K_4] and self.can_switch_weapon:
        self.can_switch_weapon = False
        self.weapon_switch_time = pygame.time.get_ticks()
        self.weapon_index = 3
        self.weapon = list(weapon_data.keys())[self.weapon_index]

      if keys[pygame.K_5] and self.can_switch_weapon:
        self.can_switch_weapon = False
        self.weapon_switch_time = pygame.time.get_ticks()
        self.weapon_index = 4
        self.weapon = list(weapon_data.keys())[self.weapon_index]
    
  def cooldowns(self):
    current_time = pygame.time.get_ticks()
    if self.attacking:
      if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown'] :
        self.attacking = False
        self.end_attack()
        
    if not self.can_switch_weapon:
      if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
        self.can_switch_weapon = True

    if not self.can_switch_spell:
      if current_time - self.spell_switch_time >= self.switch_duration_cooldown:
        self.can_switch_spell = True   
        
    if not self.vulnerable:
      if current_time - self.hurt_time >= self.invulerability_duration:
        self.vulnerable = True
        
  def get_status(self):
    if self.direction.x == 0 and self.direction.y == 0:
      if not 'idle' in self.status and not 'attack' in self.status:
        self.status = self.status + '_idle'
    if self.attacking:
      self.direction.x = 0
      self.direction.y = 0
      if not 'attack' in self.status:
        if 'idle' in self.status:
          self.status = self.status.replace('idle', 'attack')
        else:  
          self.status = self.status + '_attack'
    else:
      if 'attack' in self.status:
        self.status = self.status.replace('_attack', '')
        
  def animate(self):
    animation = self.animations[self.status]
    
    self.frame_index += self.animation_speed
    if self.frame_index >= len(animation):
      self.frame_index = 0
      
    self.image = animation[int(self.frame_index)]
    self.rect = self.image.get_rect(center = self.hitbox.center)
    
    if not self.vulnerable:
      alpha = self.wave_value()
      self.image.set_alpha(alpha)
    else:
      self.image.set_alpha(255)
  
  def get_full_weapon_damage(self):
    base_damage = self.stats['attack']
    weapon_damage = weapon_data[self.weapon]['damage']
    return base_damage + weapon_damage
  
  def update(self):
    self.input()
    self.cooldowns()
    self.get_status()
    self.animate()
    self.move(self.speed)