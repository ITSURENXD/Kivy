# Defaults for object
    pos: 0px,0px or 0dp, odp
    size: 100px, 100px or 40dp, 40dp (size of a finger)
    color: red,green,blue,transparency(gamma) where 1=100%
    #no need to write px as it is default
    #px is useless because scren size changes, use dp (density indenpendent pixels) instead
    
    pos: 100dp,200dp
    size:: 40dp,40dp

# Widgets
    Widgets are defined by <MainWidget>
    DISADVANTAGE: can't accomodate for change in screen size

# Layouts
1. Box Layout:
stack vertically and horizontally 

2. Anchor Layout
puts objects on all sides of the screen

3. Grid Layout 
puts objects in the column and row format. It is *mandatory* to specify rows and cols.
[IMP] Size_hint may not work here because of multiple rows or column.

4. StackLayout:
gets stacked on multiple lines. need size of elements, which can be indiviaully unique. However they may not be scrolled hence the need of scroll view

5. Scroll view:
one long object that can be scrolled. [IMP] needs size of the item to be scrolled: we can use self.minimum_height to get away most of the times

6. Page layout:
Page like layout

Layouts can't use size and pos as they are decided by the layout itself based on the availabe screen   space. However, we may use the size_hint and pos_hint to give a size based on proportion to its default size where 1=100%
Also, layouts CAN use size and pos if we put size_hint: None,None. In this case, width and height can be used instead of size

# Embedding
Layouts can be imbedded inside another layout of different kind. and can be spaced with a __spacing: "<number> dp"__

# shortcuts
Instead of creating classes in the py file we can simply define it in the kv with <anme of the class>@<layout>

# final steps
- we copied the directory to linux subsystem with: __sudo cp -r  /mnt/d/get_closest/development /__ (here mnt is to access windows files and / it the default directory on linux)
- we ran: __buildozer init__ to create a buidozer.spec file [IMP] while on the main.py hosting directory
- we changed the app names and added .ttf in include of builder.spec file for custom fonts
- we used: __buildozer android debug deploy run__ to create the apk on the bin folder on the main.py hosting directory
- we went to a loop of **Waiting for app to start** but apk was already made so we __ctrl c__ out of it and copied it to the phone and installed it
-[IMP] we used __buildozer android clean__ everytime we chaged somethingin the buildozer.spec file
