from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import pandas as pd
from kivy.core.window import Window 


class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass
    

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):  
    pass
    
class FifthWindow(Screen):
    
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("test.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
    Window.close()
    
