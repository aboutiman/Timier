import tkinter as tk
import time

class TimerStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timier")
        self.is_timer_running = False
        self.timer_seconds = 0
        self.up_check = False
        self.down_check = False
        self.pause_check = False

        self.time_entry = tk.Entry(root, font=("Helvetica", 16))
        self.time_entry.insert(tk.END, "00:00:00")
        self.time_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=3)  # Adjust columnspan for the desired width

        self.timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 36))
        self.timer_label.grid(row=1, column=1, padx=0, pady=10)

        self.set_button = tk.Button(root, text="SET", command=self.set)
        self.set_button.grid(row=0, column=0, padx=5, pady=5)

        self.up_button = tk.Button(root, text="UP", command=self.up)
        self.up_button.grid(row=2, column=0, padx=5, pady=5)

        self.down_button = tk.Button(root, text="DOWN", command=self.down)
        self.down_button.grid(row=2, column=2, padx=5, pady=5)

        self.pause_button = tk.Button(root, text="PAUSE", command=self.pause)
        self.pause_button.grid(row=2, column=1, padx=5, pady=5)

        self.update_timer()

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
            return "-{:02d}:{:02d}:{:02d}".format(h, m, s)
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
