# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 120
TILESIZE = 64

# ui
BAR_HEIGHT = 20
MANA_BAR_WIDTH = 200
HEALTH_BAR_WIDTH = 260
ITEM_BOX_SIZE = 80
UI_FONT = '/Users/sjohal/Desktop/Python/Z-Game/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
MANA_COLOR = 'blue' 
STAMINA_COLOR = 'green'
UI_BORDER_COLOR_ACTIVE = 'gold' 

# weapons
weapon_data = {
  'sword': {'cooldown': 100, 'damage': 20, 'graphic': '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/sword/full.png'},
  'lance': {'cooldown': 400, 'damage': 15, 'graphic': '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/lance/full.png'},
  'axe': {'cooldown': 300, 'damage': 25, 'graphic': '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/axe/full.png'},
  'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/rapier/full.png'},
  'sai': {'cooldown': 80, 'damage': 10, 'graphic': '/Users/sjohal/Desktop/Python/Z-Game/graphics/weapons/sai/full.png'}
}

#spells
spells_data = {
  'flame': {'strength': 5, 'cost': 20, 'graphic': '/Users/sjohal/Desktop/Python/Z-Game/graphics/particles/flame/fire.png'}, 
  'heal': {'strength': 20, 'cost': 10, 'graphic': '/Users/sjohal/Desktop/Python/Z-Game/graphics/particles/heal/heal.png'},
}

#enemies
monster_data = {
  'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': '/Users/sjohal/Desktop/Python/Z-Game/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 75, 'notice_radius': 360},
  'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': '/Users/sjohal/Desktop/Python/Z-Game/audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
  'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': '/Users/sjohal/Desktop/Python/Z-Game/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
  'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': '/Users/sjohal/Desktop/Python/Z-Game/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},  
}