class Settings:
    '''A class to store all of the settings for Alien Invasion'''

    def __init__(self):
        '''Initialise the game's settings.'''
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        #Ship settings.
        self.ship_limit = 3

        #Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60,) * 3
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 7

        #How quickly the game speeds up.
        self.speedup_scale = 1.1
        #The multiplier at which alien point values increase.
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        '''Initialise settings that change throughout the game.'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.5

        #Fleet direction 1 = right, -1 represents left.
        self.fleet_direction = 1

        #Scoring.
        self.alien_points = 50

    def increase_speed(self):
        '''Increase speed settings and alien point values.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)