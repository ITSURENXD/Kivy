from kivy.app import App
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
"""Button also needs to be imported"""
from kivy.uix.button import Button

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation= "rl-tb"
        for i in range(0,100):
            #these 100 hundreds intems are not scrollable
            b=Button(text=f"stack {i}", size_hint=(None,None), size=(dp(100),dp(100)))
            self.add_widget(b)

#class GridLayoutExampl(GridLayout): Unnecesary as we can simply do <GridLayoutExample@GridLayout> in kv
    #pass

class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    #this is just an example, doing it in kv file is better unless you need to looop it
    """ #just for inheritance and for loops 
        def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #Button iniltialization 
        b1 = Button(text="Hello")
        b2 = Button(text="World")
        b3 = Button(text=".")

        #default is horizontal
        self.orientation="vertical"
        #this is first come, first served. Order is important 
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)"""
    

#for all the widgets 
class MainWidget(Widget):
    pass

#the App might be needed
class LabsApp(App):
    pass

LabsApp().run()