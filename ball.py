# ball settings module
class Ball:
    def __init__(self):
        self.ball_radius = 5
        self.ball_x = 0
        self.ball_y = 0
        self.ball_dx = 0
        self.ball_dy = 0
        self.ball_speed = 0

    def set_radius(self, radius):
        self.ball_radius = radius

    def set_x(self, x):
        self.ball_x = x

    def set_y(self, y):
        self.ball_y = y

    def set_dx(self, dx):
        self.ball_dx = dx

    def set_dy(self, dy):
        self.ball_dy = dy

    def set_speed(self, speed):
        self.ball_speed = speed

    def get_radius(self):
        return self.ball_radius
    
    def get_x(self):
        return self.ball_x
    
    def get_y(self):
        return self.ball_y
    
    def get_dx(self):
        return self.ball_dx
    
    def get_dy(self):
        return self.ball_dy
    
    def get_speed(self):
        return self.ball_speed