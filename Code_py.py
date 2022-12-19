import rotatescreen as rt
from time import sleep as sp
screen = rt.get_primary_display()
for i in range (0,13):
    sp(1)
    screen.rotate_to(i * 90 %360)
    
