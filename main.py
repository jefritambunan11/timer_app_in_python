from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
WHITE = "#ffffff"
FONT_NAME = "Arial"
WORK_MIN = 1
BREAK_MIN = 1
is_running = False
state = None

def start_timer():
	start_btn.config(state="disabled")
	reset_btn.config(state="normal")
	global state, is_running
	is_running = True
	if state is None: state = 'work'
	if state == 'work':
		lbl.config(
			text = "WORK", 
			fg = BLACK
		)
		work_in_seconds = WORK_MIN * 60 
		count_down(work_in_seconds)
	else:
		lbl.config(
			text = "BREAK", 
			fg = BLACK
		)
		break_in_seconds = BREAK_MIN * 60 
		count_down(break_in_seconds)		

def count_down(count):
	if is_running:
		if count > -1:
			count_min = math.floor(count/60)
			count_sec = count % 60  
			if len(str(count_min)) < 2: count_min = f"0{str(count_min)}" 			
			if len(str(count_sec)) < 2: count_sec = f"0{str(count_sec)}" 		
			tk.after(1_000, count_down, count-1) 
			canvas.itemconfig(
				timer_text, 
				text = f"{count_min}:{count_sec}"
			)
		else:
			global state
			if state == 'work': 
				state = 'break'
			else:
				state = 'work'
			start_timer()

def reset_timer():
	global state, is_running
	if  is_running:
		state = None
		is_running = False
		start_btn.config(state="normal")
		reset_btn.config(state="disabled")
		canvas.itemconfig(
			timer_text, 
			text = "00:00"
		)
		lbl.config(
			text = "Stopped"
		) 

tk = Tk()
tk.title("Aplikasi Hitung Waktu Sederhana - Jefri Tambunan")
tk.config(
	padx = 100, 
	pady = 50, 
	bg = YELLOW
) 
tk.resizable(False, False)  

lbl = Label(
	text = "TIMER", 
	bg = YELLOW, 
	fg = BLACK, 
	font = ("Arial", 80, "bold"), 
) 
lbl.grid(
	column = 1, 
	row = 0
)

canvas = Canvas(
	width = 200, 
	height = 224, 
	bg = YELLOW, 
	highlightthickness = 0
)
watch = PhotoImage(
	file = "watch.png"
)
canvas.create_image(
	100, 
	112, 
	image = watch
)
timer_text = canvas.create_text(
	100, 
	130, 
	text = "00:00", 
	fill = "#000000", 
	font = (FONT_NAME, 100, "bold")
)
canvas.grid(column=1, row=1)

start_btn = Button(
	text = "Start", 
	bg = None, 
	highlightthickness = 0, 
	command = start_timer
)
start_btn.grid(
	column = 0, 
	row = 2
)

reset_btn = Button(
	text = "Reset", 
	bg = None, 
	highlightthickness = 0,
	command = reset_timer,
	state = "disabled"
)
reset_btn.grid(
	column = 2, 
	row = 2
)

marks_lbl = Label(
	text = "Made By Jefri Tambunan", 
	bg = YELLOW, 
	fg = BLACK
)
marks_lbl.grid(
	column=1, 
	row=2
)

git = Label(
	text = "github.com/jefritambunan11", 
	bg = YELLOW, 
	fg = BLACK
)
git.grid(
	column=1, 
	row=3
) 

tk.mainloop()