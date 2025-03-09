from kivy.graphics import Ellipse, Color
from kivy.core.window import Window
from kivy.uix.button import Button
class CircularButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Делаем фон прозрачным
        self.size_hint = (None, None)

        # Рисуем круг
        with self.canvas.before:
            Color(0, 0.5, 1, 0)  # Синий цвет
            self.circle = Ellipse(pos=self.pos, size=self.size)

        # Обновляем позицию круга при изменении позиции кнопки
        self.bind(pos=self.update_circle, size=self.update_circle)

    def update_circle(self, *args):
        self.circle.pos = self.pos
        self.circle.size = self.size