from random import random
from tkinter import HIDDEN, NORMAL, Tk, Canvas, W        
root = Tk()

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)
    
    
    
def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)
    

def left_H(event):
    if event.x <= 180:
        PosiX = 180
    elif event.x >= 500:
        PosiX = 500
    else:
        PosiX = event.x
    
    if event.y <= 180:
        PosiY = 180
    elif event.y >= 700:
        PosiY = 700
    else:
        PosiY = event.y
    c.coords(hand_left,PosiX-30,PosiY-30, PosiX+30,PosiY+30)
    c.coords(arm_left,PosiX,PosiY,540,480)
    c.reset_hand_time = False
    
    
def right_H(event):
    if event.x <= 500:
        PosiX = 500
    elif event.x >= 800:
        PosiX = 800
    else:
        PosiX = event.x
    
    if event.y <= 200:
        PosiY = 200
        if c.act_hi%2 == 0:
            c.act_hi+=1
    elif event.y >= 700:
        PosiY = 700
        if c.act_hi%2 == 1:
            c.act_hi+=1
    else:
        PosiY = event.y
    c.coords(hand_right,PosiX-30,PosiY-30, PosiX+30,PosiY+30)
    c.coords(arm_right,530, 470,PosiX,PosiY)        
    c.reset_hand_time = False
    
def all_hand(event):
    right_H(event)
    left_H(event)
    c.act_hi-=1
    c.reset_hand_time = False

#background set
c = Canvas(root, width=1000, height=1000)
c.configure(bg='lemon chiffon', highlightthickness=0)
c.body_color = 'pink'

#all body
shadow = c.create_oval(100, 700, 800, 900, outline='gray82', fill='gray82')

arm_left = c.create_line(150, 510, 320,500,fill='black', width=25, smooth=1)
arm_right = c.create_line(600, 510, 750,500,fill='black', width=25)

body = c.create_polygon([100,800,550,100,315,270,405,270,500,275,800,800], outline='black',fill='lightsteelBlue2', smooth=1,width = '7')
body2 = c.create_polygon([170,750,620,100,320,270,405,270,450,275,750,750], outline='black',fill='azure2', smooth=1,width = '5')

head = c.create_oval(300, 500, 700, 150, outline='black',fill='pink',width = '5')

eye_left = c.create_oval(400, 300, 345, 350, outline='black',fill='white',state=NORMAL,width = '3')
eye_right = c.create_oval(600, 300, 550, 350, outline='black',fill='white',state=NORMAL,width = '3')

pupil_left = c.create_oval(400, 320, 370, 345, outline='gray15', fill='gray15',state=NORMAL)
pupil_right = c.create_oval(600, 320, 570, 345, outline='gray15', fill='gray15',state=NORMAL)

eyebrow_left = c.create_line(350, 270, 410, 300, fill='gray15', smooth=1, width=4)
eyebrow_right = c.create_line(550, 300, 610, 270, fill='gray15', smooth=1, width=4)

foot_left = c.create_oval(350, 780, 445, 820, outline='gray9', fill='gray9')
foot_right = c.create_oval(460, 780, 545, 820, outline='gray9', fill='gray9')

mouth_happy = c.create_line(400, 400,480, 500,550,400,fill='black', smooth=1, width=4)

hand_left = c.create_oval(120, 540, 180, 480, outline='black', fill='gold',width = '3')
hand_right = c.create_oval(720, 530, 780, 470, outline='black', fill='gold',width = '3')

hat = c.create_arc(700, 80, 300, 400, start=00, extent=180, fill="snow",width = '9')

c.pack()

root.after(3000, blink)
c.bind("<B1-Motion>", left_H)
c.bind("<B2-Motion>", all_hand)
c.bind("<B3-Motion>", right_H)

c.act_hi = 0




root.mainloop()

