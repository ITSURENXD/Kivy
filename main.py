from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
"""Button also needs to be imported"""
from kivy.uix.button import Button

"""NOTE: Most of the class names are hardfast rules so try to stick to the standard. for most cases, you just need to have the same name of the class in the kv file and it will work"""

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