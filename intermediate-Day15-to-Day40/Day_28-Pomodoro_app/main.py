
import tkinter

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("PomoDoro App")
window.config(padx=100, pady=50, bg=YELLOW)

label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
label.grid(column=1, row=0)

tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(102, 112, image=tomato_img)

canvas.create_text(102, 130, text=f"00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_btn = tkinter.Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=3)

reset_btn = tkinter.Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=3)

new_label = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
new_label.grid(column=1, row=4)



window.mainloop()
