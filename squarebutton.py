from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class SquareButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Прозрачный фон
        self.size_hint = (None, None)  # Фиксированный размер

        with self.canvas.before:
            Color(0, 0.5, 1, 0)  # Синий цвет
            self.square = Rectangle(pos=self.pos, size=self.size)

        # Обновляем положение и размер квадрата при изменении кнопки
        self.bind(pos=self.update_square, size=self.update_square)

    def update_square(self, *args):
        self.square.pos = self.pos
        self.square.size = self.size