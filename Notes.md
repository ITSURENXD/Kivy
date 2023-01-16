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
    1) Box Layout:
        stack vertically and horizontally 

    2) Anchor Layout
        puts objects on all sides of the screen

    3) Grid Layout 
        puts objects in the column and row format 

    4) Scroll view:
        one long object that can be scrolled

    5) Page layout:
        Page like layout

    Layouts can't use size and pos as they are decided by the layout itself based on the availabe screen   space. However, we may use the size_hint and pos_hint to give a size based on proportion to its default size where 1=100%
    Also, layouts CAN use size and pos if we put size_hint: None,None. In this case, width and height can be used instead of size
