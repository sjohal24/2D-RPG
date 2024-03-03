import pygame
from settings import *

class UI:
  def __init__(self):
    
    self.display_surface = pygame.display.get_surface()
    self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
    
    self.health_bar_rect = pygame.Rect(10, 10 , HEALTH_BAR_WIDTH, BAR_HEIGHT)
    self.mana_bar_rect = pygame.Rect(10, 34, MANA_BAR_WIDTH, BAR_HEIGHT)
    self.stamina_bar_rect = pygame.Rect(10, 58 , MANA_BAR_WIDTH, BAR_HEIGHT)

    self.weapon_graphics = []
    for weapon in weapon_data.values():
      path = weapon['graphic']
      weapon = pygame.image.load(path).convert_alpha()
      self.weapon_graphics.append(weapon)
    
    self.spell_graphics = []
    for spell in spells_data.values():
      path = spell['graphic']
      spell = pygame.image.load(path).convert_alpha()
      self.spell_graphics.append(spell)
  
  def show_bar(self, current_amount, max_amount, bg_rect, color):
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
    
    ratio = current_amount / max_amount
    current_width = ratio * bg_rect.width
    current_rect = bg_rect.copy()
    current_rect.width = current_width
    
    pygame.draw.rect(self.display_surface, color, current_rect)
    pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)


  def show_exp(self, exp):
    text_surface = self.font.render(str(int(exp)), False, TEXT_COLOR)
    x = self.display_surface.get_size()[0] - 20
    y = self.display_surface.get_size()[1] - 20
    text_rect = text_surface.get_rect(bottomright = (x,y))
    
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20,20))
    self.display_surface.blit(text_surface, text_rect)
    pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20,20), 3)
    
  def selection_box(self, left, top, has_switched):
    bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
    pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
    if has_switched:
      pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
    else:
      pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
    return bg_rect
  
  def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 630, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)        
        self.display_surface.blit(weapon_surf, weapon_rect)
        
  def spell_overlay(self, spell_index, has_switched):
        bg_rect = self.selection_box(87, 635, has_switched)
        spell_surf = self.spell_graphics[spell_index]
        spell_rect = spell_surf.get_rect(center = bg_rect.center)        
        self.display_surface.blit(spell_surf, spell_rect)
  
  def display(self, player):
    self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
    self.show_bar(player.mana, player.stats['mana'], self.mana_bar_rect, MANA_COLOR)
    self.show_bar(player.stamina, player.stats['stamina'], self.stamina_bar_rect, STAMINA_COLOR)
    
    self.show_exp(player.exp)
    self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
    self.spell_overlay(player.spell_index, not player.can_switch_spell)