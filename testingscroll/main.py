from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder


class TestApp(App):
    pass

kv = Builder.load_file("test.kv")


class MyMainApp(App):
    def build(self):
        return kv