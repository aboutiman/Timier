import tkinter as tk

class TimerStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.overrideredirect(False)
        self.root.geometry("400x260")
        self.root.config(bg="#1e1e1e")  # Set the background color to a dark gray
        # transparency_level = 220
        # root.wm_attributes("-alpha", transparency_level/255)
        root.resizable(False, False)
        self.root.iconbitmap("timer.png")
        self.moveable = False
        self.root.bind("<ButtonPress-1>", self.on_drag_start)
        self.root.bind("<B1-Motion>", self.on_drag_motion)

        self.title_label = tk.Label(root, text='TIMIER', font=("Courier New", 16,"bold"), fg="white", bg="#1e1e1e", padx=10)
        self.title_label.grid(row=0, column=1)

        self.close_button = tk.Button(root, text="         EXIT       ", command=self.on_close, bg="#282828", fg="white", relief=tk.FLAT)
        self.close_button.grid(row=0, column=2)


        self.is_timer_running = False
        self.timer_seconds = 0
        self.up_check = False
        self.down_check = False
        self.pause_check = False

        self.time_entry = tk.Entry(root, font=("Courier New", 16), bg="#282828", fg="white", insertbackground="white", relief=tk.FLAT)
        self.time_entry.insert(tk.END, "00:00:00")
        self.time_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

        self.timer_label = tk.Label(root, text="00:00:00", font=("Courier New", 36, "bold"), fg="white", bg="#1e1e1e")
        self.timer_label.grid(row=2, column=1, padx=0, pady=10)

        self.set_button = tk.Button(root, text="SET", command=self.set, bg="#282828", fg="white", activebackground="#0066b3", relief=tk.FLAT)
        self.set_button.grid(row=1, column=0, padx=5, pady=5)

        self.up_button = tk.Button(root, text="  UP  ", font=("Palatino Linotype", 12,"bold"), command=self.up, bg="grey", fg="white", activebackground="#398546", relief=tk.FLAT)
        self.up_button.grid(row=3, column=0, padx=5, pady=5)

        self.down_button = tk.Button(root, text="DOWN", font=("Palatino Linotype", 12,"bold"), command=self.down, bg="grey", fg="white", activebackground="#c64747", relief=tk.FLAT)
        self.down_button.grid(row=3, column=2, padx=0, pady=0)

        self.pause_button = tk.Button(root, text="PAUSE", command=self.pause, bg="grey", fg="black", activebackground="#e5bb00", relief=tk.FLAT)
        self.pause_button.grid(row=3, column=1, padx=5, pady=0)
        
        self.email_label = tk.Label(root, text='contact us: im74an@gmail.com', font=("Courier New", 10,"bold"), fg="white", bg="#282828", padx=10)
        self.email_label.grid(row=5, column=1, pady=20)

        self.always_on_top_var = tk.BooleanVar()
        self.always_on_top_button = tk.Checkbutton(root, text="on top", font=("Courier New", 8), variable=self.always_on_top_var, command=self.toggle_always_on_top, bg="#1e1e1e", fg="white", selectcolor="#1e1e1e", activebackground="#1e1e1e")
        self.always_on_top_button.grid(row=0, column=0)

        self.light_theme = tk.BooleanVar()
        self.light_theme_button = tk.Checkbutton(root, text="light", font=("Courier New", 8), variable=self.light_theme, command=self.light_theme_toggle, bg="#1e1e1e", fg="white", selectcolor="#1e1e1e", activebackground="#1e1e1e")
        self.light_theme_button.grid(row=5, column=0)



        self.update_timer()

    def on_close(self):
        self.root.destroy()

    def toggle_always_on_top(self):
        if self.always_on_top_var.get():
            self.root.overrideredirect(True)
            self.moveable = True
        else:
            self.root.overrideredirect(False)
            self.moveable = False
        self.root.attributes("-topmost", self.always_on_top_var.get())

    def light_theme_toggle(self):
        if self.light_theme.get():
            self.root.config(bg="#E8E8E8")
            self.title_label.config(bg="#E8E8E8", fg="#282828")
            self.close_button.config(bg="white", fg="#282828")
            self.time_entry.config(bg="light grey", fg="grey", insertbackground="black")
            self.timer_label.config(fg="grey", bg="#E8E8E8")
            self.set_button.config(bg="light grey", fg="#282828")
            self.up_button.config(bg="white", fg="black")
            self.down_button.config(bg="white", fg="black")
            self.pause_button.config(bg="white", fg="grey")
            self.email_label.config(fg="#282828", bg="#E8E8E8")
            self.always_on_top_button.config(bg="#E8E8E8", fg="black", selectcolor="white", activebackground="white")
            self.light_theme_button.config(bg="#E8E8E8", fg="black", selectcolor="white", activebackground="white")

        else:
            self.root.config(bg="#1e1e1e")
            self.title_label.config(fg="white", bg="#1e1e1e")
            self.close_button.config(bg="#282828", fg="white")
            self.time_entry.config(bg="#282828", fg="white", insertbackground="white")
            self.timer_label.config(fg="white", bg="#1e1e1e")
            self.set_button.config(bg="#282828", fg="white")
            self.up_button.config(bg="grey", fg="white")
            self.down_button.config(bg="grey", fg="white")
            self.pause_button.config(bg="grey", fg="black")
            self.email_label.config(fg="white", bg="#282828")
            self.always_on_top_button.config(bg="#1e1e1e", fg="white", selectcolor="#1e1e1e", activebackground="#1e1e1e")
            self.light_theme_button.config(bg="#1e1e1e", fg="white", selectcolor="#1e1e1e", activebackground="#1e1e1e")
            

    # Methods for dragging the window
    def on_drag_start(self, event):
        self._drag_data = {"x": event.x, "y": event.y}

    def on_drag_motion(self, event):
        if self.moveable:
            x = self.root.winfo_x() + (event.x - self._drag_data["x"])
            y = self.root.winfo_y() + (event.y - self._drag_data["y"])
            self.root.geometry("+{}+{}".format(x, y))

    def update_timer(self):
        if self.is_timer_running:
            if self.up_check:
                self.timer_seconds += 1
                self.timer_label.config(text=self.format_time(self.timer_seconds))
            elif self.down_check:
                self.timer_seconds -= 1
                self.timer_label.config(text=self.format_time(self.timer_seconds))
            elif self.pause_check:
                self.timer_seconds -= 0
                self.timer_label.config(text=self.format_time(self.timer_seconds))

        self.root.after(1000, self.update_timer)

    def up(self):
        if not self.is_timer_running:
            self.is_timer_running = True
        if not self.up_check:
            self.up_check = True
            self.down_check = False
            self.pause_check = False
            self.pause_button.config(text = "PAUSE", command = self.pause)

    def down(self):
        if not self.is_timer_running:
            self.is_timer_running = True
        if not self.down_check:
            self.up_check = False
            self.down_check = True
            self.pause_check = False
            self.pause_button.config(text = "PAUSE", command = self.pause)

    def pause(self):
        if self.is_timer_running:
            if not self.pause_check:
                self.up_check = False
                self.down_check = False
                self.pause_check = True
                self.pause_button.config(text = "RESET")
                self.pause_button.config(command = self.reset)
            else:
                self.pause_button.config(command = self.pause)

    def reset(self):
        if self.is_timer_running:
            self.timer_seconds = 0
            self.pause_button.config(text = "PAUSE", command = self.pause)
            self.timer_label.config(text=self.format_time(self.timer_seconds))
            self.pause_check = False
            self.is_timer_running = False

    def format_time(self, seconds):
        if seconds < 0:
            seconds *= -1
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return "-{:01d}:{:02d}:{:02d}".format(h, m, s)
        else:
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            return "{:02d}:{:02d}:{:02d}".format(h, m, s)
        
    def set(self):
        time_str = self.time_entry.get()
        h, m, s = map(int, time_str.split(":"))
        total_seconds = h * 3600 + m * 60 + s
        self.timer_seconds = total_seconds
        self.timer_label.config(text=self.format_time(self.timer_seconds))

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerStopwatchApp(root)
    root.mainloop()
