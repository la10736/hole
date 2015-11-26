import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock


__version__ = "1.0"


class Ball(Widget):
    velocity_x = NumericProperty(5)
    velocity_y = NumericProperty(2)

    def move(self):
        self.pos = Vector(self.velocity_x, self.velocity_y) + self.pos


class Hole(Widget):
    pass


class HoleGame(Widget):
    score = NumericProperty(0)
    ball = ObjectProperty(None)
    hole = ObjectProperty(None)
    MAX_VELOCITY = 5

    def update(self, dt):
        self.ball.move()
        if self.ball.x < 0 or self.ball.right > self.width:
            self.ball.velocity_x = -self.ball.velocity_x
        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y = -self.ball.velocity_y
        if self.ball_in_hole():
            self.score += 1
            self.random_hole()

    def on_touch_down(self, touch):
        new_velocity = self.relative_position(touch.x, touch.y) * self.MAX_VELOCITY
        self.ball.velocity_x = new_velocity.x
        self.ball.velocity_y = new_velocity.y

    def relative_position(self, x, y):
        v = Vector(x, y)
        max_value = Vector(self.width, self.height).length()
        return (v - self.center)/max_value

    def random_hole(self, start=False):
        x = random.randint(self.ball.width/2, int(self.width - self.ball.width))
        y = random.randint(self.ball.height/2, self.height - self.ball.height)
        if start:
            x = random.randint(self.ball.width/2, 200)
            y = random.randint(self.ball.height/2, 300)
        self.hole.center = x, y

    def ball_in_hole(self):
        return (self.ball.x >= self.hole.x and self.ball.right <= self.hole.right ) or \
                (self.ball.y >= self.hole.y and self.ball.top <= self.hole.top)


class HoleApp(App):
    def build(self):
        game = HoleGame()
        game.random_hole(True)
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    HoleApp().run()
