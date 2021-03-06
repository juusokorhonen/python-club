from random import randint
from math import sqrt

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang.builder import Builder


DEFAULT_VELOCITY = (8, 0)
MAX_VELOCITY = 20


design_spec = """
#:kivy 1.0.9

<PongBall>:
    size: 50, 50
    canvas:
        Ellipse:
            pos: self.pos
            size: self.size

<PongPaddle>:
    size: 25, 200
    canvas: 
        Rectangle:
            pos:self.pos
            size: self.size

<PongGame>:
    ball: pong_ball
    player1: player_left
    player2: player_right

    canvas:
        Rectangle:
            pos: self.center_x - 5, 0
            size: 10, self.height

    Label:
        font_size: 70
        center_x: root.width / 4
        top: root.top - 50
        text: str(root.player1.score)

    Label:
        font_size: 70
        center_x: root.width * 3 / 4
        top: root.top - 50
        text: str(root.player2.score)

    PongBall:
        id: pong_ball
        center: self.parent.center

    PongPaddle:
        id: player_left
        x: root.x
        center_y: root.center_y

    PongPaddle:
        id: player_right
        x: root.width - self.width
        center_y: root.center_y
"""


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            if -0.95 > offset or offset > 0.95:
                offset *= 5
            print(f"DEBUG: {offset=}")
            bounced = Vector(-1 * vx, vy + offset)
            vel = bounced * 1.1
            vel_total = sqrt(vel.x**2 + vel.y**2)
            if abs(vel_total) > MAX_VELOCITY:
                scaler = (vel_total/MAX_VELOCITY)**2
                vel.x /= scaler
                vel.y /= scaler
            print(f"DEBUG: {vel_total=}")
            print(f"DEBUG: {vel=}")

            ball.velocity = vel.x, vel.y


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=DEFAULT_VELOCITY):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(DEFAULT_VELOCITY[0], DEFAULT_VELOCITY[1]))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-DEFAULT_VELOCITY[0], DEFAULT_VELOCITY[1]))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        Builder.load_string(design_spec, filename="pong.kv")
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


print("Creating PongApp...")
app = PongApp()
print("Running PongApp...")
app.run()
print("PongApp finished.")
