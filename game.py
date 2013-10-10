import curses
import random
from sys import exit
from time import sleep

myscreen = curses.initscr()
curses.curs_set(0)
curses.noecho()
x = 25
y = 25
ent_x = 0
ent_y = 0
kling_x = 0
kling_y = 0


def grid(x,y):
	myscreen.move(10,10)
	for a in range (1,x):
		for b in range(1,y):
                	myscreen.addstr(a, b, ".")

def klingon_start(a,b):
        global kling_x
        global kling_y
        x = random.randint(1,a)
        y = random.randint(1,b)
	myscreen.addstr(x,y,"K")
        kling_x = x
        kling_y = y


def enterprise_start(a,b):
	global ent_x
	global ent_y
	x = random.randint(1,a)
	y = random.randint(1,b)
	myscreen.addstr(x,y,"e")
	ent_x = x
	ent_y = y

def enterprise_move(d):
	global ent_x,kling_x
	global ent_y,kling_y
	old_x = ent_x
	old_y = ent_y

	
	if d == "u":
	
           	if ent_x > 1:
                       	ent_x -= 1
                       	return
               	else:
                       	ent_x= 1
	                return
	elif d == "d":
		colided()
                if ent_x < 24:
                        ent_x += 1
                        return
                else:
                        ent_x= 24
                        return
	elif d == "l":
		colided()
                if ent_y > 1:
                        ent_y -= 1
                        return
                else:
                        ent_y= 1
                        return
	elif d == "r":
		colided()
                if ent_y < 24 :
                        ent_y += 1
                        return
                else:
                        ent_y= 24
                        return




def draw_screen():
	global ent_x,ent_y,kling_x,kling_y
	grid(x,y)
	myscreen.addstr(ent_x,ent_y,"e")
	myscreen.addstr(kling_x,kling_y,"K")
	myscreen.addstr(0,30,"ent_x %s"% ent_x)
	myscreen.addstr(1,30,"ent_y %s"% ent_y)
	myscreen.addstr(3,30,"kling_x %s"% kling_x)
        myscreen.addstr(4,30,"kling_y %s"% kling_y)
	myscreen.refresh()

def draw_weapon():
	global ent_x,ent_y,kling_x,kling_y
	weap_x = ent_x+1
	weap_y = ent_y
	draw_screen()
	myscreen.addstr(weap_x,weap_y,"*")
	myscreen.refresh()
	sleep(0.2)
	for i in range(1,4):
		weap_x += 1
		draw_screen()
		myscreen.addstr(weap_x,weap_y,"*")
		myscreen.refresh()
		if weap_x == kling_x and weap_y == kling_y:
			curses.flash()
			myscreen.addstr(kling_x,kling_y,".")
			break
		else:
			sleep(0.2)
			draw_screen()
def colided():
	global ent_x,ent_y,kling_x,kling_y

	if ent_x == kling_x and ent_y == kling_y:
		return True
	else:
		
		return	False	
grid(x,y)
enterprise_start(x,y)
klingon_start(x,y)
while True:
	#key = myscreen.getch()
	draw_screen()
	#myscreen.addstr(29,30,"Keycode; %s"%key)
	
        coll = colided()        
	if coll is True:
		myscreen.addstr(7,30,"collsion detected")
                myscreen.refresh()
		#draw_screen()
	else:
		myscreen.addstr(7,30,"collsion not detected")
                myscreen.refresh()
	key = myscreen.getch()
	myscreen.addstr(29,30,"Keycode; %s"%key)
	if key == 113:
		curses.endwin()
		exit(0)
	elif key == 65:
		enterprise_move("u")
		#draw_screen()
	elif key == 66:
                enterprise_move("d")
                #draw_screen()
	elif key == 68:
                enterprise_move("l")
                #draw_screen()
	elif key == 67:
                enterprise_move("r")
                #draw_screen()
	elif key == 32:
		draw_weapon()
	else:	
		draw_screen()

	draw_screen()
#curses.endwin()
