# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:17:35 2022

@author: kelly
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window 


def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
            

class RootWidget(BoxLayout):
    def __init__(self, **kwargs): 
        super(RootWidget, self).__init__(**kwargs)

    def play1(self):
        print("Twinkle")
    
    def play2(self):
        print("HotCrossBuns")

    def light1(self):
        print("Twinkle")
        
    def light2(self):
        print("HotCrossBuns")
    
    

class TestApp(App):
    def build(self):
        return RootWidget()
    
    def process(self):
        text = self.root.ids.input.text
        print(text)

if __name__ == '__main__':
    reset()
    TestApp().run()
    Window.close()