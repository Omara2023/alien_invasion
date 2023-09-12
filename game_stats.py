class GameStats():
    '''Track the statistics for Alien Invasion.'''

    def __init__(self, ai_settings):
        '''Initialise settigns.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien Invasion in an non-active state.
        self.game_active = False
        #High score should be persistent.
        self.high_score = 0

    def reset_stats(self):
        '''Initialise statistics that can change during the game.'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1