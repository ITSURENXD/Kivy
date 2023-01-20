from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty,BooleanProperty,NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
"""Button also needs to be imported"""
from kivy.uix.button import Button

#for python code in 2nd part
class WidgetsExample(GridLayout):
    #no need for an initiator as we are not initiating anything
    count=0
    count_enable=BooleanProperty(False)
    my_text = StringProperty("0")
    textinputs = StringProperty("Type Something")
    def on_button_click(self):
        print("Button Clicked")
        if self.count_enable==True:
            self.count+=1

        #[IMP] use self to change the value on the scope of the class and not function
        self.my_text=str(self.count)

    def on_toggle(self,widget):
        if widget.state=="normal":
            widget.text="OFF" #no need for string properrty as the widget is passed as an argument
            self.count_enable=False
        else:
            widget.text="ON"
            self.count_enable=True

    def on_switch(self,widget):
        if widget.active==True:
            print("switch on")
        else: 
            print("switch off")

    # on_slider(self,widget):
        #print(f"The slider value is {int(widget.value)}")
    
    def on_text_validates(self,widget):
        self.textinputs=widget.text
        


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