from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Ellipse, Color
from kivy.clock import Clock
import sys
import os
from kivy.clock import Clock
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from squarebutton import SquareButton
from circlebutton import CircularButton
Window.size=(1000,600)
Window.set_icon('safe-nobg.png')
class MyApp(App):
    def build(self):
        layout=FloatLayout()
        self.image=Image(source='safe.png',size_hint=(1,1),allow_stretch=True, keep_ratio=False)
        self.label1=Label(text='',font_size=30,pos_hint={"center_x": 0.5, "center_y": 0.34},color=(1,0,0,1))
        btn1=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2065,'center_y':0.555})
        btn2=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2247,'center_y':0.555})
        btn3=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2395,'center_y':0.555})
        btn4=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2065,'center_y':0.530})
        btn5=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2247,'center_y':0.530})
        btn6=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2395,'center_y':0.530})
        btn7=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2065,'center_y':0.51})
        btn8=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2247,'center_y':0.51})
        btn9=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2395,'center_y':0.51})
        btn10=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2065,'center_y':0.490})
        btn11=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2247,'center_y':0.490})
        btn12=SquareButton(text='',size=(20,15),pos_hint={'center_x': 0.2395,'center_y':0.490})
        self.btn_open=CircularButton(text='',size=(150,150),pos_hint={'center_x': 0.5,'center_y':0.54})
        self.label2 = TextInput(
            text='',
            hint_text="",
            font_size=10,
            size_hint=(0.06, 0.04),
            height=100,
            pos_hint={"center_x": 0.225, "center_y": 0.59},
            background_normal="",  # Отключаем стандартный фон
            background_color=(0, 0, 0, 1),  # Белый фон
            foreground_color=(1, 1, 1, 1),  # Чёрный текст,
            multiline=False,
            readonly=True
        )

        layout.add_widget(self.image)
        layout.add_widget(self.btn_open)
        layout.add_widget(self.label1)
        layout.add_widget(self.label2)
        self.textinputed=''
        for button in (btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12):
            layout.add_widget(button)
        btn1.bind(on_press=self.on_button_press1)
        btn2.bind(on_press=self.on_button_press2)
        btn3.bind(on_press=self.on_button_press3)
        btn4.bind(on_press=self.on_button_press4)
        btn5.bind(on_press=self.on_button_press5)
        btn6.bind(on_press=self.on_button_press6)
        btn7.bind(on_press=self.on_button_press7)
        btn8.bind(on_press=self.on_button_press8)
        btn9.bind(on_press=self.on_button_press9)
        btn10.bind(on_press=self.meow)
        btn11.bind(on_press=self.on_button_press0)
        btn12.bind(on_press=self.ok)
        return layout
    def on_button_press1(self,inst):
        self.label2.text+='*'
        self.textinputed+='1'
    def on_button_press2(self,inst):
        self.label2.text+='*'
        self.textinputed+='2'
    def on_button_press3(self,inst):
        self.label2.text+='*'
        self.textinputed+='3'
    def on_button_press4(self,inst):
        self.label2.text+='*'
        self.textinputed+='4'
    def on_button_press5(self,inst):
        self.label2.text+='*'
        self.textinputed+='5'
    def on_button_press6(self,inst):
        self.label2.text+='*'
        self.textinputed+='6'
    def on_button_press7(self,inst):
        self.label2.text+='*'
        self.textinputed+='7'
    def on_button_press8(self,inst):
        self.label2.text+='*'
        self.textinputed+='8'
    def on_button_press9(self,inst):
        self.label2.text+='*'
        self.textinputed+='9'
    def on_button_press0(self,inst):
        self.label2.text+='*'
        self.textinputed+='0'
    def ok(self,inst):
        self.label2.text=''
        if self.textinputed=='532625':           
            self.label2.background_color=(0,1,0,1)
            self.btn_open.bind(on_press=self.opensafe)
        else:
            self.label2.background_color=(1,0,0,1)
            Clock.schedule_once(self.incorrect,2)
        self.textinputed=''
    def incorrect(self,insta,*args):
        self.label2.background_color=(0,0,0,1)
    def meow(self,insta):
        self.label2.text=''
        self.textinputed=''
    def opensafe(self,insta):
        self.stop()
        SecondApp().run()
class SecondApp(App):
    def build(self):
        Window.set_icon('gold.png')
        layout=FloatLayout()
        self.image=Image(source='gold.png',size_hint=(1,1),allow_stretch=True, keep_ratio=False)
        self.button=Button(text='Обратно',size_hint_y=None,pos_hint={'center_x': 0.5,'center_y': 0.95})
        self.button.bind(on_press=self.back_to_safe)
        layout.add_widget(self.image)
        layout.add_widget(self.button)
        return layout    
    def back_to_safe(self,insta):
        self.stop()
        MyApp().run()
if __name__=='__main__':
    MyApp().run()