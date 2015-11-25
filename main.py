from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivy.properties import ObjectProperty
from kivy.clock import Clock


__version__ = "1.0"


class Ball(Widget):
    def move(self):
        self.pos = Vector(2, 3) + self.pos


class HoleGame(Widget):
    ball = ObjectProperty(None)

    def on_touch_down(self, touch):
        self.ball.center = touch.pos
        return True

    def update(self, dt):
        self.ball.move()


class HoleApp(App):
    def build(self):
        game = HoleGame()
        # Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    HoleApp().run()
