# import tkinter
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import threading
import time


class Timer:
    def __init__(self, parent):
        # variable storing time
        self.y = 0
        self.seconds = 0
        # label displaying time
        self.label = tk.Label(parent, text="0 s", font="Arial 30", width=10)
        self.label1 = tk.Label(parent, text=0)
        self.label.pack()
        self.label1.pack()
        # start the timer
        self.refresh_label()

    def refresh_label(self):
        """ refresh the content of the label every second """
        # increment the time
        self.seconds += 1
        for x in range(0, 5):
            self.label1.configure(text=self.y)
            self.y += 1
        # display the new time
        self.label.configure(text="%i s" % self.seconds)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
        self.label.after(1000, self.refresh_label)


class Licz:
    for x in range(0, 5):
        print("HEJ")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Winda")
    timer = threading.Thread(target=Timer, args=(root,))
    # licz = threading.Thread(target=Licz)
    timer.start()
    # licz.start()
    root.mainloop()
