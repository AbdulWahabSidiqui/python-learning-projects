from tkinter import *
import time

BG = "#0F172A"
PANEL = "#1E293B"
TEXT = "#F8FAFC"
ACCENT = "#2DD4BF"

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.state("zoomed")
        self.window.title("Dangerous Writing App")
        self.window.config(bg=BG)
        self.time_left = 5
        self.timer = None

        self.main = Frame(self.window,bg=BG)
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.main.grid(row=0,column=0,sticky="nsew", padx=40, pady=30)

        self.title_label = Label(self.main, text="Dangerous Writing App",font=("Segoe UI", 28, "bold"),bg=BG,fg=ACCENT)
        self.title_label.grid(row=0,column=0,pady=(20,10))

        self.subheading_label = Label(self.main,text="Keep typing! If you stop for 5 seconds,everything will be deleted.",font=("Segoe UI", 14),bg=BG,fg=TEXT)
        self.subheading_label.grid(row=1,column=0,pady=(0,20))

        self.countdown_label = Label(self.main,text="Time Remaining: 5",font=("Segoe UI", 14),bg=BG,fg=TEXT)
        self.countdown_label.grid(row=2,column=0,pady=(0,20))

        self.text_area = Text(self.main,width=80,height=22,font=("Consolas", 14),wrap="word",bg=PANEL,fg=TEXT,insertbackground=TEXT,relief="flat",padx=15,pady=15)
        self.text_area.focus_set()
        self.text_area.bind("<KeyPress>",self.reset_timer)
        self.text_area.grid(row=3,column=0,pady=(0,20),padx=40,sticky="nsew")
        self.main.rowconfigure(3, weight=1)
        self.main.columnconfigure(0, weight=1)

        self.window.mainloop()



    def reset_timer(self,event):
        if self.timer is not None:
            self.window.after_cancel(self.timer)
        self.time_left = 5
        self.countdown_label.config(text=f"Time Remaining: {self.time_left}")
        if self.text_area.get("1.0","end").strip():
            self.countdown()

    def countdown(self):
        self.countdown_label.config(text=f"Time Remaining: {self.time_left}")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer = self.window.after(1000,self.countdown)
        else:
            self.text_area.delete("1.0",END)
            self.countdown_label.config(text="Time Remaining: 0")



ui = GUI()

