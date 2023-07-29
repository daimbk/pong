# player class module
class Player:
    def __init__(self):
        self.player_x = 0
        self.player_y = 0

    def set_x(self, x):
        self.player_x = x

    def set_y(self, y):
        self.player_y = y

    def get_x(self):
        return self.player_x
    
    def get_y(self):
        return self.player_y
    