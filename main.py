import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivy.properties import ObjectProperty, NumericProperty
from kivy.clock import Clock


__version__ = "1.0"


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    def move(self):
        self.pos = Vector(self.velocity_x, self.velocity_y) + self.pos


class Hole(Widget):
    pass


class HoleGame(Widget):
    score = NumericProperty(0)
    ball = ObjectProperty(None)
    hole = ObjectProperty(None)
    spring_stregth = NumericProperty(0.0005)
    spring_vertex = None
    MAX_VELOCITY = 5

    def update(self, dt):
        if self.spring_vertex is not None:
            v = Vector(self.spring_vertex.x - self.ball.center_x, self.spring_vertex.y - self.ball.center_y)
            self.ball.velocity_x, self.ball.velocity_y = v.x * self.spring_stregth + self.ball.velocity_x, \
                                                         v.y * self.spring_stregth + self.ball.velocity_y
        self.ball.move()
        if self.ball.x < 0 or self.ball.right > self.width:
            self.ball.velocity_x = -self.ball.velocity_x
        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y = -self.ball.velocity_y
        if self.ball_in_hole():
            self.score += 1
            self.random_hole()

    def on_touch_down(self, touch):
        self.spring_vertex = touch

    def on_touch_up(self, touch):
        self.spring_vertex = None

    def relative_position(self, x, y):
        v = Vector(x, y)
        max_value = Vector(self.width, self.height).length()
        return (v - self.center)/max_value

    def random_hole(self):

        x = random.randint(0, self.width - self.hole.width) + self.hole.width/2
        y = random.randint(0, self.height - self.hole.height) + self.hole.height/2
        self.hole.center = x, y

    def ball_in_hole(self):
        return (self.ball.x >= self.hole.x and self.ball.right <= self.hole.right ) and \
                (self.ball.y >= self.hole.y and self.ball.top <= self.hole.top)


class HoleApp(App):
    def build(self):
        game = HoleGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    HoleApp().run()
